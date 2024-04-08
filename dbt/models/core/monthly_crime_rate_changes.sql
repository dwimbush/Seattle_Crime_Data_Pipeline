-- models/core/monthly_crime_rate_changes.sql

{{ config(materialized='table') }}

WITH monthly_crimes AS (
  SELECT
    EXTRACT(YEAR FROM report_datetime) AS year,
    EXTRACT(MONTH FROM report_datetime) AS month,
    COUNT(*) AS total_crimes
  FROM
    {{ ref('stg_seattle_crime') }}
  GROUP BY
    year, month
),

monthly_changes AS (
  SELECT
    *,
    LAG(total_crimes) OVER (ORDER BY year, month) AS prev_month_crimes,
    ((total_crimes - LAG(total_crimes) OVER (ORDER BY year, month)) / LAG(total_crimes) OVER (ORDER BY year, month)) * 100 AS percentage_change
  FROM
    monthly_crimes
)

SELECT
  year,
  month,
  total_crimes,
  prev_month_crimes,
  percentage_change
FROM
  monthly_changes
ORDER BY
  year, month

--dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
-- {% if var('is_test_run', default=true) %}

--     limit 100
    
-- {% endif %}
-- models/core/crime_time_series.sql

{{ config(materialized='table') }}

WITH base AS (
  SELECT
    DATE(report_datetime) AS report_date,
    group_a_b
  FROM
    {{ ref('stg_seattle_crime') }}
)

SELECT
  report_date,
  COUNT(*) AS total_crimes,
  COUNTIF(group_a_b = 'A') AS group_a_crimes,
  COUNTIF(group_a_b = 'B') AS group_b_crimes
FROM
  base
GROUP BY
  report_date
ORDER BY
  report_date

--dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
-- {% if var('is_test_run', default=true) %}

--     limit 100
    
-- {% endif %}
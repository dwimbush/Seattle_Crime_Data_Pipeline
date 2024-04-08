-- models/core/highest_crime_hour_by_precinct.sql

{{ config(materialized='table') }}

WITH hourly_crimes AS (
  SELECT
    precinct,
    EXTRACT(HOUR FROM report_datetime) AS hour_of_day,
    COUNT(*) AS incident_count
  FROM
    {{ ref('stg_seattle_crime') }}
  GROUP BY
    precinct, hour_of_day
),

ranked_hours AS (
  SELECT
    *,
    RANK() OVER (PARTITION BY precinct ORDER BY incident_count DESC) AS rank
  FROM
    hourly_crimes
)

SELECT
  precinct,
  hour_of_day,
  incident_count
FROM
  ranked_hours
WHERE
  rank = 1
ORDER BY
  precinct, hour_of_day

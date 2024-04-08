-- models/recent_crime_activity.sql

{{ config(materialized='table') }}

WITH recent_crimes AS (
  SELECT
    offense,
    precinct,
    EXTRACT(DAYOFWEEK FROM report_datetime) AS day_of_week,
    COUNT(*) AS incident_count
  FROM
    {{ ref('stg_seattle_crime') }} 
  WHERE
    report_datetime >= CURRENT_DATE - INTERVAL 7 DAY
  GROUP BY
    offense, precinct, day_of_week
)

SELECT
  offense,
  precinct,
  CASE
    WHEN day_of_week = 1 THEN 'Sunday'
    WHEN day_of_week = 2 THEN 'Monday'
    WHEN day_of_week = 3 THEN 'Tuesday'
    WHEN day_of_week = 4 THEN 'Wednesday'
    WHEN day_of_week = 5 THEN 'Thursday'
    WHEN day_of_week = 6 THEN 'Friday'
    WHEN day_of_week = 7 THEN 'Saturday'
  END AS day_of_week_str,
  incident_count
FROM
  recent_crimes
ORDER BY
  precinct, offense, day_of_week
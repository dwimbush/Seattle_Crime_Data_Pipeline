-- models/crime_by_day_of_week.sql

{{ config(materialized='table') }}

SELECT
  FORMAT_DATE('%A', report_datetime) AS day_of_week,
  COUNT(*) AS incident_count
FROM
  {{ ref('stg_seattle_crime') }}
GROUP BY
  day_of_week
ORDER BY
  CASE day_of_week
    WHEN 'Sunday' THEN 1
    WHEN 'Monday' THEN 2
    WHEN 'Tuesday' THEN 3
    WHEN 'Wednesday' THEN 4
    WHEN 'Thursday' THEN 5
    WHEN 'Friday' THEN 6
    WHEN 'Saturday' THEN 7
  END

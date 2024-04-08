-- models/core/crime_hotspots_by_hour.sql

{{ config(materialized='table') }}

SELECT
  EXTRACT(HOUR FROM report_datetime) AS hour_of_day,
  COUNT(*) AS incident_count
FROM
  {{ ref('stg_seattle_crime') }}
GROUP BY
  hour_of_day
ORDER BY
  hour_of_day DESC
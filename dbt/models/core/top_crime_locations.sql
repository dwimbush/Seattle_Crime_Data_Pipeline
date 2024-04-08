-- models/core/top_crime_locations.sql

{{ config(materialized='table') }}

SELECT
  ROUND(longitude, 3) AS rounded_longitude,
  ROUND(latitude, 3) AS rounded_latitude,
  COUNT(*) AS incident_count
FROM
  {{ ref('stg_seattle_crime') }}
WHERE
  longitude <> 0.0 AND latitude <> 0.0
GROUP BY
  rounded_longitude, rounded_latitude
ORDER BY
  incident_count DESC
LIMIT 10
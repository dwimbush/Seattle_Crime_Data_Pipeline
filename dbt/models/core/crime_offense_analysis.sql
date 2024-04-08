-- models/core/crime_offense_analysis.sql

{{ config(materialized='table') }}

SELECT
  crime_against_category,
  offense,
  COUNT(*) AS incident_count
FROM
  {{ ref('stg_seattle_crime') }}
GROUP BY
  crime_against_category,
  offense
ORDER BY
  incident_count DESC
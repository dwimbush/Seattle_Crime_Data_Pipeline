-- models/core/crime_category_analysis.sql

{{ config(materialized='table') }}

SELECT
  crime_against_category,
  offense_parent_group,
  COUNT(*) AS incident_count
FROM
  {{ ref('stg_seattle_crime') }}
GROUP BY
  crime_against_category,
  offense_parent_group
ORDER BY
  incident_count DESC
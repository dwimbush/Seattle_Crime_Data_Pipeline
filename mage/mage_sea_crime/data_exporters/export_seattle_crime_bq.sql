CREATE OR REPLACE TABLE `seattle-crime-48435.crime_dataset.seattle_crime_partitioned`
PARTITION BY pseudo_partition_date
AS
SELECT
  *,
  DATE_TRUNC(DATE(report_datetime), MONTH) as pseudo_partition_date
FROM
  {{ df_1 }};

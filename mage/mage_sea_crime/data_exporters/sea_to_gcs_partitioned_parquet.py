import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Assuming necessary imports and initial setup are already in place.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/key.json"

bucket_name = 'seattle-crime-48435-bucket'
table_name = "seattle_crime_data"

# This path is used for operations that require the bucket/key format.
root_path_for_operations = f'{bucket_name}/{table_name}'

# Initialize GCS filesystem interface.
fs = pa.fs.GcsFileSystem()

@data_exporter
def export_data(data, *args, **kwargs):
    data['report_year'] = data['report_datetime'].dt.strftime('%Y')

    unique_years = data['report_year'].unique()
    for year in unique_years:
        year_data = data[data['report_year'] == year]

        # Specific year's data is filtered.
        partition_path = f'report_year={year}'

        # Listing all objects in the partition to prepare for deletion.
        objects_in_partition = fs.get_file_info(pa.fs.FileSelector(f'{root_path_for_operations}/{partition_path}', recursive=True))
        for obj_info in objects_in_partition:
            if obj_info.type == pa.fs.FileType.File:
                # Deleting the file using the bucket/key format.
                fs.delete_file(obj_info.path)

        # Writing the filtered DataFrame to the dataset.
        pq.write_to_dataset(
            pa.Table.from_pandas(year_data),
            root_path=f'{bucket_name}/{table_name}',  # Full GCS URI is used here correctly for writing.
            partition_cols=['report_year'],
            filesystem=fs
        )
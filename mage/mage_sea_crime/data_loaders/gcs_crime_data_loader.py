import pandas as pd
import pyarrow.parquet as pq
from google.cloud import storage
import io
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_all_years_from_google_cloud_storage(*args, **kwargs):
    print('Starting data loader...')

    # Directly use the credentials file path here instead of loading from YAML to avoid parsing issues
    creds_path = "/home/src/key.json"  # Update this path to your actual credentials file path

    print(f'Using Google Cloud credentials from: {creds_path}')
    client = storage.Client.from_service_account_json(creds_path)
    bucket_name = 'seattle-crime-48435-bucket'
    base_path = 'seattle_crime_data'

    start_year = 2008
    end_year = 2024

    dfs = []
    for year in range(start_year, end_year + 1):
        prefix = f'{base_path}/report_year={year}/'
        blobs = client.list_blobs(bucket_name, prefix=prefix)
        for blob in blobs:
            if blob.name.endswith('.parquet'):
                print(f'Reading file: gs://{bucket_name}/{blob.name}')
                blob_data = blob.download_as_bytes()
                df_year = pd.read_parquet(io.BytesIO(blob_data), engine='pyarrow')
                dfs.append(df_year)

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df
    else:
        print('No data was loaded. Returning an empty DataFrame.')
        return pd.DataFrame()

@test
def test_output(output, *args) -> None:
    print('Testing output...')
    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output DataFrame is empty'
    print('Test passed. Data loaded successfully.')

import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """ Load data from the Seattle Open API with pagination and ordering 
    """
    print("Starting data download...")
    api_url = 'https://data.seattle.gov/resource/tazs-3rd5.csv'
    page_size = 50000  # Adjust based on API limits and considerations
    order_by = 'report_number'  # Replace with the actual field name you want to order by
    records = []
    offset = 0

    sf_crime_dtype = {
                    "report_number":pd.StringDtype(),
                    "offense_id":pd.Int64Dtype(),
                    "group_a_b":pd.StringDtype(),
                    "crime_against_category":pd.StringDtype(),
                    "offense_parent_group":pd.StringDtype(),
                    "offense":pd.StringDtype(),
                    "offense_code":pd.StringDtype(),
                    "precinct":pd.StringDtype(),
                    "sector":pd.StringDtype(),
                    "beat":pd.StringDtype(),
                    "mcpp":pd.StringDtype(),
                    "_100_block_address":pd.StringDtype(),
                    "longitude":pd.Float64Dtype(),
                    "latitude":pd.Float64Dtype()
}
    parse_dates = ["offense_start_datetime", "offense_end_datetime", "report_datetime" ]

    while True:
        # Construct the API request URL with offset, limit, and order
        request_url = f"{api_url}?$limit={page_size}&$offset={offset}&$order={order_by}"
        print(f"Requesting data from URL: {request_url}")
        
        # Make the API request
        response = requests.get(request_url)
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
            break
        
        # Load the CSV data from response
        df = pd.read_csv(io.StringIO(response.text), dtype=sf_crime_dtype, parse_dates=parse_dates)

        # Manually parse datetime columns to handle potential parsing issues
        # with non-standard or malformed date strings.
        # Using `errors='coerce'` converts problematic data to `NaT` (Not a Time)
        # instead of raising an error. This allows the DataFrame to be created without
        # interruption and enables subsequent inspection of problematic date entries.
        for date_column in parse_dates:
            df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        
        # Check if the dataframe is empty
        if df.empty:
            print("No more data to retrieve.")
            break
        
        # Add the retrieved data to your records list
        records.append(df)
        
        # Update the offset for the next iteration
        offset += page_size
        print(f"Downloaded {len(df)} records. Total records downloaded: {sum(len(r) for r in records)}")
    
    # Concatenate all dataframes into a single dataframe
    if records:
        final_df = pd.concat(records, ignore_index=True)
    else:
        final_df = pd.DataFrame()
     
    print("Data download completed.")
    return final_df

@test
def test_output(output, *args) -> None:
    """
    Test the output of the load_data_from_api function.
    """
    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output dataframe is empty'
    assert isinstance(output, pd.DataFrame), 'The output is not a pandas DataFrame'
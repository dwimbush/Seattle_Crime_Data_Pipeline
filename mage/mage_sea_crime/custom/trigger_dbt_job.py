import requests
from mage_ai.data_preparation.decorators import data_exporter
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@custom
def trigger_dbt_run(data_frame, *args, **kwargs):
    account_id = '255399'  # your dbt Cloud account ID
    job_id = '565791'  # your dbt Cloud job ID
    # dbt_api_token = 'dbtc_hPnMbiYfiL8MIbWssRPJA24hcqtv58isXtR37tRs-vM95l6VMc'  # your dbt Cloud API token

    dbt_api_token = os.getenv('DBT_API_TOKEN')  # Read the dbt Cloud API token from environment variable

    if not dbt_api_token:
        print("DBT_API_TOKEN environment variable is not set.")
        return None

    url = f'https://cloud.getdbt.com/api/v2/accounts/{account_id}/jobs/{job_id}/run/'
    headers = {
        'Authorization': f'Token {dbt_api_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'cause': 'Triggered from Mage.ai',  # Add a meaningful description for the cause of the run
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200 or response.status_code == 201:
        print('dbt Cloud job triggered successfully.')
        return response.json()  # Returns the response from the dbt Cloud API
    else:
        print(f'Failed to trigger dbt Cloud job. Status code: {response.status_code}')
        print(f'Response: {response.text}')
        return None


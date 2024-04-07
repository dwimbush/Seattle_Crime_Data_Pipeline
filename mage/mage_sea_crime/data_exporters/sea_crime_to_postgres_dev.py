from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path
from mage_ai.orchestration.triggers.api import trigger_pipeline

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """
    schema_name = 'crime'  # Specify the name of the schema to export data to
    table_name = 'seattle_crime'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:    
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

trigger_pipeline(
    'seattle_crime_gcs_to_bigquery', # the UUID of the pipleline to trigger; only required parameter
    variables={}, # Runtime variables for the pipeline.
    check_status=False, # Poll and check the status of the triggered pipeline.
    error_on_failure=False, # Raise an exception if the triggered pipeline fails.
    poll_interval=60, # Check the status of triggered pipeline every N seconds.
    poll_timeout=None, # After N seconds have elapsed, raise an exception if the triggered pipeline hasn’t finished running successful.
    schedule_name=None,  # Enter a unique name to create a new trigger each time
    verbose=True, # Print status of triggered pipeline run.
)
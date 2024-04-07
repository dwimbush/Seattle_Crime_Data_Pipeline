from mage_ai.orchestration.triggers.api import trigger_pipeline

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

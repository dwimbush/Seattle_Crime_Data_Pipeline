from mage_ai.seetings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'seattle-crime-48435-bucket'
    object_key = 'seattle-crime-48435'

    return BoogleCloudStorage.with_confgi(ConfigFileLoader(config_path)
        bucket_name,
        object_key
    )
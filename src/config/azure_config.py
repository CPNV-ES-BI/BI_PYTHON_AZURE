# -----------------------------------------------------------------------------------  
# File   :   azure_config.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   Attribute are set from these environnment variables:
#            - AZURE_STORAGE_CONNECTION_STRING
#            - AZURE_CONTAINER_NAME
# -----------------------------------------------------------------------------------

import os

class AzureConfig:
    """Retrieves and verifies the environment variables needed for an Azure configuration"""

    _ENV_CONNECTION_STRING = "AZURE_STORAGE_CONNECTION_STRING"
    _ENV_CONTAINER_NAME = "AZURE_CONTAINER_NAME"

    _connection_string: str        
    _container_name: str
    
    def __init__(self) -> None:
        """Constructor

        Raises:
            ValueError: if the connection string or the container name env variable
            are not set.

        """
        if not self._env_var_does_exist():
            raise ValueError("Missing attributes: connection string or container name")
        self._connection_string = os.environ[self._ENV_CONNECTION_STRING]
        self._container_name = os.environ[self._ENV_CONTAINER_NAME]

    def _env_var_does_exist(self) -> bool:
        if not self._ENV_CONNECTION_STRING in os.environ or not self._ENV_CONTAINER_NAME in os.environ:
            return False
        return True
    
    @property
    def connection_string(self):
        return self._connection_string

    @property
    def container_name(self):
        return self._container_name


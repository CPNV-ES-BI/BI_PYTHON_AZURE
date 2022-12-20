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

    __connection_string: str        
    __container_name: str
    
    def __init__(self) -> None:
        """Constructor

        Raises:
            ValueError: if the connection string or the container name env variable
            are not set.

        """
        self._set_connection_string(os.environ["AZURE_STORAGE_CONNECTION_STRING"])
        self._set_container_name(os.environ["AZURE_CONTAINER_NAME"])

    # Protected setter
    def _set_connection_string(self, connection_string: str):
        if not connection_string:
            raise ValueError("Connection string is empty.")
        self.__connection_string = connection_string

    @property
    def connection_string(self):
        return self.__connection_string

    # Protected setter
    def _set_container_name(self, container_name: str):
        if not container_name:
            raise ValueError("Container name is empty.")
        self.__container_name = container_name

    @property
    def container_name(self):
        return self.__container_name


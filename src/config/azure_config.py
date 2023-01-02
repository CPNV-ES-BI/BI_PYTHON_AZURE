# -----------------------------------------------------------------------------------  
# File   :   azure_config.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   Attribute are set from these environnment variables:
#            - AZURE_STORAGE_CONNECTION_STRING
# -----------------------------------------------------------------------------------

import os

class AzureConfig:
    """Retrieves and verifies the environment variables needed for an Azure configuration"""

    _ENV_CONNECTION_STRING = "AZURE_STORAGE_CONNECTION_STRING"

    _connection_string: str    

    def __init__(self) -> None:
        """Constructor

        Raises:
            ValueError: if the connection string env variable is not set.
        """
        if not self._ENV_CONNECTION_STRING in os.environ:
            raise ValueError("Missing attribute: connection string")
        self._connection_string = os.environ[self._ENV_CONNECTION_STRING]
    
    @property
    def connection_string(self):
        return self._connection_string
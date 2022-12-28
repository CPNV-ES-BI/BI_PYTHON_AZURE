# -----------------------------------------------------------------------------------  
# File   :   client.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
#            TODO get BlobServiceClient for container
# -----------------------------------------------------------------------------------

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from src.config.azure_config import AzureConfig

class Client:
    """Provide the appropriate client based on AzureConfig instance"""

    _config: AzureConfig
    _service_client: BlobServiceClient

    def __init__(self) -> None:
        """Constructor
        
        Raises: 
            ValueError: refer AzureConfig constructor

        """
        self._init_azure_config()
        self._init_service_client()
    
    def _init_azure_config(self)-> None:
        """Init AzureConfig Object
        
        Raises: 
            ValueError: refer AzureConfig constructor
    
        """
        self._config = AzureConfig()

    def _init_service_client(self) -> None:
        self._service_client = BlobServiceClient.from_connection_string(self._config.connection_string)

    @staticmethod
    def get_container_client() -> ContainerClient:
        """Returns ContainerClient based on AzureConfig values

        Returns:
            ContainerClient: A client to interact with the specified container in AzureConfig
        """
        client: Client = Client()
        return client._service_client.get_container_client(client._config.container_name)


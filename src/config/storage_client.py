# -----------------------------------------------------------------------------------  
# File   :   client.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
#            TODO get BlobServiceClient for container
# -----------------------------------------------------------------------------------

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from src.config.azure_config import AzureConfig

class StorageClient:
    """Provide the appropriate client based on AzureConfig instance"""

    _config: AzureConfig
    _blob_service_client: BlobServiceClient
    

    def __init__(self) -> None:
        """Constructor
        
        Raises: 
            ValueError: refer AzureConfig constructor

        """
        self._config = AzureConfig()
        self._service_client = BlobServiceClient.from_connection_string(self._config.connection_string)      

    @property 
    def blob_service_client(self) -> BlobServiceClient:
        return self._service_client
    
    def get_container_client(self, container_name: str) -> ContainerClient:
        return self._service_client.get_container_client(container_name)

    def get_blob_client(self, container_name: str, blob_name: str) -> BlobClient:
        return self._service_client.get_blob_client(container_name, blob_name)    
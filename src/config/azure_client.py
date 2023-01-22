from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from src.config.azure_config import AzureConfig


class AzureClient:
    """Provide the appropriate client based on AzureConfig

    Notes
    ---
    Manages the closing of the connection when the instance is destroyed

    """

    __service_client: BlobServiceClient

    def __init__(self) -> None:
        """Constructor
        
        Raises: 
            ValueError: refer AzureConfig constructor
        """
        self._config = AzureConfig()
        self.__service_client = BlobServiceClient.from_connection_string(self._config.connection_string)

    def __del__(self):
        """ Destructor

         Close the connection to the BlobServiceClient

        """
        self.__service_client.close()

    def get_blob_service_client(self) -> BlobServiceClient:
        return self.__service_client
    
    def get_container_client(self, container_name: str) -> ContainerClient:
        return self.__service_client.get_container_client(container_name)

    def get_blob_client(self, container_name: str, blob_name: str) -> BlobClient:
        return self.__service_client.get_blob_client(container_name, blob_name)

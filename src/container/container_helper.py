# -----------------------------------------------------------------------------------  
# File   :   container_helper.py
# Author :   Mélodie Ohan
# Version:   02-01-2022 - original (dedicated to BI1)
# Remarks:   
# -----------------------------------------------------------------------------------

from interface.data_object import DataObject
from config.storage_client import StorageClient

class ContainerHelper:

    _storage_client: StorageClient

    def __init__(self, storage_client: StorageClient) -> None:
        self._storage_client = storage_client

    def does_exist(self, object_name: str) -> bool:
        return self._storage_client.get_container_client(object_name).exists()

    def create(self, object_name: str) -> None:
        self._storage_client.blob_service_client.create_container(object_name)
    
    def delete(self, object_name: str) -> None:
        self._storage_client.blob_service_client.delete_container(object_name)
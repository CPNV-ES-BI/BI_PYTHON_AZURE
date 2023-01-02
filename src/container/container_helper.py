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
        containers: list = self._storage_client.blob_service_client.list_containers(object_name)
        for container in containers:
            if container.name == object_name:
                return True
        return False

    def create(self, object_name: str) -> None:
        self._storage_client.blob_service_client.create_container(object_name)

    def download(self, object_path: str) -> str:
        pass

    def publish(self, object_path: str) -> None:
        pass
    
    def delete(self, object_name: str) -> None:
        self._storage_client.blob_service_client.delete_container(object_name)
# -----------------------------------------------------------------------------------  
# File   :   container_helper.py
# Author :   Mélodie Ohan
# Version:   02-01-2022 - original (dedicated to BI1)
# Remarks:   
# -----------------------------------------------------------------------------------

from interface.data_object import DataObject
from src.config.azure_client import AzureClient
from blob.blob_helper import BlobHelper   


class ContainerHelper(DataObject):

    _storage_client: AzureClient

    def __init__(self, storage_client: AzureClient) -> None:
        if not storage_client:
            raise ValueError("Missing parameter: AzureClient")
        self._storage_client = storage_client

    def does_exist(self, container_name: str) -> bool:
        return self._storage_client.get_container_client(container_name).exists()

    def create(self, container_name: str) -> None:
        if self.does_exist(container_name):
             raise Exception(f"container `{container_name}` already exists.")
        self._storage_client.get_blob_service_client().create_container(container_name)

    def publish(self, container_name: str) -> str:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        raise NotImplementedError("It is not possible yet to define a public container.")     

    def download(self, container_name: str) -> list[bytes]:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        blobs: list = self._storage_client.get_container_client(container_name).list_blobs()
        result = list[bytes]()
        for blob in blobs:
            data: list[bytes] = BlobHelper(self._storage_client, container_name).download(blob.name)
            if data:
                result.append(data[0])
        return result

    def delete(self, container_name: str) -> None:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        self._storage_client.get_blob_service_client().delete_container(container_name)
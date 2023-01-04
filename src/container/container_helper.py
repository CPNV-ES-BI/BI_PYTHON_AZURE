# -----------------------------------------------------------------------------------  
# File   :   container_helper.py
# Author :   Mélodie Ohan
# Version:   02-01-2022 - original (dedicated to BI1)
# Remarks:   
# -----------------------------------------------------------------------------------

from interface.data_object import DataObject
from config.storage_client import StorageClient
from blob.blob_helper import BlobHelper
from utils.file_helper import FileHelper

class ContainerHelper(DataObject):

    _storage_client: StorageClient

    def __init__(self, storage_client: StorageClient) -> None:
        self._storage_client = storage_client

    def does_exist(self, container_name: str) -> bool:
        return self._storage_client.get_container_client(container_name).exists()

    def create(self, container_name: str) -> None:
        if self.does_exist(container_name):
             raise Exception(f"container `{container_name}` already exists.")
        self._storage_client.blob_service_client.create_container(container_name)
    
    def download(self, container_name: str, local_path: str) -> str:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        blobs: list = self._storage_client.get_container_client(container_name).list_blobs()
        for blob in blobs:
            blob_helper = BlobHelper(container_name)
            blob_helper.download(blob.name, local_path)
        return local_path

    def delete(self, container_name: str) -> None:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        self._storage_client.blob_service_client.delete_container(container_name)
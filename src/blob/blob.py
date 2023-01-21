# -----------------------------------------------------------------------------------  
# File   :   blob_helper.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import os

from interface.data_object import DataObject
from src.config.azure_client import AzureClient
from azure.storage.blob import ContainerClient, BlobClient, StorageStreamDownloader

class Blob(DataObject):

    _storage_client: AzureClient
    _container_name: str
    
    def  __init__(self, storage_client: AzureClient, container_name: str) -> None:
        self._storage_client = storage_client
        self._container_name = container_name

    def __blob_client(self, blob_name: str) -> BlobClient:
        return self._storage_client.get_blob_client(self._container_name, blob_name)
    
    def __container_client(self) -> ContainerClient:
        return self._storage_client.get_container_client(self._container_name)

    def does_exist(self, blob_name: str) -> bool:
        return self.__blob_client(blob_name).exists()

    def create(self, blob_name: str, local_file_path: str) -> None:

        if self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` already exists.")

        if not os.path.exists(local_file_path):
            self.__blob_client(blob_name).upload_blob(data="")
        else:
            with open(local_file_path, "rb") as data:
                self.__blob_client(blob_name).upload_blob(data=data)

    def download(self, blob_name: str) -> list[bytes]:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        downloaded_response = self.__blob_client(blob_name).download_blob()
        return [downloaded_response.readall()]
        
    def publish(self, blob_name: str) -> str:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        raise NotImplementedError("It is not possible yet to define a public blob.")
          
    def delete(self, blob_name: str, recusrive: bool = True) -> None:
 
        blobs = list(self.__container_client().list_blob_names(name_starts_with=blob_name))
        if not len(blobs):
            raise Exception(f"No blob starts with `{blob_name}` does not exist.")
        for blob in blobs:
            self.__blob_client(blob).delete_blob()

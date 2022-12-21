# -----------------------------------------------------------------------------------  
# File   :   blob_helper.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from interface.data_object import DataObject
from config.client import Client
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient

class BlobHelper(DataObject):

    _client: ContainerClient
    
    def  __init__(self, client: ContainerClient) -> None:
        self._client = client

    def does_exist(self, object_path: str) -> bool:
        matches = self._client.list_blob_names(name_starts_with=object_path)
        for blob_name in matches:
            if blob_name == blob_name:
                return True
        return False

    def create(self, object_path: str, local_file_path: str) -> None:
        if self.does_exist(object_path):
            raise Exception(f"blob `{object_path}` already exists.")
                     
        with open(local_file_path, "rb") as data:
            self._client.upload_blob(name=object_path, data=data) 

    def download(self, object_path: str) -> str:
        return self._client.download_blob(object_path)

    def publish(self, object_path: str) -> None:
        # TODO find a way to set a blob public
        pass
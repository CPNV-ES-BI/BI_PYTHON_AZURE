# -----------------------------------------------------------------------------------  
# File   :   blob_helper.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import os

from interface.data_object import DataObject
from src.config.azure_client import AzureClient
from azure.storage.blob import ContainerClient, PublicAccess
from utils.file_helper import FileHelper

class BlobHelper(DataObject):

    _container_client: ContainerClient
    
    def  __init__(self, storage_client: AzureClient, container_name: str) -> None:
        self._container_client = storage_client.get_container_client(container_name)

    def _get_blob_client(self, blob_name: str):
        return self._container_client.get_blob_client(blob_name)

    def does_exist(self, blob_name: str) -> bool:
        return self._get_blob_client(blob_name).exists()

    def is_public(self, blob_name: str) -> bool:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        properties = self._get_blob_client(blob_name).get_blob_properties()
        return properties.public_access == PublicAccess.Blob

    def create(self, blob_name: str, local_file_path: str) -> None:
        self._get_blob_client(blob_name)

        if self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` already exists.")

        if not os.path.exists(local_file_path):
            self._container_client.upload_blob(name=blob_name, data="")
        else:
            with open(local_file_path, "rb") as data:
                self._container_client.upload_blob(name=blob_name, data=data)
      
    def delete(self, blob_name: str) -> None:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        self._container_client.delete_blob(blob_name)

    def download(self, blob_name: str, local_path: str) -> str:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        downloaded_response = self._container_client.download_blob(blob_name)
        return FileHelper().make_from_path(local_path, blob_name, downloaded_response.readall())
        
    def publish(self, blob_name: str) -> None:
        if not self.does_exist(blob_name):
            raise Exception(f"blob `{blob_name}` does not exist.")
        raise NotImplementedError("It is not possible yet to define a public blob.")
        #
        # TODO set a blob public 
        #
        # permission = ContainerSasPermissions(read=True)
        # access_policy = AccessPolicy(permission)
        # identifiers = {'test': access_policy}
        # self._container_client.set_container_access_policy(signed_identifiers=identifiers, public_access=blob_name)
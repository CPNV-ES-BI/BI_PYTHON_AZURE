# -----------------------------------------------------------------------------------  
# File   :   container_helper.py
# Author :   Mélodie Ohan
# Version:   02-01-2022 - original (dedicated to BI1)
# Remarks:   
# -----------------------------------------------------------------------------------

from utils.file_helper import FileHelper
from interface.data_object import DataObject
from src.config.azure_client import AzureClient
from blob.blob_helper import BlobHelper   


class ContainerHelper(DataObject):

    _storage_client: AzureClient

    def __init__(self, storage_client: AzureClient) -> None:
        self._storage_client = storage_client

    def does_exist(self, container_name: str) -> bool:
        return self._storage_client.get_container_client(container_name).exists()

    def create(self, container_name: str) -> None:
        if self.does_exist(container_name):
             raise Exception(f"container `{container_name}` already exists.")
        self._storage_client.get_blob_service_client().create_container(container_name)

    def delete(self, container_name: str) -> None:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        self._storage_client.get_blob_service_client().delete_container(container_name)
    
    def download(self, container_name: str, local_path: str) -> str:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        blobs: list = self._storage_client.get_container_client(container_name).list_blobs()
        local_path = FileHelper().join_path(local_path, container_name)
        for blob in blobs:
            blob_helper = BlobHelper(self._storage_client, container_name)
            blob_helper.download(blob.name, local_path)
        return local_path
    
    def publish(self, container_name: str) -> None:
        if not self.does_exist(container_name):
            raise Exception(f"container `{container_name}` does not exist.")
        raise NotImplementedError("It is not possible yet to define a public container.")
        # TODO
        # unable to implement set_container_access_policy(), publicAccess (from container_client)
        #access_policy = AccessPolicy(permission=ContainerSasPermissions(read=True),
        #                        expiry=datetime.utcnow() + timedelta(hours=1),
        #                        start=datetime.utcnow() - timedelta(minutes=1))
        #identifiers = {'test': access_policy}
        # container_client = self._storage_client.get_container_client(container_name)
        #container_client.set_container_access_policy(identifiers, public_access=)

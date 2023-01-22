# -----------------------------------------------------------------------------------
# File   :   blob_helper.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import os

from azure.storage.blob import ContainerClient, BlobClient, StorageStreamDownloader

from interface.data_object import DataObject
from config.azure_client import AzureClient

from blob.errors.blob_already_exists_error import BlobAlreadyExistsError
from blob.errors.blob_does_not_exist_error import BlobDoesNotExistError


class BlobHelper(DataObject):
    """Provide methods for performing operations on blobs

    Notes
    ---
    It is not possible to change the access level of a blob.
    In order to do so, you have to temporary set the container access policy to public.
    Refer to ContainerHelper set_container_public_read_access method.

    """

    _storage_client: AzureClient

    _container_name: str

    def __init__(self, storage_client: AzureClient, container_name: str) -> None:
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
            raise BlobAlreadyExistsError(f"blob `{blob_name}` already exists.")

        if not os.path.exists(local_file_path):
            self.__blob_client(blob_name).upload_blob(data="")
        else:
            with open(local_file_path, "rb") as data:
                self.__blob_client(blob_name).upload_blob(data=data)

    def download(self, blob_name: str) -> list[bytes]:
        if not self.does_exist(blob_name):
            raise BlobDoesNotExistError(f"blob `{blob_name}` does not exist.")

        downloaded_response: StorageStreamDownloader = self.__blob_client(blob_name).download_blob()

        return downloaded_response.readall()

    def publish(self, blob_name: str) -> str:
        if not self.does_exist(blob_name):
            raise BlobDoesNotExistError(f"blob `{blob_name}` does not exist.")

        return self.__blob_client(blob_name).url

    def _recursive_delete(self, blob_name: str):
        blobs = list(self.__container_client().list_blobs(name_starts_with=blob_name))
        if not len(blobs):
            raise BlobDoesNotExistError(f"No blob starts with `{blob_name}` does not exist.")
        for blob in blobs:
            self.__container_client().delete_blob(blob.name)

    def delete(self, blob_name: str, recursive: bool = True) -> None:
        if recursive:
            self._recursive_delete(blob_name)
        else:
            if not self.does_exist(blob_name):
                raise BlobDoesNotExistError(f"blob `{blob_name}` does not exist.")
            self.__blob_client(blob_name).delete_blob()

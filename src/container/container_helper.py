# -----------------------------------------------------------------------------------  
# File   :   container_helper.py
# Author :   Mélodie Ohan
# Version:   22-01-2022 - original (dedicated to BI1)
# Remarks:   
# -----------------------------------------------------------------------------------

from datetime import datetime, timedelta
from azure.storage.blob import ContainerSasPermissions, PublicAccess, AccessPolicy

from interface.data_object import DataObject
from config.azure_client import AzureClient
from container.errors.container_already_exists_error import ContainerAlreadyExistsError
from container.errors.container_does_not_exist_error import ContainerDoesNotExistError
from container.errors.container_forbidden_operation_error import ContainerForbiddenOperationError


class ContainerHelper(DataObject):
    """Provide methods for performing operations on container"""

    _storage_client: AzureClient

    def __init__(self, storage_client: AzureClient) -> None:
        if not storage_client:
            raise ValueError("Missing parameter: AzureClient")
        self._storage_client = storage_client

    def does_exist(self, container_name: str) -> bool:
        return self._storage_client.get_container_client(container_name).exists()

    def create(self, container_name: str, local_file_path: str = None) -> None:
        if local_file_path is not None:
            raise ContainerForbiddenOperationError("Container creation is not based on a file path.")
        if self.does_exist(container_name):
            raise ContainerAlreadyExistsError(f"Container `{container_name}` already exists.")
        self._storage_client.get_blob_service_client().create_container(container_name)

    def publish(self, container_name: str) -> str:
        raise ContainerForbiddenOperationError("This operation is not possible on container.")

    def download(self, container_name: str) -> bytes:
        raise ContainerForbiddenOperationError("This operation is not possible on container")

    def delete(self, container_name: str, recursive: bool = True) -> None:
        if not recursive:
            raise ContainerForbiddenOperationError("Deleting a container means deleting all its contents")
        if not self.does_exist(container_name):
            raise ContainerDoesNotExistError(f"Container `{container_name}` does not exist.")
        self._storage_client.get_blob_service_client().delete_container(container_name)

    def set_container_public_read_access(self, container_name: str) -> None:
        """Set the container access policy to the provided access

        Args:
            container_name: str       Data object name

        Raises:
            ContainerDoesNotExistError if the container does not exist
        """
        if not self.does_exist(container_name):
            raise ContainerDoesNotExistError(f"Container `{container_name}` does not exist.")
        access_policy = AccessPolicy(permission=ContainerSasPermissions(read=True, write=True),
                                     expiry=datetime.utcnow() + timedelta(hours=1),
                                     start=datetime.utcnow() - timedelta(minutes=1))
        identifiers = {'read': access_policy}
        public_access = PublicAccess.Container
        self._storage_client.get_container_client(container_name)\
            .set_container_access_policy(signed_identifiers=identifiers,public_access=public_access)

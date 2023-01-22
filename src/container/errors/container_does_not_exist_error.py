from container.errors.container_error import ContainerError


class BlobDoesNotExistError(ContainerError):
    """Raised when trying to perform an operation on a container that does not exist"""
    pass

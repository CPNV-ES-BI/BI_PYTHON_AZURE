from container.errors.container_error import ContainerError


class ContainerForbiddenOperationError(ContainerError):
    """Raised when trying to perform a forbidden or not possible operation on a container"""
    pass

from container.errors.container_error import ContainerError


class ContainerAlreadyExistsError(ContainerError):
    """Raised when creating an already existing container"""
    pass

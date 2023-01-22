# -----------------------------------------------------------------------------------
# File   :   container_does_not_exist_error.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from container.errors.container_helper_error import ContainerHelperError


class ContainerDoesNotExistError(ContainerHelperError):
    """Raised when trying to perform an operation on a container that does not exist"""
    pass

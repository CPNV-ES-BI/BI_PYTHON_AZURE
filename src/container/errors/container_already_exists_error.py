# -----------------------------------------------------------------------------------
# File   :   container_already_exists_error.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from container.errors.container_helper_error import ContainerHelperError


class ContainerAlreadyExistsError(ContainerHelperError):
    """Raised when creating an already existing container"""
    pass

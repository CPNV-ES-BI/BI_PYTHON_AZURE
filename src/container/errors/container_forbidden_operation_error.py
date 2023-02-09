# -----------------------------------------------------------------------------------
# File   :   container_forbidden_operation_error.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from container.errors.container_helper_error import ContainerHelperError


class ContainerForbiddenOperationError(ContainerHelperError):
    """Raised when trying to perform a forbidden or not possible operation on a container"""
    pass

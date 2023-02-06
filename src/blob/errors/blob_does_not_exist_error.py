# -----------------------------------------------------------------------------------
# File   :   blob_does_not_exist_error.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from blob.errors.blob_helper_error import BlobHelperError


class BlobDoesNotExistError(BlobHelperError):
    """Raised when trying to perform an operation on a blob that does not exist"""
    pass

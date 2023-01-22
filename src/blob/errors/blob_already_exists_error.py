# -----------------------------------------------------------------------------------
# File   :   blob_already_exists_error.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from blob.errors.blob_helper_error import BlobHelperError


class BlobAlreadyExistsError(BlobHelperError):
    """Raised when creating an already existing blob"""
    pass

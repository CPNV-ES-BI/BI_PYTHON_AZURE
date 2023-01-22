from blob.errors.blob_error import BlobError


class BlobAlreadyExistsError(BlobError):
    """Raised when creating an already existing blob"""
    pass

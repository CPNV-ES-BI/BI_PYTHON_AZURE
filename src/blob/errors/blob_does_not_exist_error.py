from blob.errors.blob_error import BlobError


class BlobDoesNotExistError(BlobError):
    """Raised when trying to perform an operation on a blob that does not exist"""
    pass

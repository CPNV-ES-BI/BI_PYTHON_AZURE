from interface.errors.data_object_error import DataObjectError


class DataObjectDoesNotExistError(DataObjectError):
    """Raised when trying to perform an operation on an object that does not exist"""
    pass

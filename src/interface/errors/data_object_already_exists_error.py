from interface.errors.data_object_error import DataObjectError


class DataObjectAlreadyExistsError(DataObjectError):
    """Raised when creating an already existing object"""
    pass

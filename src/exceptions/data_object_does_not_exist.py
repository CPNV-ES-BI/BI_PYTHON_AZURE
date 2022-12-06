from .data_object_exception import DataObjectException


class DataObjectDoesNotExist(DataObjectException):
    "Occurs when an operation is done on an object that does not exist "
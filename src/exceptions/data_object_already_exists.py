from .data_object_exception import DataObjectException


class DataObjectAlreadyExists(DataObjectException):
    "Occurs when a DataObject alrady exists"
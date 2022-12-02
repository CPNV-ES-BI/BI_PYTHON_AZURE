from .abc_data_object import ABCDataObject
from .exceptions.data_object_already_exists import DataObjectAlreadyExists

class DataObject(ABCDataObject):

    @staticmethod
    def does_exist(identifier: str) -> bool:
        raise NotImplementedError("Not implemented!")

    @staticmethod
    def create_object(identifier: str, path: str = '') -> object:
        raise NotImplementedError("Not implemented!")

    @staticmethod
    def download_object(identifier: str) -> object:
        raise NotImplementedError("Not implemented!")

    @staticmethod
    def publish_object(identifier: str):
        raise NotImplementedError("Not implemented!")
    
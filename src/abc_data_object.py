from abc import ABC, abstractmethod



class ABCDataObject(ABC):
    
    _identifier: str
    _path: str

    @abstractmethod
    def does_exist(identifier: str) -> bool:
        pass

    @abstractmethod
    def create_object(identifier: str, path: str = '') -> object:
        pass

    @abstractmethod
    def download_object(identifier: str) -> object:
        pass

    @abstractmethod
    def publish_object(identifier: str):
        pass
    
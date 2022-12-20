# -----------------------------------------------------------------------------------  
# File   :   blob_helper.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from interface.data_object import DataObject

class BlobHelper(DataObject):
    """Blob Data Object helper
    Implementation of DataObject class
    """
    
    def does_exist(self, object_name: str) -> bool:
        raise NotImplementedError("Not implemented!")

    def create(self, object_name: str, local_file_path: str) -> object:
        raise NotImplementedError("Not implemented!")

    def download(self, data_object_name: str, filepath: str) -> None:
        raise NotImplementedError("Not implemented!")

    def publish(self, object_name: str, local_file_path: str) -> None:
        raise NotImplementedError("Not implemented!")

# -----------------------------------------------------------------------------------
# File   :   data_object.py
# Author :   Mélodie Ohan
# Version:   22-01-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

class DataObject:
    """DataObject interface
    
    All methods must be implemented in inheriting class.

    Notes
    ---
    There is no explicit interface implementation, no keyword interface in the current Python version.
    In order to "implement" DataObject, make your data object inherit from this class.

    """

    def does_exist(self, object_name: str) -> bool:
        """Check if the data object exists in the distant storage

        Args:
            object_name: str       Data object name

        """
        raise NotImplementedError("Not implemented!")

    def create(self, object_name: str, local_file_path: str = None) -> None:
        """Create the data object in the distant storage

        Args:
            object_name: str       Data object name
            local_file_path: str   For cases where the object needs a local file path

        Raises: 
            errors.DataObjectError if the object already exists

        """
        raise NotImplementedError("Not implemented!")

    def download(self, object_name: str) -> bytes:
        """Return the bytes necessary to write the downloaded object

        Args:
            object_name: str       Data object name

        Returns: 
            A list that contain the bytes of the downloaded object

        Raises: 
            errors.DataObjectError if the object does not exist

        """
        raise NotImplementedError("Not implemented!")

    def publish(self, object_name: str) -> str:
        """ Make the content

        Args:
            object_name: str       Data object name (file.extension)

        Returns:
            str public link
        
        Raises: 
            errors.DataObjectError if the object does not exist

        """
        raise NotImplementedError("Not implemented!")

    def delete(self, object_name: str, recursive: bool = False) -> None:
        """Delete the data object by its name. 
        Will delete recursively if the recursive parameter is true.

        Args:
            object_name: str     Data object name (file.extension)
            recursive: bool      Indicate to recursively delete data object content

        Raises: 
            errors.DataObjectError if the object does not exist

        """
        raise NotImplementedError("Not implemented!")

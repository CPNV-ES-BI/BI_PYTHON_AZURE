# -----------------------------------------------------------------------------------  
# File   :   data_obect.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   There is no explicit interface implementation, no keyword interface in
#            the current Python version.
#            In order to "implement" iDataObject make your data object inherit 
#            from this class.
# -----------------------------------------------------------------------------------

class DataObject:
    """DataObject interface
    
    All methods must be implemented in inheriting class.
    """

    def does_exist(self, object_name: str) -> bool:
        """Check if the data object exists in the distant storage"""
        raise NotImplementedError("Not implemented!")

    def create(self, object_name: str, local_file_path: str) -> None:
        """Create the data object in the distant storage

        Args:
            object_name: str       Data object name
            local_file_path: str   Local path (if the objects is based on a file)

        Raises: 
            Exception: if the object already exists in distant storage
        """
        raise NotImplementedError("Not implemented!")

    def download(self, object_name: str) -> list:
        """Return a list of object to download from the distant storage

        Args:
            object_name: str       Data object name

        Returns: 
            A list that contain the bytes of the downloaded object

        Raises: 
            Exception the data object name does not exists
        
        """
        raise NotImplementedError("Not implemented!")

    def publish(self, object_name: str) -> str:
        """

        Args:
            object_name: str       Data object name (file.extension)
            local_file_path: str   Local path (path + file.extension)

        Returns:
            str public link
        
        Raises: 
            Exception the data object name does not exists
        """
        raise NotImplementedError("Not implemented!")

    def delete(self, object_name: str) -> None:
        """Delete the data object by its name

        Args:
            object_name: str       Data object name (file.extension)

        Raises: 
            Exception the data object name does not exists
        """
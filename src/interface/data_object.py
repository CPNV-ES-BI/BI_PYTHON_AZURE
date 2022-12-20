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

    def create(self, object_name: str, local_file_path: str) -> object:
        """Create the data object in the distant storage

        Args:
            object_name: str       Data object name (file.extension)
            local_file_path: str   Local path (path + file.extension)

        Returns:
            DataObject in the distant storage

        Raises: 
            Exception: if the object already exists in distant storage
        
        Notes: 
            If the local_file_path does not exists, it creates the data object anyway.
            It will upload an empty file with the object name as name file.
        """
        raise NotImplementedError("Not implemented!")

    def download(self, data_object_name: str, filepath: str) -> None:
        """Download the file from the distant data object through its name

        Args:
            object_name: str       Data object name (file.extension)
            local_file_path: str   Local path (path + file.extension)

        Raises: 
            Exception the data object name does not exists
        
        """
        raise NotImplementedError("Not implemented!")

    def publish(self, object_name: str, local_file_path: str) -> None:
        """Publish the file to the distant data object through its name

        Args:
            object_name: str       Data object name (file.extension)
            local_file_path: str   Local path (path + file.extension)

        Raises: 
            Exception the data object name does not exists
        
        """
        raise NotImplementedError("Not implemented!")


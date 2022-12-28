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

    def does_exist(self, object_path: str) -> bool:
        """Check if the data object exists in the distant storage"""
        raise NotImplementedError("Not implemented!")

    def create(self, object_path: str, local_file_path: str) -> None:
        """Create the data object in the distant storage

        Args:
            object_path: str       Path to the object in the distant storage
                                   Ex: `subdir1/subdir2/myfile.txt" 

            local_file_path: str   Local path (path + file.extension)

        Returns:
            DataObject in the distant storage

        Raises: 
            Exception: if the object already exists in distant storage
        
        Notes: 
            If the local_file_path does not exists, it creates the structure anyway.
        """
        raise NotImplementedError("Not implemented!")

    def download(self, object_path: str) -> str:
        """Download the file from the distant data object through its name

        Args:
            object_path: str       Data object name (file.extension)

        Returns: 
            Path to the downloaded object 

        Raises: 
            Exception the data object name does not exists
        
        """
        raise NotImplementedError("Not implemented!")

    def publish(self, object_path: str) -> None:
        """Set the data_object public

        Args:
            object_path: str       Data object name (file.extension)
            local_file_path: str   Local path (path + file.extension)

        Raises: 
            Exception the data object name does not exists
        
        """
        raise NotImplementedError("Not implemented!")

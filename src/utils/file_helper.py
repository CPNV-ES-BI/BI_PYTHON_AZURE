# -----------------------------------------------------------------------------------  
# File   :   file_helper.py
# Author :   Mélodie Ohan
# Version:   20-12-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------


import os
import re

class FileHelper:
    """ Provide methods to read, create files and directories. """

    def is_readable(self, path: str) -> bool:
        """Checks that the path is readable"""
        return os.access(path, os.R_OK)
    
    def is_valid_file_path(self, path: str) -> bool:
        """Check if the provided path has the correct format.

        Args: 
            path: str
                `path/to/file_name.extension`
                `/path/to/file_name.extension`
                allows file names such as file.tar.gz

        Returns:
            True if the file path is correct
        """
        regex = r"^(/?[\w.-]+)+/[\w.-]+\.[\w]{1,4}$"        
        return re.match(regex, path) is not None

    def _get_file_name(self, file_path: str) -> str:
        """
        Return the last element of a path

        Args:
            file_path: str      `subdir1/subdir2/myfile.txt" 

        """
        return file_path.rsplit("/", 1)[-1]


    def make_from_path(self, write_path: str, file_path: str, data) -> str:
        """ Create the folder tree of the file_path in the write_path

        Args: 
            write_path: str
                Where to create the directory with the provided file

            file_path: str
                Full path to the file
            
            data: ReadableBuffer
                file data
        
        Returns:
            The full path of the created file (from the write_path)
        """
        if not self.is_readable(write_path) and os.path.isdir(write_path):
            raise ValueError(f"Argument error: `{write_path}` does not exist")
        
        if not self.is_valid_file_path(file_path):
            raise ValueError(f"Argument error: cannot create `{file_path}` ")
        
        # Extract filename and filepath
        full_path: str = os.path.join(write_path, file_path)
        file_name = self._get_file_name(full_path)
        dir_name = full_path[:-len(file_name)]

        # Create any non existent sub directories in the path
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        # Create the file
        with open(full_path, "wb") as f: 
            f.write(data)
        
        return full_path

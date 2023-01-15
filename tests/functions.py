import uuid
import tempfile
import os
import shutil
import re

"""
The functions below are only intended to help in the realization of unit tests.
"""

def get_random_name() -> str:
    """
    Return a generated uuid in string format
    """
    return str(uuid.uuid4()) 

def is_file_name(file_path: str) -> bool:
    pattern = r'^[\w\-. ]+\.[A-Za-z]{2,}$'
    match = re.search(pattern, file_path)
    return bool(match)

def create_test_directory(file_name: str = None, data: bytes|str = None) -> None:
    """
    Create a tmp directory for tests.

    Returns:
        tmp directory str path

    Notes: 
        If the filename is set, it creates a file in the tmp directory.
        If the data are set, it writes the requested content in this file.
    
    """
    tmp_dir = tempfile.mkdtemp()
    if file_name and is_file_name(file_name):
        file_path = os.path.join(tmp_dir, file_name)
        if data is None:
            data = "Generated file from functions.create_test_directory()"
        with open(file_path, "w") as f: f.write(data)
    return tmp_dir

def delete_directory(path: str) -> None:
    """
    Delete recursively a directory with its content.

    Notes:
        Deletes only if the user has write and execute permission
        on the directory.
    """
    if os.access(path, os.W_OK) and os.access(path, os.X_OK):
        shutil.rmtree(path)

def merge_paths(path: str, other: str) -> str:
    """Join two paths"""
    return os.path.join(path, other)
import unittest
import os
import tempfile
import shutil
import os
import uuid

from blob.blob_helper import BlobHelper
from config.client import Client


class TestBlobHelper(unittest.TestCase):

    _blob_helper: BlobHelper
    _tmp_dir: str
    _file_path: str # file name + extension
    _object_path: str

    # Before all
    @classmethod
    def setUpClass(cls):
        cls._blob_helper = BlobHelper(Client.get_container_client())
        # Create and set tmp test directory
        cls._tmp_dir = tempfile.mkdtemp()
        # Create a file with a random name
        file_name = f"{str(uuid.uuid4())}.txt" 
        cls._file_path = os.path.join(cls._tmp_dir , file_name)
        with open(cls._file_path, "w") as f: f.write("~")
        # Define objet path
        cls._object_path = 'file.txt'
    
    # After all
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls._tmp_dir)

    # Before each
    def setUp(self):
        pass
    
    # After each 
    def tearDown(self):
        # TODO Delete created object?
        pass
    
    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given
        # refer to setUpClass
        
        # when
        # Refer to setUp() (where the object must be created)

        # then  
        self.assertEqual(self._blob_helper.does_exist(TestBlobHelper._object_path), True)

    
    # depends on test_does_exist_not_exists_success
    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUp (where the object is created)

        # when
        # then
        with self.assertRaises(Exception):
            self._blob_helper.create(
                TestBlobHelper._object_path, 
                TestBlobHelper._object_path)

    # Depends on does_exist_exists_case_success
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # refer to setUpClass
        object_path: str = f"{str(uuid.uuid4())}.txt" 
        local_path: str = '/impossible/path/afile.txt'

        # when
        self._blob_helper.create(object_path, local_path)

        # then
        self.assertEqual(self._blob_helper.does_exist(object_path), True)

    
    def test_does_exist_exists_case_success(self):
        # given 
        # refer to setUpClass
        # Generate an impossible random file
        blob_name: str = f"{str(uuid.uuid4())}.txt" 
        
        # when
        result: bool = self._blob_helper.does_exist(blob_name)
        
        # then
        self.assertEqual(result, False)

    def test_does_exist_not_exists_success(self):
        # given 
        # refer to setUpClass and setUp()
        
        # when
        result: bool = self._blob_helper.does_exist('existing_blob_name')
        
        # then
        self.assertEqual(result, False)

    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass

        # when
        file_path: str = self._blob_helper.download(TestBlobHelper._object_path)

        # then
        self.assertEqual(os.path.isfile(file_path), True)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass
        object_path: str = f"{str(uuid.uuid4())}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self._blob_helper.download(object_path)
    
        # Depends on download_object_nominal_case_downloaded
    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass

        # when
        # then
        pass
        

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass

        # when
        # then
        pass
  

if __name__ == '__main__':
    unittest.main()
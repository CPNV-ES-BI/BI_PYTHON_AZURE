import unittest
import os
import tempfile
import shutil
import uuid

from config.azure_client import AzureClient
from container.container_helper import ContainerHelper
from blob.blob_helper import BlobHelper

class TestContainerHelper(unittest.TestCase):

    # Attributes area
    # -----------------------------------------------------------------------    

    # instance attributes
    _container_helper: ContainerHelper 
    _container_name: str   

    # Class attributes
    _storage_client: AzureClient     
    _blob_name: str
    _blob_path: str 
    _local_file_path: str                

    # Test class methods area
    # -----------------------------------------------------------------------
  
    @classmethod
    def _create_test_directory(cls):
        """Create a tmp directory with a txt file"""
        cls._tmp_dir = tempfile.mkdtemp()
        file_name = f"{str(uuid.uuid4())}.txt" 
        cls._local_file_path = os.path.join(cls._tmp_dir, file_name)
        with open(cls._local_file_path, "w") as f: f.write("~")

    @classmethod
    def _delete_test_directory(cls):
        """Delete the created tmp directory with its content"""
        shutil.rmtree(cls._tmp_dir)
    
    @classmethod
    def _create_blob(cls, container_name: str):
        cls._blob_helper = BlobHelper(TestContainerHelper._storage_client, container_name)
        cls._blob_name = "TestContainerHelper/example.txt"
        cls._blob_helper.create(cls._blob_name, TestContainerHelper._local_file_path)
    
    @classmethod
    def _path_exist(cls, container_name: str,  obj_path: str) -> bool:
        path = os.path.join(cls._tmp_dir, container_name)
        path = os.path.join(path, obj_path)
        return os.path.exists(path)

    # SetUp and TearDown area
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        cls._storage_client = AzureClient()
        cls._create_test_directory()

    # After all
    @classmethod
    def tearDownClass(cls):
        cls._delete_test_directory()

    # Before each
    def setUp(self):
        # create a container with a blob
        self._container_name = f"{str(uuid.uuid4())}" 
        self._container_helper = ContainerHelper(TestContainerHelper._storage_client)
        self._container_helper.create(self._container_name)
        TestContainerHelper._create_blob(self._container_name)

    # After each 
    def tearDown(self):
        # Delete the container
        if self._container_helper.does_exist(self._container_name):
            self._container_helper.delete(self._container_name)

    # Tests area
    # -----------------------------------------------------------------------

    def test_does_exist_exists_case_success(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result: bool = self._container_helper.does_exist(self._container_name)
        
        # then
        self.assertEqual(result, True)

    def test_does_exist_not_exists_success(self):
        # given 
        # refer to and setUp()
        container_name = f"{str(uuid.uuid4())}"  

        # when
        result: bool = self._container_helper.does_exist(container_name)
        
        # then
        self.assertEqual(result, False)

    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given        
        # when
        # refer to setUp()
    
        # then  
        self.assertEqual(self._container_helper.does_exist(self._container_name), True)
    
    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(Exception):
            self._container_helper.create(self._container_name)

    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result = self._container_helper.download(self._container_name)

        # then
        # It checks the full path to the blob
        self.assertIsNotNone(result)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        container_name = f"{str(uuid.uuid4())}" 

        # when
        # then
        with self.assertRaises(Exception):
            self._container_helper.download(container_name)

    # depends on test_does_exist_not_exists_success
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUp()

        # when
        self._container_helper.delete(self._container_name)

        # then
        self.assertEqual(self._container_helper.does_exist(self._container_name), False)

    def test_delete_object_object_doesnt_exist_throw_exception(self):
        # given
        # refer to setUp()
        container_name = f"{str(uuid.uuid4())}"  

        # when
        # then
        with self.assertRaises(Exception):
            self._container_helper.delete(container_name)

if __name__ == '__main__':
    unittest.main()
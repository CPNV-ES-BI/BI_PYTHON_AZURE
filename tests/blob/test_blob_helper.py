import unittest
import os
import tempfile
import shutil
import uuid

from blob.blob_helper import BlobHelper
from config.storage_client import StorageClient
from container.container_helper import ContainerHelper


class TestBlobHelper(unittest.TestCase):

    _blob_helper: BlobHelper  
    _blob_name: str

    # start class attributes
    _local_file_path: str       
    _object_path: str
    _storage_client: StorageClient
    _tmp_dir: str
    _container_name: str
    _container_helper: str
    # end class attributes area

    # -----------------------------------------------------------------------
    # These methods create/delete the test environment 
    # and depend on the TestContainerHelper successes
    # Refer to:
    # - test_create_object_nominal_case_object_exists()
    # - test_delete_object_object_exists_object_deleted
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
    def _create_test_container(cls):
        """Create a container with a random name"""
        cls._container_name = f"{str(uuid.uuid4())}"
        cls._container_helper = ContainerHelper(cls._storage_client)
        cls._container_helper.create(cls._container_name)

    @classmethod
    def _delete_test_container(cls):
        """Delete the created tmp directory with its content"""
        cls._container_helper.delete(cls._container_name)
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        cls._object_path = 'file.txt'
        cls._storage_client = StorageClient()
        cls._create_test_directory()
        cls._create_test_container()
    
    # After all
    @classmethod
    def tearDownClass(cls):
        cls._delete_test_container()
        cls._delete_test_directory()

    # Before each
    def setUp(self):
        self._blob_helper = BlobHelper(TestBlobHelper._storage_client, TestBlobHelper._container_name)
        self._blob_name = "TestBlobHelper/example.txt"
        self._blob_helper.create(self._blob_name, TestBlobHelper._local_file_path)
    
    # After each 
    def tearDown(self):
        self._blob_helper.delete(self._blob_name)
    
    def test_does_exist_exists_case_success(self):
        # given         
        # refer to setUpClass and setUp()
                
        # when
        result: bool = self._blob_helper.does_exist(self._blob_name)
        
        # then
        self.assertEqual(result, True)

    def test_does_exist_not_exists_success(self):
        # given 
        # refer to setUpClass and setUp()
        blob_name: str =  f"{str(uuid.uuid4())}.txt" 

        # when
        result: bool = self._blob_helper.does_exist(blob_name)
        
        # then
        self.assertEqual(result, False)
        pass

    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given
        # when
        # refer to setUpClass and setUp()

        # then
        object_exist: bool = self._blob_helper.does_exist(self._blob_name)  
        self.assertEqual(object_exist, True)

    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(Exception):
            self._blob_helper.create(
                self._blob_name, 
                TestBlobHelper._local_file_path)
        
    # Depends on does_exist_exists_case_success
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{str(uuid.uuid4())}.txt" 
        local_path: str = f"does_not_exist{TestBlobHelper._local_file_path}"

        # when
        self._blob_helper.create(blob_name, local_path)

        # then
        self.assertEqual(self._blob_helper.does_exist(blob_name), True)
    
    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass and setUp()

        # when
        self._blob_helper.download(self._blob_name, TestBlobHelper._tmp_dir)

        # then
        result: bool = os.path.exists(TestBlobHelper._tmp_dir)
        self.assertEqual(result, True)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{str(uuid.uuid4())}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self._blob_helper.download(blob_name, TestBlobHelper._tmp_dir)
        

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{str(uuid.uuid4())}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self._blob_helper.publish(self._blob_name)

    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass and setUp()
        
        # when
        self._blob_helper.publish(self._blob_name)

        # then
        result: bool = self._blob_helper.is_public(self._blob_name)
        self.assertEqual(result, True)
        

if __name__ == '__main__':
    unittest.main()
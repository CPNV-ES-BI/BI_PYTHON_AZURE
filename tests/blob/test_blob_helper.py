import unittest

from tests.functions import get_random_name, create_test_directory, delete_directory, merge_paths
from blob.blob_helper import BlobHelper
from config.azure_client import AzureClient
from container.container_helper import ContainerHelper


class TestBlobHelper(unittest.TestCase):

    # Attributes area
    # -----------------------------------------------------------------------

    # instance attributes
    __blob_helper: BlobHelper  
    __blob_name: str

    # Class attributes
    __local_file_path: str     
    __storage_client: AzureClient
    __tmp_dir: str
    __container_name: str
    __container_helper: str

    
    # Test class methods area
    # -----------------------------------------------------------------------

    @classmethod
    def __create_test_container(cls):
        """Create a container with a random name"""
        cls.__container_name = get_random_name()
        cls.__container_helper = ContainerHelper(cls.__storage_client)
        cls.__container_helper.create(cls.__container_name)

    @classmethod
    def __delete_test_container(cls):
        """Delete the created tmp directory with its content"""
        cls.__container_helper.delete(cls.__container_name)

    # SetUp and TearDown area
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        cls.__storage_client = AzureClient()
        cls.__create_test_container()
        # Creates tests environnment
        file_name = f"{get_random_name()}.txt"
        cls.__tmp_dir = create_test_directory(file_name)
        cls.__local_file_path = merge_paths(cls.__tmp_dir, file_name)
    
    # After all
    @classmethod
    def tearDownClass(cls):
        cls.__delete_test_container()
        delete_directory(cls.__tmp_dir)

    # Before each
    def setUp(self):
        self.__blob_helper = BlobHelper(TestBlobHelper.__storage_client, TestBlobHelper.__container_name)
        self.__blob_name = "TestBlobHelper/example.txt"
        self.__blob_helper.create(self.__blob_name, TestBlobHelper.__local_file_path)
    
    # After each 
    def tearDown(self):
        if self.__blob_helper.does_exist(self.__blob_name):
            self.__blob_helper.delete(self.__blob_name)

    # Tests area
    # -----------------------------------------------------------------------

    def test_does_exist_exists_case_true(self):
        # given         
        # refer to setUpClass and setUp()
                
        # when
        result: bool = self.__blob_helper.does_exist(self.__blob_name)
        
        # then
        self.assertEqual(result, True)

    def test_does_exist_not_exists_false(self):
        # given 
        # refer to setUpClass and setUp()
        blob_name: str =  f"{get_random_name()}.txt" 

        # when
        result: bool = self.__blob_helper.does_exist(blob_name)
        
        # then
        self.assertEqual(result, False)
        pass

    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given
        # when
        # refer to setUpClass and setUp()

        # then
        object_exist: bool = self.__blob_helper.does_exist(self.__blob_name)  
        self.assertEqual(object_exist, True)

    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(Exception):
            self.__blob_helper.create(
                self.__blob_name, 
                TestBlobHelper.__local_file_path)
        
    # Depends on does_exist_exists_case_success
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{get_random_name()}.txt" 
        local_path: str = f"does_not_exist{TestBlobHelper.__local_file_path}"

        # when
        self.__blob_helper.create(blob_name, local_path)

        # then
        self.assertEqual(self.__blob_helper.does_exist(blob_name), True)
    
    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result = self.__blob_helper.download(self.__blob_name)

        # then
        self.assertIsNotNone(result)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{get_random_name()}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self.__blob_helper.download(blob_name)
    
    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass and setUp()
        
        # when
        result: str = self.__blob_helper.publish(self.__blob_name)

        # then
        self.assertIsNotNone(result)

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{get_random_name()}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self.__blob_helper.publish(self.__blob_name)
    
    # depends on test_does_exist_exists_case_success
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUpClass and setUp()
        
        # when
        self.__blob_helper.delete(self.__blob_name)

        # then
        self.assertEqual(self.__blob_helper.does_exist(self.__blob_name), False)

    def test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively(self):
        # given
        # refer to setUpClass and setUp()
   
        # when
        self.__blob_helper.delete(self.__blob_name)

        # then
        self.assertEqual(self.__blob_helper.does_exist(self.__blob_name), False)
    
    #depends on test_does_exist_not_exists_success
    def test_delete_object_object_doesnt_exist_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{get_random_name()}.txt" 

        # when
        # then
        with self.assertRaises(Exception):
            self.__blob_helper.delete(blob_name)

if __name__ == '__main__':
    unittest.main()

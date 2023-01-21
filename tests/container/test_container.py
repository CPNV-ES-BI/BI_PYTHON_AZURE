import unittest

from tests.functions import get_random_name, create_test_directory, delete_directory, merge_paths
from config.azure_client import AzureClient
from container.container import Container
from blob.blob import Blob


class TestContainer(unittest.TestCase):

    # Attributes area
    # -----------------------------------------------------------------------    

    # instance attributes
    __container: Container 
    __container_name: str   

    # Class attributes
    __storage_client: AzureClient     
    __blob_name: str
    __local_file_path: str                

    # Test class methods area
    # -----------------------------------------------------------------------
  
    @classmethod
    def __create_blob(cls, container_name: str):
        cls.__blob = Blob(TestContainer.__storage_client, container_name)
        cls.__blob_name = "TestContainer/example.txt"
        cls.__blob.create(cls.__blob_name, TestContainer.__local_file_path)
    
    # SetUp and TearDown area
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        cls.__storage_client = AzureClient()
        # Creates tests environnment
        file_name = f"{get_random_name()}.txt"
        cls.__tmp_dir = create_test_directory(file_name)
        cls.__local_file_path = merge_paths(cls.__tmp_dir, file_name)

    # After all
    @classmethod
    def tearDownClass(cls):
        delete_directory(cls.__tmp_dir)

    # Before each
    def setUp(self):
        # create a container with a blob
        self.__container_name = get_random_name() 
        self.__container = Container(TestContainer.__storage_client)
        self.__container.create(self.__container_name)
        TestContainer.__create_blob(self.__container_name)

    # After each 
    def tearDown(self):
        # Delete the container
        if self.__container.does_exist(self.__container_name):
            self.__container.delete(self.__container_name)

    # Tests area
    # -----------------------------------------------------------------------

    def test_does_exist_exists_case_true(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result: bool = self.__container.does_exist(self.__container_name)
        
        # then
        self.assertEqual(result, True)

    def test_does_exist_not_exists_false(self):
        # given 
        # refer to and setUp()
        container_name = get_random_name() 

        # when
        result: bool = self.__container.does_exist(container_name)
        
        # then
        self.assertEqual(result, False)

    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given        
        # when
        # refer to setUp()
    
        # then  
        self.assertEqual(self.__container.does_exist(self.__container_name), True)
    
    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(Exception):
            self.__container.create(self.__container_name)

    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result = self.__container.download(self.__container_name)

        # then
        # It checks the full path to the blob
        self.assertIsNotNone(result)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        container_name = get_random_name()

        # when
        # then
        with self.assertRaises(Exception):
            self.__container.download(container_name)

    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass and setUp()

        # when
        result: str = self.__container.publish(self.__container_name)

        # then
        # should return an url
        self.assertIsNotNone(result)

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        container_name: str = get_random_name()

        # when
        # then
        with self.assertRaises(Exception):
            self.__container.publish(self.__container_name)

    # depends on test_does_exist_not_exists_false
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUp()

        # when
        self.__container.delete(self.__container_name)

        # then
        self.assertEqual(self.__container.does_exist(self.__container_name), False)

    # depends on test_does_exist_not_exists_false
    def test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively(self):
        # given
        # refer to setUp()
        
        # when
        self.__container.delete(self.__container_name)

        # then
        # We assume that the delete method delete any blob contained in the container
        self.assertEqual(self.__container.does_exist(self.__container_name), False)

    def test_delete_object_object_doesnt_exist_throw_exception(self):
        # given
        # refer to setUp()
        container_name = get_random_name()

        # when
        # then
        with self.assertRaises(Exception):
            self.__container.delete(container_name)

if __name__ == '__main__':
    unittest.main()

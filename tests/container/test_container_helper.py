import unittest
import os
import tempfile
import shutil
import os
import uuid

from config.storage_client import StorageClient
from container.container_helper import ContainerHelper

class TestContainerHelper(unittest.TestCase):

    _storage_client: StorageClient      # class attribute
    _container_helper: ContainerHelper 
    _container_name: str                

    # Before all
    @classmethod
    def setUpClass(cls):
        cls._storage_client = StorageClient()
    
    # After all
    @classmethod
    def tearDownClass(cls):
        pass

    # Before each
    def setUp(self):
        self._container_helper = ContainerHelper(TestContainerHelper._storage_client)
        # Create a test container
        self._container_name = f"{str(uuid.uuid4())}"
        self._container_helper.create(self._container_name)
    
    # After each 
    def tearDown(self):
        # Delete a test container if it exists (for the delete case)
        if self._container_helper.does_exist(self._container_name):
            self._container_helper.delete(self._container_name)

    def test_does_exist_exists_case_success(self):
        # given
        
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
    
    # depends on test_does_exist_not_exists_success
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUp()

        # when
        self._container_helper.delete(self._container_name)

        # then
        self.assertEqual(self._container_helper.does_exist(self._container_name), False)


if __name__ == '__main__':
    unittest.main()
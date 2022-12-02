import unittest

from src.data_object import DataObject
from src.exceptions.data_object_already_exists import DataObjectAlreadyExists
from src.exceptions.data_object_does_not_exist import DataObjectDoesNotExist

class TestDataObject(unittest.TestCase):
    
    _data_object: DataObject
    _identifier: str = 'unique_identifier'
    _path: str = 'real/path/'

    # Before all
    @classmethod
    def setUpClass(cls):
        pass
    
    # After all
    @classmethod
    def tearDownClass(cls):
        pass
    
    # Before each
    def setUp(self):
        self._data_object = DataObject.create_object(self._identifier, self._path)
    
    # After each 
    def tearDown(self):
        # TODO Delete created object?
        pass
        # given
        # when
        # then
    
    def does_exist_exists_case_success(self):
        # given 
        # refer to class attributes
        
        # when
        result: bool = DataObject.does_exist(self._identifier)

        # then
        self.assertEqual(result, True)

    def does_exist_not_exists_success(self):
        # given 
        # refer to class attributes
        
        # when
        result: bool = DataObject.does_exist('non_existing_identifier')

        # then
        self.assertEqual(result, False)

    def create_object_nominal_case_object_exists(self):
        # given
        data_object: DataObject
        identifier: str = 'new_unique_identifier'
        path: str = 'new/path/'

        # when
        data_object = DataObject.create_object(identifier, path)

        # then
        self.assertEqual(DataObject.does_exist(identifier), True)

    def create_object_already_exists_throw_exception(self):
        # given 
        # refer to class attribute and setUp()

        # when
        # then
        with self.assertRaises(DataObjectAlreadyExists):
            DataObject.create_object(self._identifier)

    # Depends on does_exist_exists_case_success
    def create_object_path_not_exists_object_exists(self):
        # given
        # refer to class attribute
        path: str = 'not/existing/path/'
        identifier: str = 'another_unique_identifier'

        # when
        data_object: DataObject = DataObject.create_object(identifier, path)
    
        # then
        self.assertEqual(DataObject.does_exist(identifier), True)

    def download_object_nominal_case_downloaded(self):
        # given
        # refer to class attributes and setUp()

        # when
        data_object: DataObject = DataObject.download_object(self._identifier)

        # then
        self.assertIsNotNone(data_object)

    def download_object_not_exists_throw_exception(self):
        # given
        identifier: str = 'not_existing_identifier'

        # when
        # then
        with self.assertRaises(DataObjectDoesNotExist):
            DataObject.download_object(identifier)

    # Depends on download_object_nominal_case_downloaded
    def publish_object_nominal_case_object_published(self):
        # given
        # refer to class attribute and setUp()

        # when
        DataObject.publish(self._identifier)

        # then
        self.assertIsNotNone(DataObject.download_object(self._identifier))

    def publish_object_objecT_not_found_throw_exception(self):
        # given
        identifier: str = 'not_existing_identifier'

        # when
        # then
        with self.assertRaises(DataObjectDoesNotExist):
            DataObject.publish_object(identifier)
  
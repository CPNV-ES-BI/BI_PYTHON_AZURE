import unittest

from blob.blob_helper import BlobHelper

class TestBlobHelper(unittest.TestCase):

    # Before all
    @classmethod
    def setUpClass(cls):
        # TODO create a temp directory and a temp file and set it to _file_path
        # TODO set the object name (temp file name + extension)
        # TODO init blob_helper
        pass
    
    # After all
    @classmethod
    def tearDownClass(cls):
        # TODO delete created temp directory
        pass
    
    # Before each
    def setUp(self):
        pass
    
    # After each 
    def tearDown(self):
        # TODO Delete created object?
        pass

    def test_does_exist_exists_case_success(self):
        # given 
        # refer to setUpClass
        
        # when

        # then
        pass

    def test_does_exist_not_exists_success(self):
        # given 
        # refer to setUpClass
        
        # when

        # then
        pass
    
    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given
        # refer to setUpClass

        # when

        # then  
        pass
    
        # depends on test_does_exist_not_exists_success

    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass

        # when
        # then
        pass

    # Depends on does_exist_exists_case_success
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # refer to setUpClass

        # when

        # then
        pass
    
    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass

        # when
        
        # then
        pass

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass
        object_name: str = 'a-random-name'
        file_path: str = 'temp/downloaded/file/path/file.ext'

        # when
        # then
        pass
    
        # Depends on download_object_nominal_case_downloaded
    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass

        # when
        # then
        pass
        

    def test_publish_object_objecT_not_found_throw_exception(self):
        # given
        # refer to setUpClass

        # when
        # then
        pass
  

if __name__ == '__main__':
    unittest.main()
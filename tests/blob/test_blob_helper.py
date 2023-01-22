# -----------------------------------------------------------------------------------
# File   :   test_blob_helper.py
# Author :   Mélodie Ohan
# Version:   22-01-2023 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import unittest
import os
import uuid
import re
import inspect

from config.azure_client import AzureClient
from blob.blob_helper import BlobHelper
from container.container_helper import ContainerHelper
from blob.errors.blob_already_exists_error import BlobAlreadyExistsError
from blob.errors.blob_does_not_exist_error import BlobDoesNotExistError


class TestBlobHelper(unittest.TestCase):
    # Attributes area
    # -----------------------------------------------------------------------

    # Class attributes constants
    # Directory name where a test file is contained
    __TEST_DIR_NAME: str = "files"
    __TEST_FILE_NAME: str = "test_blob_file.txt"

    # class attributes
    __storage_client: AzureClient
    __test_file_path: str
    __container_name: str
    __container_helper: ContainerHelper

    # instance attributes
    __blob_name: str
    __blob_helper: BlobHelper

    # Required methods for test execution
    # -----------------------------------------------------------------------
    @staticmethod
    def __get_prefixed_random_name(prefix: str = "") -> str:
        """Return a unique name with 'prefix-' and 10 uuid char"""
        # Use the first 5 characters and the last 5 characters of the UUID to limit collision in names
        uuid_str = str(uuid.uuid4()).replace("-", "")
        return f"{prefix}-{uuid_str[:5] + uuid_str[-5:]}"

    @staticmethod
    def __get_test_file_path() -> str:
        """Get the existing test file path."""
        # get the current directory
        test_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # complete the path to the test file
        test_dir = os.path.join(test_dir, TestBlobHelper.__TEST_DIR_NAME)
        return os.path.join(test_dir, TestBlobHelper.__TEST_FILE_NAME)

    @staticmethod
    def __get_test_file_bytes(file_path: str) -> bytes:
        """Open the provided file in binary mode and return it"""
        with open(file_path, 'rb') as f:
            data = f.read()
        return data

    @staticmethod
    def __is_azure_blob_url(url: str, container_name: str, blob_name: str):
        """Check if the url is a standard blob url
        The url must look like:
        https://username.blob.core.windows.net/{container_name}/{_blob_name}
        """
        pattern: str = f"^(https://)(.+)(blob.core.windows.net/)({container_name})/({blob_name})"
        return True if re.search(pattern, url) else False

    # SetUp and TearDown area
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        # Set the test file path
        cls.__test_file_path = TestBlobHelper.__get_test_file_path()
        # Init the storage client and the container
        cls.__storage_client = AzureClient()
        cls.__container_helper = ContainerHelper(cls.__storage_client)
        # Create the container
        cls.__container_name = TestBlobHelper.__get_prefixed_random_name("container")
        cls.__container_helper.create(cls.__container_name)
        # Set container access policy
        cls.__container_helper.set_container_public_read_access(cls.__container_name)

    # After all
    @classmethod
    def tearDownClass(cls):
        if cls.__container_helper.does_exist(cls.__container_name):
            cls.__container_helper.delete(cls.__container_name)

    # Before each
    def setUp(self):
        self.__blob_name = f"{TestBlobHelper.__get_prefixed_random_name('blob')}.txt"
        self.__blob_helper = BlobHelper(TestBlobHelper.__storage_client, TestBlobHelper.__container_name)
        self.__blob_helper.create(self.__blob_name, TestBlobHelper.__test_file_path)

    # After each
    def tearDown(self):
        if self.__blob_helper.does_exist(self.__blob_name):
            self.__blob_helper.delete(self.__blob_name, False)

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
        blob_name: str = f"{TestBlobHelper.__get_prefixed_random_name('blob')}.txt"

        # when
        result: bool = self.__blob_helper.does_exist(blob_name)

        # then
        self.assertEqual(result, False)

    # depends on test_does_exist_exists_case_true
    def test_create_object_nominal_case_object_exists(self):
        # given
        # when
        # refer to setUpClass and setUp()

        # then
        self.assertEqual(self.__blob_helper.does_exist(self.__blob_name), True)

    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(BlobAlreadyExistsError):
            self.__blob_helper.create(self.__blob_name, TestBlobHelper.__test_file_path)

    # Depends on test_does_exist_exists_case_true
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{TestBlobHelper.__get_prefixed_random_name('empty_path_blob')}.txt"
        local_path: str = "./any/empty/path/"

        # when
        self.__blob_helper.create(blob_name, local_path)

        # then
        self.assertEqual(self.__blob_helper.does_exist(blob_name), True)

    def test_download_object_nominal_case_downloaded(self):
        # given
        # refer to setUpClass and setUp()
        uploaded_file_bytes: bytes = self.__get_test_file_bytes(TestBlobHelper.__get_test_file_path())

        # when
        result = self.__blob_helper.download(self.__blob_name)

        # then
        self.assertEqual(result, uploaded_file_bytes)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{TestBlobHelper.__get_prefixed_random_name('blob')}.txt"

        # when
        # then
        with self.assertRaises(BlobDoesNotExistError):
            self.__blob_helper.download(blob_name)

    def test_publish_object_nominal_case_object_published(self):
        # given
        # refer to setUpClass and setUp()

        # when
        blob_url: str = self.__blob_helper.publish(self.__blob_name)

        # then
        is_azure_blob_url: str = TestBlobHelper.__is_azure_blob_url(blob_url,
                                                                    TestBlobHelper.__container_name,
                                                                    self.__blob_name)
        self.assertEqual(is_azure_blob_url, True)

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{TestBlobHelper.__get_prefixed_random_name('blob')}.txt"

        # when
        # then
        with self.assertRaises(BlobDoesNotExistError):
            self.__blob_helper.publish(blob_name)

    # depends on test_does_exist_not_exists_false
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUpClass and setUp()

        # when
        self.__blob_helper.delete(self.__blob_name, recursive=False)

        # then
        self.assertEqual(self.__blob_helper.does_exist(self.__blob_name), False)

    # test_does_exist_not_exists_false
    def test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively(self):
        # given
        # refer to setUpClass and setUp()
        # Creates blob in "sub-directories"
        main_dir: str = '/a_dir'
        blob_name: str = f"{main_dir}/another_one/{self.__blob_name}"
        self.__blob_helper.create(blob_name, TestBlobHelper.__test_file_path)

        # when
        self.__blob_helper.delete(main_dir)

        # then
        self.assertEqual(self.__blob_helper.does_exist(blob_name), False)

    def test_delete_object_object_doesnt_exist_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        blob_name: str = f"{TestBlobHelper.__get_prefixed_random_name('blob')}.txt"

        # when
        # then
        with self.assertRaises(BlobDoesNotExistError):
            self.__blob_helper.delete(blob_name, False)


if __name__ == '__main__':
    unittest.main()

import unittest
import uuid

from config.azure_client import AzureClient
from container.container import Container
from container.errors.container_already_exists_error import ContainerAlreadyExistsError
from container.errors.container_does_not_exist_error import ContainerDoesNotExistError
from container.errors.container_forbidden_operation_error import ContainerForbiddenOperationError


class TestContainer(unittest.TestCase):

    # Attributes area
    # -----------------------------------------------------------------------    
    # class attributes
    __storage_client: AzureClient

    # instance attributes
    __container: Container
    __container_name: str

    # Required methods for test execution
    # -----------------------------------------------------------------------
    @staticmethod
    def get_random_container_name() -> str:
        """ Return a unique name with 'container-' and 10 uuid char"""
        # Use the first 15 characters and the last 15 characters of the UUID to limit collision in names
        uuid_str = str(uuid.uuid4()).replace("-", "")
        return f"container-{uuid_str[:5] + uuid_str[-5:]}"

    # SetUp and TearDown area
    # -----------------------------------------------------------------------

    # Before all
    @classmethod
    def setUpClass(cls):
        # Will be defined for every container class
        cls.__storage_client = AzureClient()

    # After all
    @classmethod
    def tearDownClass(cls):
        # AzureClient and Container instance are properly collected by the GC
        pass

    # Before each
    def setUp(self):
        storage_client = AzureClient()
        self.__container_name = TestContainer.get_random_container_name()
        self.__container = Container(storage_client)
        self.__container.create(self.__container_name)

    # After each 
    def tearDown(self):
        # Delete the container
        if self.__container.does_exist(self.__container_name):
            self.__container.delete(self.__container_name)

    # Tests area
    # -----------------------------------------------------------------------

    def test_does_exist_exists_case_true(self):
        # given
        # refer to setUpClass and setUp() and setUpClass()

        # when
        result: bool = self.__container.does_exist(self.__container_name)

        # then
        self.assertEqual(result, True)

    def test_does_exist_not_exists_false(self):
        # given
        # refer to setUpClass and setUp() and setUpClass()
        container_name = TestContainer.get_random_container_name()
        # when
        result: bool = self.__container.does_exist(container_name)

        # then
        self.assertEqual(result, False)

    # depends on test_does_exist_exists_case_success
    def test_create_object_nominal_case_object_exists(self):
        # given
        # when
        # refer to setUp() and setUpClass()

        # then
        self.assertEqual(self.__container.does_exist(self.__container_name), True)

    def test_create_object_already_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(ContainerAlreadyExistsError):
            self.__container.create(self.__container_name)

    # Depends on test_does_exist_exists_case_success
    # There is no path verification, containers creation do not depend on it.
    def test_create_object_path_not_exists_object_exists(self):
        # given
        # when
        # refer to setUp() and setUpClass()

        # then
        self.assertEqual(self.__container.does_exist(self.__container_name), True)

    # There is no path verification, containers creation do not depend on it.
    def test_create_object_path_is_not_none_object_throw_exception(self):
        # given
        # when
        # refer to setUp() and setUpClass()
        path: str = "any/path"

        # then
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.create(self.__container_name, path)

    def test_download_object_nominal_case_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when

        # then
        # It checks the full path to the blob
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.download(self.__container_name)

    def test_download_object_not_exists_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        container_name = TestContainer.get_random_container_name()

        # when
        # then
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.download(container_name)

    def test_publish_object_nominal_case_throw_exception(self):
        # given
        # refer to setUpClass and setUp()

        # when
        # then
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.publish(self.__container_name)

    def test_publish_object_object_not_found_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        container_name = TestContainer.get_random_container_name()

        # when
        # then
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.publish(container_name)

    # depends on test_does_exist_exists_case_success
    def test_delete_object_object_exists_object_deleted(self):
        # given
        # refer to setUpClass and setUp()

        # when
        self.__container.delete(self.__container_name)

        # then
        self.assertEqual(self.__container.does_exist(self.__container_name), False)

    # depends on test_does_exist_not_exists_false
    def test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively(self):
        # given
        # refer to setUpClass and setUp()

        # when
        self.__container.delete(self.__container_name)

        # then
        self.assertEqual(self.__container.does_exist(self.__container_name), False)

    def test_delete_object_object_not_recursive_deletion_throw_exception(self):
        # given
        # refer to setUpClass and setUp()
        recursive: bool = False

        # when
        # then
        with self.assertRaises(ContainerForbiddenOperationError):
            self.__container.delete(self.__container_name, recursive)

    def test_delete_object_object_doesnt_exist_throw_exception(self):
        # given
        # refer to setUp()
        container_name = TestContainer.get_random_container_name()

        # when
        # then
        with self.assertRaises(ContainerDoesNotExistError):
            self.__container.delete(container_name)


if __name__ == '__main__':
    unittest.main()

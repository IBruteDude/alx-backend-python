#!/usr/bin/env python3
""" Module for testing the utils module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class, param
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testing class for 'access_nested_map' function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ unit test for 'access_nested_map' util function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, error_key):
        """ unit test for 'access_nested_map' util function error handling
        """
        with self.assertRaises(KeyError) as rcm:
            access_nested_map(nested_map, path)
        self.assertEqual(rcm.exception.args[0], error_key)


class TestGetJson(unittest.TestCase):
    """ Testing class for 'get_json' function
    """
    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, *args, **kwargs):
        """ mocked unit test for 'get_json' util function
        """
        test_url = kwargs.get('test_url')
        test_payload = kwargs.get('test_payload')
        mock_get = args[-1]

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        payload = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertDictEqual(payload, test_payload)


class TestMemoize(unittest.TestCase):
    """ Testing class for 'memoize' decorator
    """
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, a_method_mock: Mock):
        """ mocked unit test for 'memoize' decorator
        """
        a_method_mock.return_value = 40
        test_obj = TestMemoize.TestClass()
        self.assertEqual(test_obj.a_property, 40)
        test_obj.a_property
        a_method_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()

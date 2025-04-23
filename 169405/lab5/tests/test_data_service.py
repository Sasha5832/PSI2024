import unittest
from unittest.mock import Mock
from lab5.src.data_service import DataService


class TestDataService(unittest.TestCase):
    def setUp(self):
        self.api_mock = Mock
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_values(self):
        self.api_mock.get_data.side_effect = [{'name': 'Jan'}, {'name': 'Anna'}]
        result = self.service.fetch_user_data(123)
        self.assertEqual(result, {'name': 'Jan'})
        result2 = self.service.fetch_user_data(56234)
        self.assertEqual(result2, {'name': 'Anna'})



    def tearDown(self):
        pass
import os
from unittest import TestCase
from odoocrm.client import Client


class OdooCRMTestCases(TestCase):
    def setUp(self):
        self.url = os.environ.get('url')
        self.database = os.environ.get('database')
        self.username = os.environ.get('username')
        self.password = os.environ.get('password')
        self.client = Client(self.url, self.database, self.username, self.password)

    def test_search_partner(self):
        response = self.client.search_partner([[['customer', '=', True]]])
        self.assertIsInstance(response, list)

    def test_read_partner(self):
        data = self.client.search_partner([[['customer', '=', True]]], {'limit': 1})
        response = self.client.read_partner(data)
        self.assertIsInstance(response, list)

    def test_list_fields_partner(self):
        response = self.client.list_fields_partner()
        self.assertIsInstance(response, dict)

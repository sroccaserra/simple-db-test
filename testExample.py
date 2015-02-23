# coding=utf-8
import unittest

from simpleDbTest import SimpleDbTestCase

class TestShowTable(SimpleDbTestCase):
    def test(self):
        tables = self.get_request_result_list("show tables;", "information_schema")
        self.assertNotEqual(0, len(tables))

if __name__ == '__main__':
    unittest.main()

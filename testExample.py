# coding=utf-8
import unittest

from simpleDbTest import SimpleDbTestCase

class TestShowTable(SimpleDbTestCase):
    def test(self):
        request = """
        select *
        from CHARACTER_SETS
        where CHARACTER_SET_NAME = 'utf8';
        """

        character_set = self.get_request_result(request, "information_schema")

        character_set_name = character_set[0]
        description = character_set[2]
        maxlen = character_set[3]

        self.assertEqual('utf8', character_set_name)
        self.assertEqual('UTF-8 Unicode', description)
        self.assertEqual(3, maxlen)

if __name__ == '__main__':
    unittest.main()

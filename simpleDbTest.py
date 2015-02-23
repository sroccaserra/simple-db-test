# coding=utf-8
import os

from unittest import TestCase
from ConfigParser import ConfigParser
import MySQLdb

class SimpleDbTestCase(TestCase):
    def __get_config(self):
        config = ConfigParser()
        confFile = os.environ['SIMPLE_TEST_CFG'] if 'SIMPLE_TEST_CFG' in os.environ else 'cfg/simpleDbTest.cfg'
        config.read([confFile, 'cfg/private.cfg'])
        return config

    def __get_connection(self, database):
        config_section = database
        config = self.__get_config()

        mysql_host = config.get(config_section, 'mysql_host')
        mysql_port = config.getint(config_section, 'mysql_port')
        mysql_user = config.get(config_section, 'mysql_user')
        mysql_password = config.get(config_section, 'mysql_password')

        connection = MySQLdb.connect(mysql_host, mysql_user, mysql_password, database, mysql_port)
        connection.set_character_set('utf8')
        connection.autocommit(True)
        return connection

    def get_request_result(self, requete, database):
        connection = self.__get_connection(database)
        cursor = connection.cursor()
        try:
            cursor.execute(requete)
            return cursor.fetchone()[0]
        except TypeError:
            return None
        finally:
            cursor.close()
            connection.close()

    def get_request_result_list(self, requete, database):
        connection = self.__get_connection(database)
        cursor = connection.cursor()
        try:
            cursor.execute(requete)
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

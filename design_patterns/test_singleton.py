import unittest

from design_patterns.singleton import ServerConnection


class TestServerConnection(unittest.TestCase):

    def test_server_connection_singleton(self):
        first_connection = ServerConnection()
        second_connection = ServerConnection()

        self.assertIs(first_connection, second_connection)

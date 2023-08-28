import unittest
from unittest.mock import MagicMock, patch

from calculator.calculator import Client, Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        client = Client()
        # client.send_data_to_server = MagicMock(return_value=None)
        self.calculator = Calculator(client)

    # @patch('calculator.calculator.Client.send_data_to_server', return_value=None)
    def test_sum(self
                 # , send_data_to_server
                 ):
        self.assertEquals(
            self.calculator.sum(1, 2),
            3
        )

    def tearDown(self) -> None:
        self.calculator.client.close_connection()

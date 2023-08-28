import unittest
from unittest.mock import MagicMock

import pytest

from user_repository.user_repository import Database, User, UserRepository


@pytest.fixture
def salaries():
    return [10000, 3000, 30000]


@pytest.fixture
def user_repository(salaries):
    database = Database()
    database.get_all_users = MagicMock(return_value=[
        User(1, 'alex', salaries[0]),
        User(2, 'emma', salaries[1]),
        User(3, 'ali', salaries[2])
    ])
    return UserRepository(database)


class TestUserRepository(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixtures(self, user_repository, salaries):
        self.user_repository = user_repository
        self.salaries = salaries

    def test_get_average_salary(self):
        self.assertEquals(
            self.user_repository.get_average_salary(),
            sum(self.salaries) / len(self.salaries)
        )

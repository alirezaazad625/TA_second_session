class User:
    def __init__(self, id: int, name: str, salary: int):
        self.id = id
        self.name = name
        self.salary = salary


class Database:
    def get_all_users(self) -> list[User]:
        raise NotImplementedError


class UserRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_average_salary(self) -> float:
        users = self.database.get_all_users()
        salaries = [user.salary for user in users]
        return sum(salaries) / len(salaries)

import abc


class DBConnection:
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def close_connection(self):
        pass


class PostgresSQLConnection(DBConnection):
    def connect(self):
        print("connect to postgres")

    def close_connection(self):
        print("connect to postgres")


class MySQLConnection(DBConnection):
    def connect(self):
        print("connect to mysql")

    def close_connection(self):
        print("connect to mysql")


class SqliteConnection(DBConnection):
    def connect(self):
        print("connect to sqlite")

    def close_connection(self):
        print("connect to sqlite")


class DBFactory:
    @staticmethod
    def create(db: str) -> DBConnection:
        match db:
            case 'postgres':
                return PostgresSQLConnection()
            case 'mysql':
                return MySQLConnection()
            case 'sqlite':
                return SqliteConnection()
            case _:
                raise NotImplementedError()
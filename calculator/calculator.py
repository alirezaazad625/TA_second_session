class Client:
    def send_data_to_server(self, **kwargs):
        raise NotImplementedError()

    def close_connection(self):
        pass


class Calculator:

    def __init__(self, client: Client):
        self.client = client

    def sum(self, first: int, second: int) -> int:
        result = first + second

        self.client.send_data_to_server(first=first, second=second, result=result)

        return result

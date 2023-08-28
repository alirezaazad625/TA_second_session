class ServerConnection(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ServerConnection, cls).__new__(cls)
        return cls._instance

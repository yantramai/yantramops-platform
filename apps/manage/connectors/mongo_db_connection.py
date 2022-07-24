from random import randint

from apps.core.base.base_connection_processor import InformalConnectorInterface
from pymongo import MongoClient


class MongoDBConnection(InformalConnectorInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def get_db_handle(self, host, port, username, password, db_name):
        # create an instance of MongoClient()
        client = MongoClient(
            host=host + ":" + str(port),
            serverSelectionTimeoutMS=3000,  # 3 second timeout
            username=username,
            password=password
        )
        return client

    def connect(self, auth: dict) -> object:
        client = self.get_db_handle(host="localhost", port=27017, username="root", password="12345",
                                                   db_name="yantram1")
        return client


import mongoengine

from projects.core.base.abstract_connection_processor import InformalConnectorInterface


class ApacheStatusCodeProcessor(InformalConnectorInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def connect(self, auth: dict) -> object:
        auth = {}
        host = auth.get("host")
        port = auth.get("port")
        username = auth.get("username")
        password = auth.get("password")
        db_name = auth.get("db_name")
        """Extract text from the currently loaded file."""
        connection: object = mongoengine.connect(db=db_name, host=host, username=username, password=password)
        return connection

    def process_data(self):
        connection = self.get_db_handle(db_name="sample_medicines", port=27017, host="localhost",
                                        username="admin",
                                        password="rootroot")

        # First define the database name
        # dbname = my_client['sample_medicines']

        # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
        # create connection
        collection_name = connection["sample_medicines"]

        # let's create two documents
        medicine_1 = {
            "medicine_id": "RR000123456",
            "common_name": "Paracetamol",
            "scientific_name": "",
            "available": "Y",
            "category": "fever"
        }
        medicine_2 = {
            "medicine_id": "RR000342522",
            "common_name": "Metformin",
            "scientific_name": "",
            "available": "Y",
            "category": "type 2 diabetes"
        }
        print(collection_name.distinct("medicine_id"))
        # Insert the documents
        collection_name.insert_many([medicine_1, medicine_2])
        # Check the count
        count = collection_name.count()
        print(count)

        # Read the documents
        med_details = collection_name.find({})
        # Print on the terminal
        for r in med_details:
            print(r["common_name"])
        # Update one document
        update_data = collection_name.update_one({'medicine_id': 'RR000123456'},
                                                 {'$set': {'common_name': 'Paracetamol 500'}})

        # Delete one document
        delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})

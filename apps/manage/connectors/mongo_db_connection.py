from random import randint

from apps.core.base.base_connection_processor import InformalConnectorInterface
from pymongo import MongoClient


class MongoDBConnection(InformalConnectorInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def get_db_handle(self, host, port, username, password, db_name):
        # host variables for MongoDB
        DOMAIN = 'localhost'
        PORT = 27017

        # create an instance of MongoClient()
        client = MongoClient(
            host=DOMAIN + ":" + str(PORT),
            serverSelectionTimeoutMS=3000,  # 3 second timeout
            username="root",
            password="12345"
        )
        return client

    def connect(self, auth: dict) -> object:
        client = self.get_db_handle(host="host", port=123, username="username", password="password",
                                                db_name="db_name")
        return client

# def connect(self, auth: dict) -> object:
    #     db_handle, client = self.get_db_handle(host=host, port=port, username=username, password=password,
    #                                                 db_name=db_name)
    #     # def process_data(self):
    #     db_handle = client["yantram1"]
    #
    #     names = ['Kitchen', 'Animal', 'State', 'Tastey', 'Big', 'City', 'Fish', 'Pizza', 'Goat', 'Salty', 'Sandwich',
    #              'Lazy', 'Fun']
    #     company_type = ['LLC', 'Inc', 'Company', 'Corporation']
    #     company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar',
    #                        'Vegetarian']
    #     for x in range(1, 501):
    #         business = {
    #             'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' +
    #                     company_type[randint(0, (len(company_type) - 1))],
    #             'rating': randint(1, 5),
    #             'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))]
    #         }
    #         # Step 3: Insert business object directly into MongoDB via insert_one
    #         print('************************************')
    #         print(db_handle)
    #         result = db_handle.reviews.insert_one(business)
    #         print('************************************')
    #         # Step 4: Print to the console the ObjectID of the new document
    #         print('Created {0} of 500 as {1}'.format(x, result.inserted_id))
    #     # Step 5: Tell us that you are done
    #     print('finished creating 500 business reviews')
    #     #     # def auth = db_name="sample_medicines", port=27017, host="localhost",
    #     #     #                                 username="admin",
    #     #     #                                 password="rootroot"
    #     #     auth = {}
    #     #     connection = self.connect(auth)
    #     #
    #     #     # First define the database name
    #     #     # dbname = my_client['sample_medicines']
    #     #
    #     #     # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
    #     #     # create connection
    #     #     collection_name = connection["sample_medicines"]
    #     #
    #     #     # let's create two documents
    #     #     medicine_1 = {
    #     #         "medicine_id": "RR000123456",
    #     #         "common_name": "Paracetamol",
    #     #         "scientific_name": "",
    #     #         "available": "Y",
    #     #         "category": "fever"
    #     #     }
    #     #     medicine_2 = {
    #     #         "medicine_id": "RR000342522",
    #     #         "common_name": "Metformin",
    #     #         "scientific_name": "",
    #     #         "available": "Y",
    #     #         "category": "type 2 diabetes"
    #     #     }
    #     #     print(collection_name.distinct("medicine_id"))
    #     #     # Insert the documents
    #     #     collection_name.insert_many([medicine_1, medicine_2])
    #     #     # Check the count
    #     #     count = collection_name.count()
    #     #     print(count)
    #     #
    #     #     # Read the documents
    #     #     med_details = collection_name.find({})
    #     #     # Print on the terminal
    #     #     for r in med_details:
    #     #         print(r["common_name"])
    #     #     # Update one document
    #     #     update_data = collection_name.update_one({'medicine_id': 'RR000123456'},
    #     #                                              {'$set': {'common_name': 'Paracetamol 500'}})
    #     #
    #     #     # Delete one document
    #     #     delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})

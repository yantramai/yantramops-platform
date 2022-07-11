from pymongo import MongoClient
import mongoengine



def get_db_handle(db_name, host, port, username, password):

    mongoengine.connect(db=db_name, host=host, username=username, password=password)
    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                         )
    db_handle = client['sample_medicines']
    return db_handle, client


from django.conf import settings

dbname,my_client = get_db_handle(db_name="sample_medicines",port=27017,host="localhost",username="admin",password="rootroot")
# dbname,my_client = get_db_handle(db_name="sample_medicines",port=27017,host="localhost",username="YWRtaW4=",password="cm9vdHJvb3Q=")

# First define the database name
# dbname = my_client['sample_medicines']


# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["sample_medicines"]

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
update_data = collection_name.update_one({'medicine_id': 'RR000123456'}, {'$set': {'common_name': 'Paracetamol 500'}})

# Delete one document
delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})

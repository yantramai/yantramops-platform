import logging

from prometheus_api_client import PrometheusConnect

from apps.core.base.base_common import Base
from apps.core.base.mongo_db_base import MongoDBBase
from apps.manage.connectors.mongo_db_connection import MongoDBConnection

"""
ASGI config for app_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""


class MongoDBUtils(MongoDBBase):

    def __init__(self):
        super().__init__()
        self._LOGGER.debug("In Base code")

    def save_helm_chart(self, file):
        mydb = self.client["yantram1"]
        deployments = mydb["deployments"]
        deployments = mydb["terraform_configuration"]
        deployments = mydb["helm_chart_values"]
        for x in deployments.find():
            self._LOGGER.debug("***************************************************************")
            self._LOGGER.debug("helm_chart_values downloaded %s", x)
            self._LOGGER.debug("***************************************************************")

        # projects = Project.objects.all()
        # return HttpResponse(results)
        context = {"projects": []}

    def process_data(self):
        mydb = self.client["yantram1"]
        #     # Read the documents
        #     med_details = collection_name.find({})
        #     # Print on the terminal
        #     for r in med_details:
        #         print(r["common_name"])
        #     # Update one document
        #     update_data = collection_name.update_one({'medicine_id': 'RR000123456'},
        #                                              {'$set': {'common_name': 'Paracetamol 500'}})
        #
        #     # Delete one document
        #     delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})

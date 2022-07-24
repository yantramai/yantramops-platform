import logging

from prometheus_api_client import PrometheusConnect

from apps.core.base.base_common import Base
from apps.manage.connectors.mongo_db_connection import MongoDBConnection

"""
ASGI config for app_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""


class MongoDBBase(Base):
    client = MongoDBConnection().get_db_handle(host="localhost", port=27017, username="root", password="12345",db_name="yantram1")
    mydb = client["yantram1"]

    def __init__(self):
        self._LOGGER.debug("In Base code")
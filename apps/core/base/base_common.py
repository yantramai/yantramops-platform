import logging

from prometheus_api_client import PrometheusConnect

"""
ASGI config for app_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""


class Base:
    logging.basicConfig(filename="base.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    _LOGGER = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    _LOGGER.setLevel(logging.DEBUG)

    def __init__(self):
        self._LOGGER.debug("In Base code")
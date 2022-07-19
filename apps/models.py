from django.db import models

from django.db import models
from django_jsonform.models.fields import JSONField
from django_jsonforms.forms import JSONSchemaField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")


class ShoppingList(models.Model):
    ITEMS_SCHEMA = {
        'type': 'array', # a list which will contain the items
        'items': {
            'type': 'string' # items in the array are strings
        }
    }
    ITEMS_SCHEMA1 = {
        'type': 'list',
        'items': {
            'type': 'dict',
            'keys': {
                'label': {
                    'type': 'string'
                },
                'link': {
                    'type': 'string'
                },
                'new_tab': {
                    'type': 'boolean',
                    'title': 'Open in new tab'
                }
            }
        }
    }

    items = JSONField(schema=ITEMS_SCHEMA1)
    date_created = models.DateTimeField(auto_now_add=True)
from django.db import models

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

from stream_django import activity


class Tweet(activity.Activity, models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)



class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends', on_delete=models.CASCADE)
    target = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target')

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

    # items = JSONField(schema=ITEMS_SCHEMA1)
    date_created = models.DateTimeField(auto_now_add=True)
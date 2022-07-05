from django.db import models

# Create your models here.

from django.db import models


class DeploymentConfig(models.Model):
    kube_context_yaml = models.TextField()
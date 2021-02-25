from django.db import models

import apps.acl.utils as utils
from apps.acl.mixin import RenderMixin

CSV_STRING_LENGTH = 300  # character limit for comma separated values
LINE_LENGTH = 80  # character limit for 1 line

class Principal(models.Model):
    """
    Principal content class

    Fields:
        name (str): principal name
        client_id (str): client_id
    """

    name = models.CharField(max_length=LINE_LENGTH)
    client_id = models.CharField(max_length=LINE_LENGTH)

    class Meta:
        abstract = True
        app_label = "acl"

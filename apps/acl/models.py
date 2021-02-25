from pathlib import Path

from django.db import models

import apps.acl.utils as utils
from apps.acl.mixin import RenderMixin

CSV_STRING_LENGTH = 300  # character limit for comma separated values
LINE_LENGTH = 80  # character limit for 1 line
PATH_LENGTH = 500
ACCESS_LENGTH = 3

class Principal(models.Model):
    """
    Principal content class

    Fields:
        name (str): principal name
        client_id (str): client_id
    """

    name = models.CharField(max_length=LINE_LENGTH)
    object_id = models.CharField(max_length=LINE_LENGTH)

    class Meta:
        abstract = True
        app_label = "acl"

class User(Principal):
    pass

class Group(Principal):
    pass

class ADLSDirectory(models.Model):
    """
    ADLS directory
    """
    literal_path = models.CharField(max_length=PATH_LENGTH)

    @property
    def path(self):
        return Path(self.literal_path)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['literal_path'], name='unique_directory')
        ] 

class ACL(models.Model, RenderMixin):

    adls_directory = models.OneToOneField(to=ADLSDirectory, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adls_directory'], name='unique_acl')
        ]

class UserPermission(models.Model):
    """read write execute permission"""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE) 
    access = models.CharField(max_length=ACCESS_LENGTH)
    acl = models.ForeignKey(to=ACL, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)

class GroupPermission(models.Model):
    group = models.OneToOneField(to=Group, on_delete=models.CASCADE)
    access = models.CharField(max_length=ACCESS_LENGTH)
    acl = models.ForeignKey(to=ACL, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)

"""
user::rwx,user:8a9d8fca-254d-462d-9187-2af59e4a2f8d:rwx,user:2a659042-4912-4f53-bd71-6b036c3f672d:rwx,group::r-x,group:6f979684-44b1-45be-aadb-db408c385d94:rwx,group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx,mask::rwx,other::---,default:user::rwx,default:user:8a9d8fca-254d-462d-9187-2af59e4a2f8d:rwx,default:user:2a659042-4912-4f53-bd71-6b036c3f672d:rwx,default:group::r-x,default:group:6f979684-44b1-45be-aadb-db408c385d94:rwx,default:group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx,default:mask::rwx,default:other::---"
"""


"""
[{
        "path": "/",
        "acl": [
            "user::rwx",
            "user:249de859-d25f-4d4e-834c-6a55459177ba:--x",
            "user:34e4c012-dbdb-4cb0-8b67-b9c3023f9394:--x",
            "group::r-x",
            "group:6f979684-44b1-45be-aadb-db408c385d94:--x",
            "group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "mask::r-x",
            "other::---",
            "default:user::rwx",
            "default:group::r-x",
            "default:group:6f979684-44b1-45be-aadb-db408c385d94:--x",
            "default:group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "default:mask::rwx",
            "default:other::---"
        ]
    }, {
        "path": "/Raw",
        "acl": [
            "user::rwx",
            "user:249de859-d25f-4d4e-834c-6a55459177ba:r-x",
            "user:34e4c012-dbdb-4cb0-8b67-b9c3023f9394:--x",
            "group::r-x",
            "group:6f979684-44b1-45be-aadb-db408c385d94:rwx",
            "group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "mask::rwx",
            "other::---",
            "default:user::rwx",
            "default:user:249de859-d25f-4d4e-834c-6a55459177ba:r-x",
            "default:group::r-x",
            "default:group:6f979684-44b1-45be-aadb-db408c385d94:rwx",
            "default:group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "default:mask::rwx",
            "default:other::---"
        ]
    }, {
        "path": "/Raw/tvs",
        "apply_recursive": true,
        "acl": [
            "user::rwx",
            "user:249de859-d25f-4d4e-834c-6a55459177ba:r-x",
            "user:34e4c012-dbdb-4cb0-8b67-b9c3023f9394:rwx",
            "group::r-x",
            "group:6f979684-44b1-45be-aadb-db408c385d94:rwx",
            "group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "mask::rwx",
            "other::---",
            "default:user::rwx",
            "default:user:249de859-d25f-4d4e-834c-6a55459177ba:r-x",
            "default:user:34e4c012-dbdb-4cb0-8b67-b9c3023f9394:rwx",
            "default:group::r-x",
            "default:group:6f979684-44b1-45be-aadb-db408c385d94:rwx",
            "default:group:beb0efb8-fe21-4e80-81d7-7bdb0981a006:rwx",
            "default:mask::rwx",
            "default:other::---"
        ]
    }
]
"""



"""This module stores the manage.py uml command."""
from django.core.management import BaseCommand, call_command
from django.conf import settings

from apps.acl.views import render


class Command(BaseCommand):
    """This command generates ACLs."""

    help = "Creates ACLs"

    def handle(self, *args, **options):
        acl = render()
        with open('acl.txt', 'w') as f:
            f.write(acl)

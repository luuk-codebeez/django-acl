"""This module stores the manage.py uml command."""
from django.core.management import BaseCommand, call_command
from django.conf import settings
from django.http import HttpRequest


from apps.acl.views import render_acls



class Command(BaseCommand):
    """This command generates ACLs."""

    help = "Creates ACLs"

    def handle(self, *args, **options):
        acl = render_acls()
        with open('acl.txt', 'w') as f:
            f.write(acl)

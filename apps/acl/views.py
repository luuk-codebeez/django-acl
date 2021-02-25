from django.shortcuts import render
from django.template.loader import get_template
from apps.acl.models import ACL


def render_acls():
    context = {"acls": ACL.objects.all()}

    template = get_template("acls.html")

    return template.render(context=context)
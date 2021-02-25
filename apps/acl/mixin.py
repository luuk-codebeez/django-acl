"""
presentation related mixin for objects
"""
import os.path

from django.template.loader import get_template, render_to_string

import apps.acl.utils as utils

COMPONENTS_FOLDER = "components"


class RenderMixin(object):
    """
    Adds render functionality to support the {% include object %} template tag

    adds render capability to our CMS models, as they are primarily concerned
    with presentation, allowing embedding in the templates
    """

    @property
    def template(self):
        return self

    @property
    def template_to_render(self):
        """Return template based on instance class name"""
        return get_template(
            os.path.join(
                COMPONENTS_FOLDER,
                utils.camelcase_to_underscore(self.__class__.__name__) + ".html",
            )
        )

    def render(self, context):
        return self.template_to_render.render(context={"object": self}, request=None)
import os

from django import template

import ajax_forms
from django.conf import settings

register = template.Library()

def include_validation():
    return '''<script type="text/javascript" src="%sajax_forms/js/jquery-ajax-validation.js"></script>''' % settings.STATIC_URL
register.simple_tag(include_validation)

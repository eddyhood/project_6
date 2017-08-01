from random import choice

from django import template
from django.utils.safestring import mark_safe

import markdown2

from rocks.models import Rock


register = template.Library()


@register.simple_tag
def random_rock():
    """Chooses a random # for the random link"""
    rocks = Rock.objects.all()
    rand_rock = choice(rocks)
    return rand_rock.name


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown to html"""
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

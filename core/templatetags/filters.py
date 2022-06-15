from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from markdownx.utils import markdownify

# Library to hold the Django template filters.
register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown(text):
    """Django filter that renders markdown data as safe HTML
    directly in the template.
    """

    return mark_safe(markdownify(text))

from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from markdownx.utils import markdownify

register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown(text):
    return mark_safe(markdownify(text))

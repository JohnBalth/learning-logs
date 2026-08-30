from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def highlight(text, query):
    if not text or not query:
        return text

    pattern = re.compile(
        re.escape(query),
        re.IGNORECASE
    )

    highlighted = pattern.sub(
        lambda match: f'<mark>{match.group(0)}</mark>',
        str(text)
    )

    return mark_safe(highlighted)



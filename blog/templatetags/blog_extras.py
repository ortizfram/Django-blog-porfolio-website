import markdown

from django import template
from django.template.defaultfilters import stringfilter
import markdown.extensions.codehilite
import markdown.extensions.fenced_code

register = template.Library()


@register.filter
@stringfilter
def convert_markdown_with_highlight(value):
    return markdown.markdown(
        value,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.codehilite",  # Enable code highlighting
        ],
        extension_configs={
            "markdown.extensions.codehilite": {
                "linenums": True,  # Add line numbers (optional)
                "guess_lang": False,  # Do not guess the language
            }
        },
    )

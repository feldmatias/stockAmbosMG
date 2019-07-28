import random
import string

from django import template

register = template.Library()

RANDOM_LENGTH = 20


@register.simple_tag
def random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=RANDOM_LENGTH))

from django import template
register = template.Library()

@register.filter()
def mod(item):
    return item%4

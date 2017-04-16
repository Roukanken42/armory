from django import template

register = template.Library()

@register.filter(name="zip")
def zip_lists(a, b):
    try:
        return zip(a, b)
    except TypeError:
        return None

@register.filter(name="getitem")
def getitem(obj, value):
    try: 
        return obj[value]
    except KeyError:
        return None



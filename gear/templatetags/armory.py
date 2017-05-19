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

@register.filter(name="addstr")
def addstr(a, b):
    try: 
        return str(a) + str(b)
    except (TypeError, ValueError):
        return None


class OnceNode(template.Node):
    def __init__(self, content):
        self.content = content

    def render(self, context):
        if self not in context.render_context:
            context.render_context[self] = True
            return self.content.render(context)

        return ""

def once(parser, token):
    content = parser.parse(('endonce',))
    parser.delete_first_token()
    return OnceNode(content)

register.tag("once", once)
from django import template

register = template.Library()


def cut(value, arg):
    """
    this will cut the string 'arg' from the string 'value'
    """
    return value.replace(arg, '')


# ONE METHOD TO REGISTER
# filters('name by which it called in template', function_name)
register.filter('cut', cut)


# SECOND METHOD TO REGISTER IS TO USE DECORATORS
@register.filter(name='add_last')
def add_last(value, arg):
    """Adds the arg to the arg."""
    try:
        return value + ' ' + arg
    except (ValueError, TypeError):
        return value


from django import template

register = template.Library()

@register.simple_tag()
def get_stroky(Argument=None):
    if not Argument:
        return "Теги без аргумента"
    else:
        return "Тег с аргументом "+str(Argument)

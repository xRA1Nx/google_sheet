from django import template

register = template.Library()


@register.filter(name="get_num")
def censorship(value, page):
    return (page - 1) * 10 + value

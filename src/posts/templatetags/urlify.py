from urllib import quote_plus
from django import template

register = template.Library()

#registers filter and helps to load as tagf
@register.filter
def urlify(value):
	return quote_plus(value)
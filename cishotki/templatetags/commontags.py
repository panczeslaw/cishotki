import os

import sys

import random

import urllib.parse as urlparse

from django import template

register = template.Library()

@register.filter
def modulo(num, val):
	return num % val


@register.filter
def split(value, arg):
    return value.split(arg)


@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.seed()
    random.shuffle(tmp)
    return tmp


@register.simple_tag
def get_form_errors(form, field):
    return "\n".join([i for i in form[field]])


@register.simple_tag
def langurl(url, val):
	params = {"lang": val}
	url_parts = list(urlparse.urlparse(url))
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	url_parts[4] = urlparse.urlencode(query)
	return urlparse.urlunparse(url_parts)


from django import template
from django.http import HttpRequest

registe = template Library()


@register.filter(name='show_sidebar')
def show_sidebar():


from django import template
from django.apps import apps

#Carrega o registro de template tags
register = template.Library()

#Registra o metodo a seguir como uma inclusion_tag indicando o template a ser renderizado
@register.inclusion_tag('menus_por_app.html')
def menus_por_app():
    lst = apps.get_app_configs()
    return { 'lst_apps' : lst }
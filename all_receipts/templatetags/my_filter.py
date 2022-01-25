from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()#создаём экземпляр класса library

#навешиваем декоратор и используем метод фильтр
@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)

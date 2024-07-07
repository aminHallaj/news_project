from news.models import News
from django import template


register = template.Library()

@register.filter
def post_count(category):
    return News.objects.filter(sub_category__category=category).count()
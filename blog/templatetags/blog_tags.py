from django import template
from ..models import Tag 
from django.db.models import Count 

register = template.Library()
@register.simple_tag
def get_tags():
    
    return Tag.objects.all().annotate(tags_count = Count('blog_tag'))
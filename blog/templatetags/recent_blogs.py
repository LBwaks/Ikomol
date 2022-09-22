
from django import  template
from ..models import Blog 
import datetime 

register = template.Library()

@register.simple_tag()
def recent_blogs():   
    return Blog.objects.filter().order_by('-created_date')[:5]
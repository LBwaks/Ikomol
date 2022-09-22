from django.contrib import admin
from .models import Tag,Blog,Comment
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display =('name','description','created_date')

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user =request.user
        obj.save()
admin.site.register(Tag,TagAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display =('title','tag','is_published','created_date')

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user 
        obj.save()
admin.site.register(Blog,BlogAdmin)

admin.site.register(Comment)
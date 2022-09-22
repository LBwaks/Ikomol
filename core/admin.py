from atexit import register
from django.contrib import admin
from .models import Contact, Package,Service,SiteDetails
# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display =('type','download_speed','price','period')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user =request.user
        obj.save()
admin.site.register(Package,PackageAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display =('title','description','created_date')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user =request.user
        obj.save()    
admin.site.register(Service,ServiceAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display =('name','email','subject','message','created_date')
admin.site.register(Contact,ContactAdmin)
admin.site.register(SiteDetails)
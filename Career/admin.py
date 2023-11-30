from django.contrib import admin
from .models import Job


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Admin View for Job"""

    list_display = ("title", "job_type", "location", "deadline")

    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ("user",)

    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()

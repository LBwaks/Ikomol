from django import form
from .models import Job
from ckeditor.widgets import CKEditorWidget


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # content = forms.CharField(widget=CKEditorWidget())
        fields = ("",)

from django import forms 
from .models import Comment
from django_ckeditor_5.widgets import CKEditor5Widget

class CommentForm(forms.ModelForm):
      """Form for comments to the article."""

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

      class Meta:
          model = Comment
          fields = ("name", "email",'body')
          widgets = {
              "name":forms.TextInput(attrs={'class':'form-control name ' 'required'}),
              'email': forms.EmailInput(attrs={'class':'form-control email ' 'required'}),
              "body": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="comment" )
          }
class SearchForm(forms.Form):
    q = forms.CharField
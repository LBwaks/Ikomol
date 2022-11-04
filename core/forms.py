from dataclasses import fields
from email import message
from django import forms
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail
# from .tasks import send_feedback_email_task

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def get_info(self):
        cleaned_data = super(ContactForm,self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject =cleaned_data.get('subject')
        message =f'{name} with email {email} said:'
        message += f'\n Subject: "{subject}"\n\n'
        message += cleaned_data.get('message')

        return name, subject,message
    def send(self):
        subject , name , message =self.get_info()
        send_mail(
            # name =name,
            subject =subject,
            message=message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.RECIPIENT_ADDRESS]
        )
        
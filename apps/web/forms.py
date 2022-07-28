from django.forms import (
    CharField,
    DateTimeField,
    DateTimeInput,
    EmailField,
    Form,
    ModelForm,
    Textarea,
)

from ckeditor.widgets import CKEditorWidget

from apps.general.outils.emailing import EmailingSystem

from .models import WebsiteEmail
from .tasks import send_website_email_task


class ContactForm(Form):
    name = CharField(label='Nombre', required=True)
    email = EmailField(label='Email', required=True)
    message = CharField(widget=Textarea, label='Mensaje', required=True)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        message = f"{name} con el email {email} ha enviado {message}"
        subject = 'Nuevo mensaje desde suport'
        EmailingSystem().simple_email(subject, message)


class WebEmailForm(ModelForm):
    # content = CharField(widget=CKEditorWidget(config_name='default'))
    date_to_send = DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datetimepicker1'
        })
    )

    class Meta:
        model = WebsiteEmail
        fields = ['title', 'content', 'date_to_send']
    
    def save(self):
        web_email = super(WebEmailForm, self).save()
        send_website_email_task.delay()
        return web_email
from django.forms import (
    CharField,
    DateTimeField,
    DateTimeInput,
    EmailField,
    Form,
    ModelForm,
    Textarea,
)
from django.contrib.admin import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, RelatedFieldWidgetWrapper

from apps.general.outils.emailing import EmailingSystem

from apps.web.models import WebsiteEmail


class ContactForm(Form):
    name = CharField(label="Nombre", required=True)
    email = EmailField(label="Email", required=True)
    message = CharField(widget=Textarea, label="Mensaje", required=True)

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]
        EmailingSystem.simple_email(f"{name} con el email {email} ha enviado {message}", "Nuevo mensaje desde suport")


class WebEmailForm(ModelForm):
    date_to_send = DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        widget=DateTimeInput(attrs={"class": "form-control datetimepicker-input"}),
        required=False,
    )

    class Meta:
        model = WebsiteEmail
        fields = [
            "title",
            "date_to_send",
            "content",
            "type_related",
            "whom_to_send",
            "users_selected",
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["type_related"].widget = RelatedFieldWidgetWrapper(
            self.fields["type_related"].widget,
            self.instance._meta.get_field("type_related").remote_field,
            site,
        )

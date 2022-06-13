from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags

from rest_framework.serializers import (
    CharField,
    Serializer,
    ModelSerializer,
    ValidationError
)

from .models import Key


class RichTextField(CharField):
    def to_representation(self, value):
        return strip_tags(value)


class AuthKeySerializer(Serializer):
    username = CharField(
        label=_("Username"),
        write_only=True
    )
    password = CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    key = CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
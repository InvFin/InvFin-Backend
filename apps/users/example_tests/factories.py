from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory
from model_bakery import baker

User = get_user_model()

super_user = baker.make(User, is_superuser=True)
regular_user = baker.make(User, is_superuser=False)

class ExampleUser:
    pass


class UserFactory(DjangoModelFactory):
    id = 1
    username = 'Lucas'
    email = 'test@example.com'
    first_name = 'Lucas'
    last_name = 'Montes'

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["id"]
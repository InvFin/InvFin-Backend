import urllib
import pytest

import datetime
from typing import Dict, Any
from unittest import skip

from bfet import DjangoTestingModel

from django.http import HttpResponseServerError
from django.shortcuts import resolve_url
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.exceptions import ErrorDetail
from rest_framework import status
from rest_framework.test import APITestCase

from apps.api.models import Key
from apps.business.models import (
    Customer,
    Product,
    ProductComplementary,
    ProductSubscriber,
)
from apps.general.models import Currency

User = get_user_model()

HTTP_VERBS = {
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "DELETE",
    "CONNECT",
    "OPTIONS",
    "TRACE",
    "PATCH",
}


class BaseAPIViewTest(APITestCase):
    """
    Mixin for sharing test methods for views.
    Needs the following attributes:
      - allowed_verbs: containing a set of HTTP verbs that should not return 405,
        check HTTP_VERBS for full list of verbs.
      - endpoint: full url
    """
    api_prefix: str = "api"
    api_version: str = settings.API_VERSION["CURRENT_VERSION"]
    allowed_verbs: Dict = {"GET", "HEAD", "OPTIONS"}
    path_name: str = ""
    url_path: str = ""
    api_key_param: str = "api_key"
    no_key_error_message: str = (
        "Tu clave es incorrecta, asegúrate que está bien escrita depués de api_key=<clave> o pide tu clave desde tu"
        " perfil"
    )
    params: Dict[str, Any] = {}
    wrong_param_error_message: str = "Ha habido un problema con tu búsqueda, asegúrate de haber introducido un valor"
    no_param_error_messages: str = "No has introducido ninguna búsqueda"
    not_found_error_messages: str = "Tu búsqueda no ha devuelto ningún resultado"
    server_problem_error_message: str = "Lo siento ha habido un problema"

    @classmethod
    def setUpTestData(cls) -> None:
        user_key_sub = DjangoTestingModel.create(User)
        user_key_removed = DjangoTestingModel.create(User)
        user_key = DjangoTestingModel.create(User)
        product = DjangoTestingModel.create(Product, title="Excel", slug="excel", is_active=True)
        product_complementary = DjangoTestingModel.create(
            ProductComplementary,
            title="Subscripción excel",
            product=product,
            is_active=True,
            currency=DjangoTestingModel.create(Currency),
        )
        product_subscriber = DjangoTestingModel.create(
            ProductSubscriber,
            product=product,
            product_complementary=product_complementary,
            subscriber=user_key_sub,
            is_active=True,
        )
        cls.subscription_key = DjangoTestingModel.create(
                    Key, user=user_key_sub, in_use=True, removed=None, subscription=product_subscriber
                )
        cls.removed_key = DjangoTestingModel.create(
            Key, user=user_key_removed, in_use=False, removed=datetime.datetime.utcnow()
        )
        cls.key = DjangoTestingModel.create(Key, user=user_key, in_use=True, removed=None)

    def test_verbs(self):
        endpoint = resolve_url(self.path_name)
        full_endpoint = f"{endpoint}?{self.api_key_param}={self.subscription_key.key}"
        if self.params:
            params = urllib.parse.urlencode(self.params)
            full_endpoint = f"{full_endpoint}&{params}"

        for verb in self.allowed_verbs:
            with self.subTest(f"testing {verb}"):
                assert self.client.generic(verb, full_endpoint).status_code != status.HTTP_405_METHOD_NOT_ALLOWED
                assert self.client.generic(verb, full_endpoint).status_code == status.HTTP_200_OK

        for verb in HTTP_VERBS - self.allowed_verbs:
            with self.subTest(f"testing {verb}"):
                assert (
                    self.client.generic(verb, full_endpoint).status_code == status.HTTP_403_FORBIDDEN
                )  # status.HTTP_405_METHOD_NOT_ALLOWED

    def test_url(self):
        assert resolve_url(self.path_name) == f"/{self.api_prefix}/{self.api_version}{self.url_path}"

    @skip("Skipping")
    def test_no_auth(self):
        """
        TODO
        Add wrong key
        Add no key
        Add key not allowed
        """
        endpoint = resolve_url(self.path_name)
        full_endpoint_removed_key = f"{endpoint}?{self.api_key_param}={self.removed_key.key}"
        full_endpoint_wrong_key = f"{endpoint}?{self.api_key_param}={self.removed_key.key}4"
        full_endpoint_no_key = f"{endpoint}?{self.api_key_param}="
        if self.params:
            params = urllib.parse.urlencode(self.params)
            full_endpoint_removed_key = f"{full_endpoint_removed_key}&{params}"
            full_endpoint_wrong_key = f"{full_endpoint_wrong_key}&{params}"
            full_endpoint_no_key = f"{full_endpoint_no_key}&{params}"

        response = self.client.get(full_endpoint_removed_key)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.data == {"detail": ErrorDetail(string=self.no_key_error_message, code="permission_denied")}

        response = self.client.get(full_endpoint_wrong_key)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.data == {"detail": ErrorDetail(string=self.no_key_error_message, code="permission_denied")}

        response = self.client.get(full_endpoint_no_key)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.data == {"detail": ErrorDetail(string=self.no_key_error_message, code="permission_denied")}

    @skip("Skipping")
    def test_server_problem(self):
        """
        TODO
        Mock the request to assert en error
        """
        endpoint = resolve_url(self.path_name)

        full_endpoint = f"{endpoint}?{self.api_key_param}={self.key.key}"
        if self.params:
            params = urllib.parse.urlencode(self.params)
            full_endpoint = f"{full_endpoint}&{params}"

        with pytest.raises(HttpResponseServerError):
            response = self.client.get(self.endpoint_key)
            assert response.status_code == status.HTTP_403_FORBIDDEN
            assert response.data == {
                "detail": ErrorDetail(string=self.server_problem_error_message, code="permission_denied")
            }

    @skip("Skipping")
    def test_no_params(self):
        """
        TODO
        Fix it, it returns 404 instead of 400
        """
        endpoint = resolve_url(self.path_name)
        endpoint_key = f"{endpoint}?{self.api_key_param}={self.key.key}&"
        if self.params:
            response = self.client.get(endpoint_key)
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert response.data == {"detail": ErrorDetail(string=self.no_param_error_messages, code="parse_error")}

    @skip("Skipping")
    def test_wrong_params(self):
        """
        TODO
        Fix it, it returns 404 instead of 400
        """
        endpoint = resolve_url(self.path_name)
        endpoint_key = f"{endpoint}?{self.api_key_param}={self.key.key}"

        if self.params:
            for key in self.params.keys():
                params = self.params
                params["bad"] = params.pop(key)
                params = urllib.parse.urlencode(params)
                response = self.client.get(f"{endpoint_key}&{params}")
                assert response.status_code == status.HTTP_400_BAD_REQUEST
                assert response.data == {
                    "detail": ErrorDetail(string=self.wrong_param_error_message, code="parse_error")
                }

    def test_not_found(self):
        endpoint = resolve_url(self.path_name)
        endpoint_key = f"{endpoint}?{self.api_key_param}={self.key.key}"
        if self.params:
            for key in self.params.keys():
                params = self.params
                params[key] = "random"
                params = urllib.parse.urlencode(params)
                response = self.client.get(f"{endpoint_key}&{params}")
                assert response.status_code == status.HTTP_404_NOT_FOUND
                assert response.data == {"detail": ErrorDetail(string=self.not_found_error_messages, code="not_found")}

    def test_success(self):
        endpoint = resolve_url(self.path_name)
        full_endpoint = f"{endpoint}?{self.api_key_param}={self.key.key}"
        if self.params:
            params = urllib.parse.urlencode(self.params)
            full_endpoint = f"{full_endpoint}&{params}"

        response = self.client.get(full_endpoint)
        assert response.status_code == status.HTTP_200_OK

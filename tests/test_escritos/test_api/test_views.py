import json

from django.contrib.auth import get_user_model

from bfet import DjangoTestingModel
from rest_framework.test import APITestCase

from src.classifications.models import Category
from src.escritos.models import Term, TermContent
from tests.data.escritos import escritos_data
from tests.utils import BaseAPIViewTestMixin

User = get_user_model()


class TestAllTermsAPIView(BaseAPIViewTestMixin, APITestCase):
    path_name = "api:all_terms_api"
    url_path = "/lista-terminos/"

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        category = DjangoTestingModel.create(Category, name="category")
        author = DjangoTestingModel.create(
            User, username="lucasMontes", first_name="Lucas", last_name="Montes"
        )
        DjangoTestingModel.create(Term, category=category, author=author, **escritos_data.TERM)
        DjangoTestingModel.create(Term, author=author, **escritos_data.EMPTY_TERM)
        DjangoTestingModel.create(Term, author=author, **escritos_data.BALANCE_SHEET_TERM)

    def test_success_response(self):
        response = self.client.get(self.full_endpoint, format="json")
        expected_data = [
            {
                "id": 1,
                "titulo": "Precio valor contable (P/B)",
                "slug": "precio-valor-en-libros",
                "link": "http://example.com:8000/definicion/precio-valor-en-libros/",
                "resumen": (
                    "El price to book compara el precio de mercado de una empresa con su valor"
                    " en libros, que muestra esencialmente el valor dado por el mercado por"
                    " cada dólar del patrimonio neto de la compañía."
                ),
                "votos_totales": 0,
                "visitas_totales": 238,
                "veces_compartido": 0,
                "categoria": "category",
                "autor": "Lucas Montes",
                "imagen": "/static/general/assets/img/general/why-us.webp",
            },
            {
                "id": 2,
                "titulo": "El balance sheet",
                "slug": "el-balance-sheet-en-espanol",
                "link": "http://example.com:8000/definicion/el-balance-sheet-en-espanol/",
                "resumen": (
                    "El balance general es el estado financiero que muestra los activos, los"
                    " pasivos y el patrimonio de los accionistas."
                ),
                "votos_totales": 0,
                "visitas_totales": 180,
                "veces_compartido": 0,
                "categoria": None,
                "autor": "Lucas Montes",
                "imagen": (
                    "https://cdn.wallstreetmojo.com/wp-content/uploads/2019/11/"
                    "Comparative-Balance-Sheet-Example-1.1-1.png"
                ),
            },
        ]
        self.assertEqual(expected_data, json.loads(json.dumps(response.data)))


class TestTermAPIView(BaseAPIViewTestMixin, APITestCase):
    path_name = "api:term_api"
    url_path = "/termino/"
    params = {"id": 1}

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        category = DjangoTestingModel.create(Category, name="category")
        author = DjangoTestingModel.create(
            User, username="lucas3245Montes", first_name="Lucas", last_name="Montes"
        )
        term = DjangoTestingModel.create(
            Term, category=category, author=author, **escritos_data.TERM
        )
        for term_content in escritos_data.TERM_CONTENT:
            DjangoTestingModel.create(TermContent, term_related=term, **term_content)

    def test_success_response(self):
        response = self.client.get(self.full_endpoint, format="json")
        expected_data = {
            "id": 1,
            "titulo": "Precio valor contable (P/B)",
            "slug": "precio-valor-en-libros",
            "link": "http://example.com:8000/definicion/precio-valor-en-libros/",
            "resumen": (
                "El price to book compara el precio de mercado de una empresa con su valor en"
                " libros, que muestra esencialmente el valor dado por el mercado por cada"
                " dólar del patrimonio neto de la compañía."
            ),
            "votos_totales": 0,
            "visitas_totales": 238,
            "veces_compartido": 0,
            "categoria": "category",
            "autor": "Lucas Montes",
            "imagen": "/static/general/assets/img/general/why-us.webp",
            "partes": [
                {
                    "id": 1,
                    "titulo": "¿Qué es el price to book?",
                    "orden": "0",
                    "contenido": (
                        "El price to book compara el precio de mercado de una empresa con su"
                        " valor en libros, que muestra esencialmente el valor dado por el"
                        " mercado por cada d&oacute;lar del patrimonio neto de la"
                        " compa&ntilde;&iacute;a.\r\n\r\nRecordemos que el patrimonio neto se"
                        " calcula restando los pasivos a los activos de la empresa que"
                        " est&aacute;n inscritos en el balance general.\r\n\r\nPatrimonio neto"
                        " = Activos - Pasivos\r\n\r\nEl valor en&nbsp; libros es"
                        " tambi&eacute;n el valor de activos netos tangibles de una empresa"
                        " calculada como, los activos totales menos los activos intangibles,"
                        " por ejemplo: Patentes, goodwill y pasivos.\r\n\r\nLas"
                        " compa&ntilde;&iacute;as de alto crecimiento a menudo"
                        " mostrar&aacute;n un PtoB muy por encima de 1.0, mientras que las"
                        " compa&ntilde;&iacute;as que enfrentan una angustia severa"
                        " ocasionalmente mostrar&aacute;n ratios por debajo de 1.0. La"
                        " relaci&oacute;n precio-valor en libros es importante porque puede"
                        " ayudar a los inversores a comprender si el precio de mercado de una"
                        " empresa parece razonable en comparaci&oacute;n con su balance. Por"
                        " ejemplo, si una empresa muestra una proporci&oacute;n de alto"
                        " precio-valor en libros, los inversores pueden verificar si esa"
                        " valoraci&oacute;n est&aacute; justificada, dadas otras medidas, como"
                        " su retorno hist&oacute;rico sobre los activos o el crecimiento en"
                        " las ganancias por acci&oacute;n (EPS). La relaci&oacute;n"
                        " precio-valor en libros tambi&eacute;n se usa frecuentemente para"
                        " detectar posibles oportunidades de inversi&oacute;n.\r\n\r\n&nbsp;"
                    ),
                    "link": "http://example.com:8000/definicion/precio-valor-en-libros/#que-es-el-price-to-book",
                },
                {
                    "id": 2,
                    "titulo": "¿Qué te cuenta el price to book?",
                    "orden": "1",
                    "contenido": (
                        "En otras palabras, si una empresa liquidase todos sus activos y"
                        " pagara toda su deuda, el valor restante ser&iacute;a el valor del"
                        " libro de la compa&ntilde;&iacute;a. La relaci&oacute;n precio valor"
                        " contable proporciona una valiosa verificaci&oacute;n de la realidad"
                        " para los inversores que buscan un crecimiento a un precio razonable"
                        " y a menudo se considera junto con el retorno del capital (ROE), un"
                        " indicador de crecimiento confiable.&nbsp;\r\n\r\nAlgunas personas"
                        " pueden conocer esta relaci&oacute;n con su nombre menos"
                        " com&uacute;n, la relaci&oacute;n precio-equidad. En esta"
                        " ecuaci&oacute;n, el valor en libros por acci&oacute;n se calcula de"
                        " la siguiente la siguiente manera:\r\n\r\n&nbsp;\r\n\r\nP/B ="
                        " (activos totales/ pasivos totales) / n&uacute;mero de acciones en"
                        " circulaci&oacute;n&nbsp;\r\n\r\n&nbsp;\r\n\r\nLas acciones de"
                        " crecimiento sobrevaloradas frecuentemente muestran una"
                        " combinaci&oacute;n de ratios bajos y ratio precio valor contable"
                        " altos. Si el ROE de una empresa est&aacute; creciendo, su"
                        " relaci&oacute;n precio valor contable tambi&eacute;n tendr&iacute;a"
                        " que estar creciendo.\r\n\r\n&nbsp;"
                    ),
                    "link": "http://example.com:8000/definicion/precio-valor-en-libros/#que-te-cuenta-el-price-to-book",
                },
            ],
        }
        self.assertEqual(expected_data, json.loads(json.dumps(response.data)))
        with self.subTest("Test with slug instead of id"):
            self.params = {"slug": "precio-valor-en-libros"}
            response = self.client.get(self.full_endpoint, format="json")
            expected_data = {
                "id": 1,
                "titulo": "Precio valor contable (P/B)",
                "slug": "precio-valor-en-libros",
                "link": "http://example.com:8000/definicion/precio-valor-en-libros/",
                "resumen": (
                    "El price to book compara el precio de mercado de una empresa con su valor"
                    " en libros, que muestra esencialmente el valor dado por el mercado por"
                    " cada dólar del patrimonio neto de la compañía."
                ),
                "votos_totales": 0,
                "visitas_totales": 238,
                "veces_compartido": 0,
                "categoria": "category",
                "autor": "Lucas Montes",
                "imagen": "/static/general/assets/img/general/why-us.webp",
                "partes": [
                    {
                        "id": 1,
                        "titulo": "¿Qué es el price to book?",
                        "orden": "0",
                        "contenido": (
                            "El price to book compara el precio de mercado de una empresa con"
                            " su valor en libros, que muestra esencialmente el valor dado por"
                            " el mercado por cada d&oacute;lar del patrimonio neto de la"
                            " compa&ntilde;&iacute;a.\r\n\r\nRecordemos que el patrimonio neto"
                            " se calcula restando los pasivos a los activos de la empresa que"
                            " est&aacute;n inscritos en el balance general.\r\n\r\nPatrimonio"
                            " neto = Activos - Pasivos\r\n\r\nEl valor en&nbsp; libros es"
                            " tambi&eacute;n el valor de activos netos tangibles de una"
                            " empresa calculada como, los activos totales menos los activos"
                            " intangibles, por ejemplo: Patentes, goodwill y"
                            " pasivos.\r\n\r\nLas compa&ntilde;&iacute;as de alto crecimiento"
                            " a menudo mostrar&aacute;n un PtoB muy por encima de 1.0,"
                            " mientras que las compa&ntilde;&iacute;as que enfrentan una"
                            " angustia severa ocasionalmente mostrar&aacute;n ratios por"
                            " debajo de 1.0. La relaci&oacute;n precio-valor en libros es"
                            " importante porque puede ayudar a los inversores a comprender si"
                            " el precio de mercado de una empresa parece razonable en"
                            " comparaci&oacute;n con su balance. Por ejemplo, si una empresa"
                            " muestra una proporci&oacute;n de alto precio-valor en libros,"
                            " los inversores pueden verificar si esa valoraci&oacute;n"
                            " est&aacute; justificada, dadas otras medidas, como su retorno"
                            " hist&oacute;rico sobre los activos o el crecimiento en las"
                            " ganancias por acci&oacute;n (EPS). La relaci&oacute;n"
                            " precio-valor en libros tambi&eacute;n se usa frecuentemente para"
                            " detectar posibles oportunidades de"
                            " inversi&oacute;n.\r\n\r\n&nbsp;"
                        ),
                        "link": "http://example.com:8000/definicion/precio-valor-en-libros/#que-es-el-price-to-book",
                    },
                    {
                        "id": 2,
                        "titulo": "¿Qué te cuenta el price to book?",
                        "orden": "1",
                        "contenido": (
                            "En otras palabras, si una empresa liquidase todos sus activos y"
                            " pagara toda su deuda, el valor restante ser&iacute;a el valor"
                            " del libro de la compa&ntilde;&iacute;a. La relaci&oacute;n"
                            " precio valor contable proporciona una valiosa"
                            " verificaci&oacute;n de la realidad para los inversores que"
                            " buscan un crecimiento a un precio razonable y a menudo se"
                            " considera junto con el retorno del capital (ROE), un indicador"
                            " de crecimiento confiable.&nbsp;\r\n\r\nAlgunas personas pueden"
                            " conocer esta relaci&oacute;n con su nombre menos com&uacute;n,"
                            " la relaci&oacute;n precio-equidad. En esta ecuaci&oacute;n, el"
                            " valor en libros por acci&oacute;n se calcula de la siguiente la"
                            " siguiente manera:\r\n\r\n&nbsp;\r\n\r\nP/B = (activos totales/"
                            " pasivos totales) / n&uacute;mero de acciones en"
                            " circulaci&oacute;n&nbsp;\r\n\r\n&nbsp;\r\n\r\nLas acciones de"
                            " crecimiento sobrevaloradas frecuentemente muestran una"
                            " combinaci&oacute;n de ratios bajos y ratio precio valor contable"
                            " altos. Si el ROE de una empresa est&aacute; creciendo, su"
                            " relaci&oacute;n precio valor contable tambi&eacute;n"
                            " tendr&iacute;a que estar creciendo.\r\n\r\n&nbsp;"
                        ),
                        "link": "http://example.com:8000/definicion/precio-valor-en-libros/#que-te-cuenta-el-price-to-book",
                    },
                ],
            }
            self.assertEqual(expected_data, json.loads(json.dumps(response.data)))

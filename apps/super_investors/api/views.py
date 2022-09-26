from django.contrib.auth import get_user_model

from apps.api.pagination import StandardResultPagination
from apps.api.views import BaseAPIView

from ..models import Superinvestor, SuperinvestorActivity, SuperinvestorHistory
from .serializers import (
    SuperinvestorActivitySerializer,
    SuperinvestorHistorySerializer,
    SuperinvestorSerializer,
)

User = get_user_model()


class AllSuperinvestorsAPIView(BaseAPIView):
    serializer_class = SuperinvestorSerializer
    queryset = Superinvestor
    pagination_class = StandardResultPagination


class SuperinvestorActivityAPIView(BaseAPIView):
    serializer_class = SuperinvestorActivitySerializer
    queryset = SuperinvestorActivity
    pagination_class = StandardResultPagination
    url_parameters = ["slug"]
    fk_lookup_model = "superinvestor_related__info_accronym"


class SuperinvestorHistoryAPIView(BaseAPIView):
    serializer_class = SuperinvestorHistorySerializer
    queryset = SuperinvestorHistory
    pagination_class = StandardResultPagination
    url_parameters = ["slug"]
    fk_lookup_model = "superinvestor_related__info_accronym"

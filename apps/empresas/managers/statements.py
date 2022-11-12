from django.db.models import Q, QuerySet

from apps.general.managers import BaseManager, BaseQuerySet

from apps.periods import constants


class BaseStatementQuerySet(BaseQuerySet):
    def quarterly(self) -> QuerySet:
        return self.exclude(period__period=constants.PERIOD_FOR_YEAR)

    def yearly(self) -> QuerySet:
        return self.filter(period__period=constants.PERIOD_FOR_YEAR)


class BaseStatementManager(BaseManager):
    def get_queryset(self):
        return BaseStatementQuerySet(self.model, using=self._db)

    def quarterly(self, **kwargs) -> QuerySet:
        return self.get_queryset().quarterly(**kwargs)

    def yearly(self, include_ttm: bool = True, **kwargs) -> QuerySet:
        yearly_filtered = self.filter(Q(is_ttm=include_ttm) | Q(period__period=constants.PERIOD_FOR_YEAR), **kwargs)
        if yearly_filtered:
            return yearly_filtered
        else:
            if kwargs:
                return self.filter(**kwargs)
            else:
                return self.all()

    def yearly_exclude_ttm(self, **kwargs) -> QuerySet:
        return self.yearly(False, **kwargs)

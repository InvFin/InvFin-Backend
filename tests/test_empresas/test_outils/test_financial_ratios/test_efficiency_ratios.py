from django.test import TestCase

from src.empresas.outils.financial_ratios.efficiency_ratios import EfficiencyRatios


class TestEfficiencyRatios(TestCase):
    def test_calculate_days_inventory_outstanding(self):
        assert 0.0002 == EfficiencyRatios.calculate_days_inventory_outstanding(234.67, 3333)
        assert 0.1615 == EfficiencyRatios.calculate_days_inventory_outstanding(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_days_inventory_outstanding(234.67, 0)

    def test_calculate_days_payables_outstanding(self):
        assert 25.699 == EfficiencyRatios.calculate_days_payables_outstanding(234.67, 3333)
        assert 21521.244 == EfficiencyRatios.calculate_days_payables_outstanding(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_days_payables_outstanding(234.67, 0)

    def test_calculate_days_sales_outstanding(self):
        assert 25.699 == EfficiencyRatios.calculate_days_sales_outstanding(234.67, 3333)
        assert 21521.244 == EfficiencyRatios.calculate_days_sales_outstanding(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_days_sales_outstanding(234.67, 0)

    def test_calculate_operating_cycle(self):
        assert 3567.67 == EfficiencyRatios.calculate_operating_cycle(234.67, 3333)
        assert 238.65 == EfficiencyRatios.calculate_operating_cycle(234.67, 3.98)
        assert 234.67 == EfficiencyRatios.calculate_operating_cycle(234.67, 0)

    def test_calculate_cash_conversion_cycle(self):
        assert 3545.67 == EfficiencyRatios.calculate_cash_conversion_cycle(234.67, 3333, 22)
        assert 216.6 == EfficiencyRatios.calculate_cash_conversion_cycle(234.62, 3.98, 22)
        assert 234.67 == EfficiencyRatios.calculate_cash_conversion_cycle(234.67, 0, 0)

    def test_calculate_asset_turnover(self):
        assert 0.07 == EfficiencyRatios.calculate_asset_turnover(234.67, 3333)
        assert 58.962 == EfficiencyRatios.calculate_asset_turnover(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_asset_turnover(234.67, 0)

    def test_calculate_inventory_turnover(self):
        assert 0.07 == EfficiencyRatios.calculate_inventory_turnover(234.67, 3333)
        assert 58.962 == EfficiencyRatios.calculate_inventory_turnover(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_inventory_turnover(234.67, 0)

    def test_calculate_fixed_asset_turnover(self):
        assert 0.07 == EfficiencyRatios.calculate_fixed_asset_turnover(234.67, 3333)
        assert 58.962 == EfficiencyRatios.calculate_fixed_asset_turnover(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_fixed_asset_turnover(234.67, 0)

    def test_calculate_payables_turnover(self):
        assert 0.07 == EfficiencyRatios.calculate_payables_turnover(234.67, 3333)
        assert 58.962 == EfficiencyRatios.calculate_payables_turnover(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_payables_turnover(234.67, 0)

    def test_calculate_fcf_to_operating_cf(self):
        assert 0.07 == EfficiencyRatios.calculate_fcf_to_operating_cf(234.67, 3333)
        assert 58.962 == EfficiencyRatios.calculate_fcf_to_operating_cf(234.67, 3.98)
        assert 0 == EfficiencyRatios.calculate_fcf_to_operating_cf(234.67, 0)

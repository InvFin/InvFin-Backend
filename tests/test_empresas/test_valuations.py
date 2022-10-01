from apps.empresas.outils.valuations import discounted_cashflow


class TestValuation:
    def test_discounted_cashflow(self):
        assert 11.29 == discounted_cashflow(
            last_revenue=6464164,
            revenue_growth=13,
            net_income_margin=10.2,
            fcf_margin=22.5,
            buyback=5,
            average_shares_out=545678,
        )

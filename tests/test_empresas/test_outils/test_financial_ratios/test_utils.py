from src.empresas.outils.financial_ratios.utils import divide_or_zero, modify_for_percentage


def test_modify_for_percentage():
    assert 4 == modify_for_percentage(4, False)
    assert 4 == modify_for_percentage(0.04, True)
    assert 4 == modify_for_percentage(0.040001, True)


def test_divide_or_zero():
    assert 5 == divide_or_zero(25, 5)
    assert 0 == divide_or_zero(25, 0)
    assert 0 == divide_or_zero(0, 5)

    assert 5 == divide_or_zero(25.0, 5)
    assert 0 == divide_or_zero(25.0, 0)
    assert 0 == divide_or_zero(0, 5.0)

    assert 5 == divide_or_zero(25.0, 5.0)
    assert 0 == divide_or_zero(25.0, 0.0)
    assert 0 == divide_or_zero(0.0, 5.0)

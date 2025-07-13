import pytest

from src.widget import get_date

@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-01-01T00:00:00.000000", "01.01.2024"),  # первое января
        ("2024-12-31T23:59:59.999999", "31.12.2024"),  # последний день года
        ("2024-02-29T12:00:00.000000", "29.02.2024"),  # високосный год
        ("2020-02-29T12:00:00.000000", "29.02.2020"),  # другой високосный год
    ],
)
def test_get_date_boundary_values(date, expected):
    assert get_date(date) == expected


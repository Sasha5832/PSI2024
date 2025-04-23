from lab8.src.discount import calculate_discounted_price
import pytest

@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 0, 100.00),
        (100, 10, 90.00),
        (199.99, 25, 149.99),
        (250, 100, 0.00),
        (123.45, 7.5, 114.19),
        (99.999, 5, 95.00),
    ],
)
def test_calculate_discounted_price_valid(price, discount, expected):
    assert calculate_discounted_price(price, discount) == expected


@pytest.mark.parametrize("price", [-10, "100", None])
def test_invalid_price_raises_value_error(price):
    with pytest.raises(ValueError, match="Price must be a non-negative number"):
        calculate_discounted_price(price, 10)


@pytest.mark.parametrize("discount", [-1, 101, "5%", None])
def test_invalid_discount_raises_value_error(discount):
    with pytest.raises(ValueError, match="Discount must be a number between 0 and 100"):
        calculate_discounted_price(100, discount)


def test_rounding_to_two_decimals():
    price = 333.3333
    discount = 12.3456
    manual = round(price * (1 - discount / 100), 2)
    assert calculate_discounted_price(price, discount) == manual
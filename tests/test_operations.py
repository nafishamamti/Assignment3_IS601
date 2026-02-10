import pytest 
from typing import Union
from app.operations import Operations

Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 7, 12),
        (1, 1, 2),
        (-3, 2, -1),
        (1.5, 2.5, 4.0),
        (-1.5, 2.5, 1.0),
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 3, 5),
        (2, 2, 0),
        (-4, -3, -1),
        (12.5, 7.5, 5.0),
        (-8.5, -3.5, -5.0),
    ],
    ids=[
        "subtract_smaller_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (0, 8, 0),
        (-3, -4, 12),
        (2.5, 3.0, 7.5),
        (-2.5, 3.0, -7.5),
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 4, 2.0),
        (-8, -4, 2.0),
        (9.0, 3.0, 3.0),
        (-9.0, 3.0, -3.0),
        (0, 7, 0.0),
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b",
    [
        (5, 0),
        (-5, 0),
        (0, 0),
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero.") as excinfo:
        Operations.division(a, b)
    
    assert "Cannot divide by zero." in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero.', but got '{excinfo.value}'"


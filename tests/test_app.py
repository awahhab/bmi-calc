import pytest

from app import calculate_bmi


def test_calculate_bmi_normal_weight():
    result = calculate_bmi(70, 1.75)
    assert result == pytest.approx(22.8571428571, rel=1e-9)


def test_calculate_bmi_underweight():
    result = calculate_bmi(50, 1.8)
    assert result == pytest.approx(15.4320987654, rel=1e-9)


def test_calculate_bmi_invalid_values():
    assert calculate_bmi(0, 1.7) == "Height and weight must be greater than zero."
    assert calculate_bmi(-5, 1.7) == "Height and weight must be greater than zero."


def test_calculate_bmi_invalid_input():
    assert calculate_bmi("abc", "1.75") == "Please enter valid numbers for weight and height."

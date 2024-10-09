"""Test module for calculator operations."""
import pytest
from app.operation import addition, subtraction, multiplication, division


# Parameterized test for addition
@pytest.mark.parametrize("a, b, result", [
    (4, 1, 5),
    (10, 2, 12),
])
def test_addition(a, b, result):
    """Test Addition Function"""
    assert addition(a, b) == result

# Parameterized test for subtraction
@pytest.mark.parametrize("a, b, result", [
    (8, 3, 5),
    (10, 8, 2),
    (5, 3, 2),
])
def test_subtraction(a, b, result):
    """Test Subtraction Function"""
    assert subtraction(a, b) == result

# Parameterized test for multiplication
@pytest.mark.parametrize("a, b, result", [
    (3, 3, 9),
    (4, 5, 20),
])
def test_multiplication(a, b, result):
    """Test Multiplication Function"""
    assert multiplication(a, b) == result

# Parameterized test for division
@pytest.mark.parametrize("a, b, result", [
    (10, 2, 5),
    (25, 5, 5),
])
def test_division(a, b, result):
    """Test Division Function"""
    assert division(a, b) == result

# Test for division by zero
def test_division_by_zero():
    """Test Division by Zero Exception"""
    with pytest.raises(ValueError, match="Cannot divide by zero please provide valid number."):
        division(5, 0)

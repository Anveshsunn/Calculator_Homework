"""Test module for calculator operations."""
import pytest
from app.main import addition, subtraction, multiplication, division

def test_basic_addition():
    """Test Addition Function"""
    assert addition(4, 1) == 5

def test_basic_subtraction():
    """Test Subtraction Function"""
    assert subtraction(8, 3) == 5
    assert subtraction(10, 8) == 2

def test_basic_multiplication():
    """Test Multiplication Function"""
    assert multiplication(3, 3) == 9
    assert multiplication(4, 5) == 20

def test_basic_division():
    """Test Division Function"""
    assert division(10, 2) == 5
    assert division(25, 5) == 5

def test_division_by_zero():
    """Test Division by Zero Exception"""
    with pytest.raises(ValueError, match="Cannot divide by zero please provide valid number."):
        division(5, 0)

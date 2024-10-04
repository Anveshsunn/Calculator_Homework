'''My Calculator Test Add'''
from app.main import addition

def test_basic():
    '''Addition Funtion'''
    assert addition(4,1) == 5

'''My Calculator Test sub'''
from app.main import subtraction

def test_basic_subtraction():
    '''Sub Function'''
    assert subtraction(8, 3) == 5
    assert subtraction(10, 8) == 2

'''My Calculator Test Multi'''
from app.main import multiplication

def test_basic_multiplication():
    '''Multi Function'''
    assert multiplication(3, 3) == 9
    assert multiplication(4, 5) == 20

'''My Calculator Test Div'''
from app.main import division

def test_basic_division():
    '''Divi Function'''
    assert division(10, 2) == 5
    assert division(25, 5) == 5

# tests/test_main.py

import pytest
from app.main import division

def test_division_by_zero():
    '''Test division by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero you have entered the value as zero. Please provide a valid number to test."):
        division(5, 0)



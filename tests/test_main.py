'''My Calculator Test'''
from app.main import addition

def test_basic():
    '''Addition Funtion'''
    assert addition(1,1) == 2

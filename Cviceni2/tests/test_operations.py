from code.operations import *
import pytest
"""
def test_add():
    a = 5
    b = 10
    out = add(a,b)
    assert out == 15

def test_sub():
    a = 5
    b = 10
    out = sub(a,b)
    assert out == -5

def test_mul():
    a = 5
    b = 10
    out = mul(a,b)
    assert out == 50

def test_div():
    a = 5
    b = 10
    out = div(a,b)
    assert out == 1/2
"""

@pytest.mark.operation
@pytest.mark.parametrize("a,b,out", [
    (1,1,2),
    (1,5,6),
    (999,1,1000),
    (1,0,1),
    (0,0,0),
])
def test_add(a,b,out):
    assert add(a,b) == out
    
@pytest.mark.operation
def test_div_zerodiv_exception():
    a,b = 1,0
    with pytest.raises(ZeroDivisionError) as e:
        div(a,b)
    assert "division by zero" in str(e.value)    
    
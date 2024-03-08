import pytest
from code.calc import *

@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.calculator
def test_last_answer_after_init(calculator):
    assert calculator.ans == 0
    
    
@pytest.mark.calculator
@pytest.mark.parametrize("a,b,out", [
    (1,3,4), (2,3,5), (1,-3,-2),
])
def test_plus(calculator,a,b,out):
    assert calculator.plus(a,b) == out
    



@pytest.mark.calculator
def test_delete(calculator):
    calculator.plus(2,2)
    calculator.delete()
    assert calculator.ans == 0
    
    
@pytest.mark.calculator
@pytest.mark.parametrize("a,b,out", [
    (1,1,2), (69,69, "nice"), (420, 420, "time to get high"),
])
def test_specialek(calculator, a,b,out):
    assert calculator.specialek(a,b) == out
from code.operations import *

class Calculator:
    
    def __init__(self):
        self._ans = 0
    
    @property
    def ans(self) -> int:
        return self._ans
    
    def _operate(self, a, b, operator):
        self._ans = operator(a,b)
        return self._ans
    
    def plus(self, a, b):
        return self._operate(a, b, operator=add)
    
    def minus(self, a, b):
        return self._operate(a, b, operator=sub)
    
    def asterisk(self, a, b):
        return self._operate(a, b, operator=mul)
    
    def slash(self, a, b):
        return self._operate(a, b, operator=div)
    
    def delete(self):
        self._ans = 0
    
    def specialek(self, a,b):
        if a == b:
            if a == 69:
                return "nice"
            elif a == 420:
                return "time to get high"
        return a+b
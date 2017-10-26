import math


class MyFactorial:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self._numerator = numerator / gcd
        self._denominator = denominator / gcd

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def __sub__(self, other):
        return MyFactorial(1,4)



def test_my_factorial_initialization():
    f = MyFactorial(1,3)
    assert f.get_numerator() == 1
    assert f.get_denominator() == 3

def test_my_factorial_lowest_terms_on_initialization():
    f = MyFactorial(4, 8)
    assert f.get_numerator() == 1
    assert f.get_denominator() == 2

# def test_my_factorial_subtracting():
#     f1 = MyFactorial(3, 4)
#     f2 = MyFactorial(5, 10)
#     assert (f1 - f2) == MyFactorial(1,4)
# A primeira linha com a quantidade inicial de átomos N
# (de 2 a 1.000.000), a segunda linha com a quantidade resultante R.
import math

from sympy import Symbol, solve

# N = int(input())
# R = int(input())
"""
x = 1.72
days = 0
y = 0
"""


def calcule_x(x):
    return 2**x - 8


x = Symbol('x')
y = calcule_x(x)
resultado = solve(y)

print(resultado)
"""
while x > 1:
    x /= 20
    y += 1
    print(x, y)
    # x = (N / R)
    # days += 1
    """

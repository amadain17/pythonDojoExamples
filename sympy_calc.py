from sympy import *
from sympy.plotting import plot

init_printing(use_unicode=True)
x = symbols('x')
a = 12*x**2 + 9*x - 8
b = 4*x - 19 + 1
#print(solve(a-b))

#p1= plot(x*x*x)

#print(solve(x**3+ 3*x - 4))
print("\n\n\n")

pprint(diff(cos(x) / log(x**2)))
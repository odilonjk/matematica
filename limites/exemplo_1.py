# %%
from sympy import Symbol, Limit, init_printing


init_printing(use_latex=True)

x = Symbol('x')


def f(x):
    return (x**3 + x**2 + x)**101


def g(x):
    return (x**2 - (2 * x)) / (x + 1)

print('Considerando a função f(x)')
display(f(x))
print('\ne a função g(x)')
display(g(x))

limite_fx = Limit(f(x), x, -1)
limite_gx = Limit(g(x), x, 3)

print('\nCalcule o valor do seguinte limite:')
display(limite_fx - 4 * limite_gx)

print('\nResultado: {}'.format(limite_fx.doit() - (4 * limite_gx.doit())))

import numpy as np


a = np.array([3, 4])
b = np.array([-2, 5])

# O produto escalar de 'a' e 'b':
# a.b = 3.(-2) + 4.5 = -6+20 = 14

# Utilizando laço de repetição:
resultado = 0
for e, f in zip(a, b):
    resultado += e * f

# Resultado: 4
print('Produto escalar utilizando laço de repetição: {}'.format(resultado))

resultado = a * b
print('Multiplicação elementar dos vetores: {}'.format(resultado))

# Utilizando a multiplicação elementar seguida da soma dos produtos:
resultado = np.sum(a * b)
print('Produto escalar utilizando np.sum(a * b): {}'.format(resultado))

# Utilizando a função dot (dot function, pois em inglês produto escalar é mais conhecido como dot product):
resultado = np.dot(a, b)
print('Produto escalar utilizando dot function: {}'.format(resultado))

# Como a dot function é um método de instância, também é possível utilizar da seguinte maneira:
produto_escalar = a.dot(b)

# Calculando o ângulo formado entre 'a' e 'b'

# 1 - Calcular o comprimento (norma ou módulo) de 'a' e 'b'
modulo_a = np.linalg.norm(a)
modulo_b = np.linalg.norm(b)

# 2 - Calcular o cosseno do ângulo entre os dois vetores
cosseno_do_angulo = produto_escalar / (modulo_a * modulo_b)

# 3 - Calcular o ângulo entre os dois vetores utilizando a inversão do cosseno do ângulo
angulo = np.arccos(cosseno_do_angulo)
print('Ângulo entre os dois vetores: {}'.format(angulo))

# Resolvendo de uma forma resumida:
angulo = np.arccos(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b)))
print('Mesmo resultado: {}'.format(angulo))

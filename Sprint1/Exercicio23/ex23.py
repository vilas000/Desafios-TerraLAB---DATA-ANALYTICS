# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 1 - Exercício 23 (Separando dígitos de um número)

numero = int(input("Informe um número: "))

print("Analisando o número {}".format(numero))
print("Unidade: {}".format(numero // 1 % 10))
print("Dezena: {}".format(numero // 10 % 10))
print("Centena: {}".format(numero // 100 % 10))
print("Milhar: {}".format(numero // 1000 % 10))

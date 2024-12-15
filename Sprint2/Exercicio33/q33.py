# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 33 (Maior e menor valores)

valores = []

numero = int(input("Insira o primeiro valor: "))
valores.append(numero)
numero = int(input("Insira o segundo valor: "))
valores.append(numero)
numero = int(input("Insira o terceiro valor: "))
valores.append(numero)

print(f"O menor valor inserido foi: {min(valores)}")
print(f"O maior valor inserido foi: {max(valores)}")

# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 52 (Números primos)

numero = int(input("Digite um número: "))
contadorDivisibilidade = 1
valores = []
for i in range(1, numero // 2 + 1):
    if numero % i == 0:
        contadorDivisibilidade = contadorDivisibilidade + 1
        valores.append(i)
valores.append(numero)

print(f"O número {numero} foi divisível {contadorDivisibilidade} vezes. (pelos números {valores})")
if contadorDivisibilidade == 2:
    print("E por isso ele é PRIMO!")
else:
    print("Ele NÃO é um número primo.")
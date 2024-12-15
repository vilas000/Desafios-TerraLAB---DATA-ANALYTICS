# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 65 (Maior e Menor valores)
from numpy.ma.extras import average

valores = []
verifica = 'S'

while verifica not in 'N':
    numero = int(input("Digite um número: "))
    valores.append(numero)
    verifica = input("Quer continuar? [S/N] ").upper()

print(f"Você digitou {len(valores)} números e a média foi {average(valores)}")
print(f"O maior valor foi {max(valores)} e o menor foi {min(valores)}")
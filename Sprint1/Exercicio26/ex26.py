# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 1 - Exercício 26 (Primeira e última ocorrência de uma string)

frase = str(input("Digite uma frase: "))
frase = frase.strip().upper()
print("A letra 'A' aparece {} vezes na frase".format(frase.count('A')))
print("O primeiro 'A' aparece na posição {}.".format(frase.find('A') + 1))
print("O último 'A' aparece na posição {}.".format(frase.rfind('A') + 1))
# Posição inicial: 1

# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 53 (Detector de Palíndromo)

frase = input("Digite uma frase: ").upper()
frase = frase.replace(" ", "")

#Slicing
fraseInvertida = frase[::-1]

if frase == fraseInvertida:
    print("Temos um palíndromo!")
else:
    print("NÃO é um palíndromo!")


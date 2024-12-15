# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 78 (Maior e Menor valores na Lista)

valores = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a Posição {i}: ")))

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"Você digitou os valores {valores}")
print(f"O maior valor que você digitou foi {max(valores)} nas posições", end=" ")
for indice, valor in enumerate(valores):
    if valor == max(valores): print(indice, end='...')
print(end='\n')
print(f"O menor valor que você digitou foi {min(valores)} nas posições", end=" ")
for indice, valor in enumerate(valores):
    if valor == min(valores): print(indice, end='...')
print(end='\n')

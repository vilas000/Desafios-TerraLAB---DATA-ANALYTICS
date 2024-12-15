# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 84 (Lista composta e análise de dados)

verificador = 'S'
cont = 0

pessoa = {}
colecao = []

while verificador not in 'N':
    pessoa['nome'] = str(input("Nome: "))
    pessoa['peso'] = float(input("Peso: "))
    colecao.append(pessoa.copy())
    pessoa.clear()
    cont += 1
    verificador = str(input("Quer continuar? [S/N] ")).upper()

print("=-" * 20)
print(f"Ao todo, você cadastrou {cont} pessoas.")

#Encontrar o menor e o maior peso
maiorPeso = max(colecao, key=lambda p: p['peso'])['peso']
menorPeso = min(colecao, key=lambda p: p['peso'])['peso']

print(f"O maior peso foi de {maiorPeso}. Peso de ", end=" ")
for pessoa in colecao:
    if pessoa['peso'] == maiorPeso:
        print(pessoa['nome'], end="...")
print(end='\n')
print(f"O menor peso foi de {menorPeso}. Peso de ", end=" ")
for pessoa in colecao:
    if pessoa['peso'] == menorPeso:
        print(pessoa['nome'], end="...")
print(end='\n')
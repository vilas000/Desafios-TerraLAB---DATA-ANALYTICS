# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 94 (Somando dois números)

dado = {}
colecao = []
verificador = 'S'

while verificador not in 'N':
    dado["Nome"] = str(input("Nome: ")).strip()

    while True:
        dado["Sexo"] = str(input("Sexo [M/F]: ")).strip().upper()
        if dado["Sexo"] in ['M','F']:
            break
        print("ERRO! Por favor, digite apenas M ou F.")

    while True:
        try:
            dado["Idade"] = int(input("Idade: "))
            break
        except ValueError:
            print("ERRO! Insira um valor válido para a idade.")

    colecao.append(dado.copy())

    while True:
        verificador = str(input("Quer continuar? [S/N] ")).strip().upper()
        if verificador in ['S','N']:
            break
        print("ERRO! Por favor, digite apenas S ou N.")

print(f"A) Ao todo temos {len(colecao)} pessoas cadastradas.")

total = 0
for i in colecao:
    total += i["Idade"]
media = total / len(colecao)

print(f"B) A média de idade é de {media:.2f} anos.")

print(f"C) As mulheres cadastradas foram: ", end='')
for i in colecao:
    if i["Sexo"] == 'F': print(f"{i["Nome"]} ", end='')
print(end='\n')

print("D) Lista das pessoas que estão acima da média: ")
print(end='\n')
for i in colecao:
    if i["Idade"] > media: print(f"nome = {i["Nome"]}; sexo = {i["Sexo"]}; idade = {i["Idade"]};")
print("<< ENCERRADO >>")


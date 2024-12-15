# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 81 (Extraindo dados de uma Lista)

verificador = 'S'
valores = []

while verificador not in 'N':
    try:
        valor = float(input("Digite um valor: "))
        valores.append(valor)
        verificador =  str(input("Quer continuar? [S/N] ")).strip().upper()
    except ValueError:
        print("Por favor, insira um valor numérico válido!")

print("-=" * 20)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}.")
chave = 5
if chave in valores:
    print(f"O valor {chave} faz parte da lista!")
else:
    print(f"O valor {chave} NÃO faz parte da lista!")

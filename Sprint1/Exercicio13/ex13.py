# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 1 - Exercício 13 (Reajuste Salarial)

salInicial = float(input("Qual o salário do funcionário? R$"))
aumento = float(input("Insira o valor percentual de aumento do funcionário: "))
salFinal = salInicial * ((aumento / 100) + 1)
print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}".format(salInicial, aumento, salFinal))

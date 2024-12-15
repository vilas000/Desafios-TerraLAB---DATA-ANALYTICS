# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 38 (Comparando números)

# Tratamento de erro
def solicitar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor insira um valor numérico.")

numero1 = solicitar_numero("Digite o primeiro valor: ")
numero2 = solicitar_numero("Digite o segundo valor: ")

if numero1 > numero2:
    print("O PRIMEIRO valor é MAIOR")
elif numero1 < numero2:
    print("O SEGUNDO valor é MAIOR")
else:
    print("Os dois valores são IGUAIS")

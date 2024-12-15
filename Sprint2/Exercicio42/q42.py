# Gabriel Vilas Novas Sousa - 23.1.4018
# Sprint 2 - Exercício 42 (Analisando Triângulos v2.0)

def verificaTriangulo(lado1, lado2, lado3):
    if lado1 > lado2 + lado3:
        return False
    if lado2 > lado1 + lado3:
        return False
    if lado3 > lado1 + lado2:
        return False
    return True

lado1 = float(input("Primeiro segmento: "))
lado2 = float(input("Segundo segmento: "))
lado3 = float(input("Terceiro segmento: "))
verifica = verificaTriangulo(lado1, lado2, lado3)
if not verifica:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")
else:
    if lado1 == lado2 == lado3:
        print(" Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
    elif lado1 == lado2 or lado1 == lado2 or lado2 == lado3:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")


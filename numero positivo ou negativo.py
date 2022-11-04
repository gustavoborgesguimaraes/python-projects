#Encontrar o dobro de um número caso ele seja positivo
#e o seu triplo caso seja negativo, imprimindo o resultado.

numero = int(input('Digite um valor: '))

if numero > 0:
    resul = numero * 2
    print('O número é positivo, e o seu dobro é: ' + str(resul))
else:
    resul = numero * 3
    print('O número é negativo, e o seu triplo é: ' + str(resul))

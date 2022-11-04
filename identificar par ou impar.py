#Faça um algoritmo que leia uma variável e some 5 caso seja par
#ou some 8 caso seja ímpar, imprimir o resultado desta operação.

numero = int(input('Digite um valor: '))

if (numero%2) == 0:
    resul = numero + 5
    print('O número digitado é par, e seu valor somado com 5 é: ' + str(resul))
else:
    resul = numero + 8
    print('O número digitado é ímpar, e seu valor somado com 8 é: ' + str(resul))
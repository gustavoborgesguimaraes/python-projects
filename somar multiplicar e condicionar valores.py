#Faça um algoritmo que leia dois valores inteiros A e B
#se os valores forem iguais deverá se somar os dois
#caso contrário multiplique A por B
#Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C
#e mostrar seu conteúdo na tela. 
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))

if (a == b):
    c = a+b
    print('Os valores de A e B são iguais, logo A+B é: ' + str(c))
else:
    c = a*b
    print('Os valores de A e B são diferentes, logo A*B é: ' + str(c))
    

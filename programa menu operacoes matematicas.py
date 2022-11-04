#Faça um programa, utilizando estrutura de condição, que receba um número real,
#digitado pelo usuário e mostre o menu para selecionar o tipo de cálculo
#que deve ser realizado com base nos códigos abaixo:
import math

valor = float(input('Digite um número real:'))
print('Qual operação você deseja realizar com o númro digitado?')
print('   101 -> Raiz quadrada')
print('   102 -> A metade')
print('   103 -> 10% do número')
print('   104 -> O dobro')
opc_menu = int(input(''))

#Raiz quadrada
if (opc_menu == 101):
    val_calc = math.sqrt(valor)
    print('A raiz quadrada é: ' + str(val_calc))

#A metade
if (opc_menu == 102):
    val_calc = valor/2
    print('A metade do valor é: ' + str(val_calc))

#10% do número
if (opc_menu == 103):
    val_calc = valor*(10/100)
    print('10% do valor é: ' + str(val_calc))

#O dobro
if (opc_menu == 104):
    val_calc = valor*2
    print('O dobro do valor é: ' + str(val_calc))
    
    
    
    

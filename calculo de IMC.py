#Elabore um algoritmo que leia o peso e a altura de um adulto
#e mostre sua condição de acordo com a tabela de IMC

peso = int(input('Qual é seu peso?'))
altura = float(input('Qual é sua altura'))

IMC = peso/(altura*2)

print('Seu IMC é: ' + str(IMC))

#Até 18,5 -> Abaixo do peso.
if (IMC < 18.5) : 
    print('...e você está abaixo do peso.')
#Entre 18,5 e 25 -> Peso normal.
if ((IMC >= 18.5) and (IMC < 25)) : 
    print('...e você está com peso normal.')
#Entre 25 e 30 -> Acima do peso.
if ((IMC >= 25) and (IMC < 30)) :
    print('...e você está acima do peso.')
# Acima de 30 -> Obeso.
if (IMC >= 30) :
    print('...e você está obeso.')

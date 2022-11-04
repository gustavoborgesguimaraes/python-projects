#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input('Digite o seu nome: ')
sexo = input('Informe seu sexo ["M" ou "F"]: ')
est_civ = input('Qual eu estado civil? ["SOLTEIRO" ou "CASADO"]')

if (sexo == 'F') and (est_civ == 'CASADO'):
    tempo_de_casado = input('Quantos anos você tem de casada?')
    print('A ' + str(nome) + ' tem '+ str(tempo_de_casado) + ' de casada.')

print('OK, muito obrigado pela participação da pesquisa.')
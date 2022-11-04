#Escrever um programa que leia 3 valores A, B e C, e os escreva em ordem crescente.
lista = []
qtdvalores = 3

for i in range(qtdvalores):
    elemento = int(input('Digite o valor ' + str(i+1) + ':'))
    lista.append(elemento)
    lista.sort(reverse = False)
    
print("A ordem crescente dos valores é: " + str(lista))
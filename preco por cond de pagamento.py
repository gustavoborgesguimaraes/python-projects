#Sistema que retrona o que deve ser pago por um produto,
#considerando o preço normal de etiqueta e a escolha da condição de pagamento.

preco_etiqueta = float(input('Qual o preço da etiqueta?'))
print('Qual a condição de pagamento?')
print('   1 : À vista em dinheiro ou cheque.')
print('   2 : À vista no cartão de crédito.')
print('   3 : Em duas vezes.')
print('   4 : Em mais de duas vezes.')
cond_pagam = int(input(''))

#À vista em dinheiro ou cheque, recebe 10% de desconto
if (cond_pagam == 1) :
    val_calc = preco_etiqueta * 0.90
    print('Você selecionou a opção [1], e terá 10% de desconto')
    print('O valor pago pelo produto será de: R$' + str(val_calc))
    
#À vista no cartão de crédito, recebe 15% de desconto
if (cond_pagam == 2) :
    val_calc = preco_etiqueta * 0.85
    print('Você selecionou a opção [2], e terá 15% de desconto')
    print('O valor pago pelo produto será de: R$' + str(val_calc))

#Em duas vezes, preço normal de etiqueta sem juros
if (cond_pagam == 3) :
    val_calc = preco_etiqueta * 1
    print('Você selecionou a opção [3], e terá preço normal de etiqueta sem juros')
    print('O valor pago pelo produto será de: R$' + str(val_calc))
    
#Em mais de duas vezes, preço normal de etiqueta mais juros de 10%
if (cond_pagam == 4) :
    val_calc = preco_etiqueta * 1.1
    print('Você selecionou a opção [4], e terá preço normal acrescido juros de 10%')
    print('O valor pago pelo produto será de: R$' + str(val_calc))    
    
    
    
    
    
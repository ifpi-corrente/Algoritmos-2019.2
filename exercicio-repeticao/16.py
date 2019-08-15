# -*- coding: utf-8 -*-
# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

soma = 0 
a1 = 1
a2 = 0
while soma < 500:
    #print("{}, ".format(soma), end="")
    print(f'{soma}, ', end="")
    a2 = a1
    a1 = soma
    soma = a1 + a2
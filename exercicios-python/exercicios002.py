# Desafio 006
#   Crie um algoritmo que leia um numero e mostre
#   o seu dobro, triplo e raiz quadrada


num = int(input('Escreva um número: '))
print()
print()
antes = num - 1
depois = num + 1
raiz = num ** (1/2)
dobro = num * 2
triplo = num * 3
print('Escolheu o número: {}'.format(num))
print('O seu dobro é: {}'.format(dobro))
print('O seu triplo é: {}'.format(triplo))
print('A sua raíz quadrada é: {}'.format(raiz))
print('O seu antecessor é {} e o sucessor é {}'.format(antes, depois))
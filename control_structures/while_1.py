# while True: 
#     print('Laço infinito')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9) #gerará um número entre esse intervalo

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
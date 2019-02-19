lista_numeros = []
#contador = 0
#maior_valor = 0
#menor_valor = 0
novo_valor = True

while novo_valor:
    numero = int(input('Qual o valor? '))
    lista_numeros.append(numero)
    flag = input('Continua (y/n)? ')
    if flag != 'y':
        novo_valor = False

print(lista_numeros)
print('O maior valor é: ', max(lista_numeros)) #métodos max e min 
print('O menor valor é: ', min(lista_numeros))
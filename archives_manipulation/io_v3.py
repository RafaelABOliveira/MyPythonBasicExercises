#!/usr/local/bin/python3

try:
    arquivo = open('D:\Users\User\Desktop\mypythonbasicexercises\archives_manipulation\pessoas.csv')
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.split(',')), end='')
except IndexError:
    pass
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')

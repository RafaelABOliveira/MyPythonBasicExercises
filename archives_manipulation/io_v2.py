#!/usr/local/bin/python3
arquivo = open('D:\Users\User\Desktop\mypythonbasicexercises\archives_manipulation\pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')), end='')
arquivo.close()
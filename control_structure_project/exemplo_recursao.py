def imprimir(maximo, atual):
    # if atual >= maximo:
    if atual < maximo:
        print(atual)
    imprimir(maximo, atual +1)

imprimir(990, 1)
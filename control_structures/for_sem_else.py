PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:

    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui palavra proibida: ', palavra)
            break
    else:
        print('Texto autorizado:', texto)

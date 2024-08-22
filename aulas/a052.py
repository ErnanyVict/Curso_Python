''' split e join com list e str
split - divide uma string
join - une uma string'''

frase = '   Ola só que, coisa interessante   '
lista_palavras = frase.split(', ')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].rstrip().lstrip())
print(lista_palavras)

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)
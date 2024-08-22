'''Dicinarios em Python (tipo dict) 
par de chave e valor
chave = índice'''
pessoa1 = dict(nome= 'Ernany', sobrenome= 'Victor')
pessoa2 = {
    'nome': 'Lucas',
    'sobrenome': 'Pareschi',
    'idade': 14,
    'parentes': [
        {'pai': 'Jonas'},
        {'mae': 'Lene'}
    ]
}

print(pessoa2, type(pessoa2))
print(pessoa2['idade'])
for chave in pessoa2:
    print(f'{chave}: {pessoa2[chave]}')
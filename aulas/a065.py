# Manipulando chaves e  valores em dicionarios

pessoa = {}

pessoa['nome'] = 'Ernany'
pessoa['sobrenome'] = 'Victor'
lista = []
chave2 = 'idade'
pessoa[chave2] = 15

print(pessoa)
del pessoa['sobrenome']

if pessoa.get('sobrenome') is not None:
    print('Existe')
else:
    print('Não existe')
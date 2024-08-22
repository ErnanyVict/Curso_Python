pessoa1 = {
    'nome': 'Ernany',
    'sobrenome': 'Victor',
    'Idade': 15
}

antigo_nome = pessoa1.pop('nome')
print(antigo_nome)
print(pessoa1)
atualizacao = [['nome', 'Ernany'], ['sobrenome', 'Lindão']]
pessoa1.update(atualizacao)
print(pessoa1)
print(pessoa1.popitem())
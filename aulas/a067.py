import copy

pessoa1 = {
    'nome': 'Ernany',
    'sobrenome': ['Victor', 'Fernandes', 'Furtunato'],
    'idade': 15
}

pessoa2 = pessoa1.copy() # shallow copy
pessoa2 = copy.deepcopy(pessoa1)
print(pessoa2)
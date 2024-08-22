# Métodos úteis dos dicionários

pessoa  = {
    'nome': 'Ernany',
    'sobrenome': 'Victor', 
    'sobrenome2': 'Fernandes'
}
print(pessoa.__len__()) # lê quantas chaves têm
print(len(pessoa))
print(list(pessoa.keys())) # Retorna as chaves
print(list(pessoa.values())) # Retorna os valores
print(list(pessoa.items())) # Retorna as chaves e os valores
pessoa.setdefault('idade', 15)
print(pessoa['idade'])
# Função lambda em python

lista = [
    {'Nome': 'Ernany', 'Sobrenome': 'Victor'},
    {'Nome': 'Carlos', 'Sobrenome': 'Alberto'},
    {'Nome': 'Maria', 'Sobrenome': 'Yvone'}
]

def exibir(lista):
    for item in lista:
        print(item)
    print()
    
l1 = sorted(lista, key=lambda item: item['Nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])

exibir(l1)
exibir(l2)
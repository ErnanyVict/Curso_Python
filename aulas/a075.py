# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteraveis
import pprint


lista = []

lista = [
    numero * 2
    for numero in range(10)
]
#print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_precos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

#print(*novos_precos, sep='\n')
def p(v): 
    pprint.pprint(v, sort_dicts=False, width=70)

#p(novos_precos)

lista = [n for n in range(10) if n < 5] #filtro
print(lista)
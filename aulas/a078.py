# isinstance - para saber se o objeto é de determinado tipo

#Valores Falsy e Truthy
# Mutáveis [] {} set() -- Falsy
# Imutáveis () "" 0 0.0 None False range(0) -- Falsy


lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))
        
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
        
    else:
        print('Outro')
        print(item)
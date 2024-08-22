# enumerate - enumera iteráveis (índices)

lista = ['Maria', 'Helena', 'Ana']
lista.append('João')

lista_enumerada = list(enumerate(lista, start= 19))
#print(lista_enumerada)

for indice, nome in lista_enumerada:
    print(indice, nome)

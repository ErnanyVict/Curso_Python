lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(70)
print(lista)
lista.pop()
print(lista)
ultimo_valor = lista.pop(0)
print(lista, "Ultimo valor:", ultimo_valor)
lista.insert(2, 30)
print(lista)
lista.clear()
print(lista)
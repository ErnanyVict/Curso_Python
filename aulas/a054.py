'''string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

for nome in lista:    
    ...
print(*lista)
print(*string)
'''

salas = [
    ['ANA' , 'Maria'],
    ['Elaine'],
    'Joana',
    (10, 20, 30, 40)
]
print(*salas, end= ' ')
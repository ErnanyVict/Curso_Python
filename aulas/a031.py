''' Flag (Bandeira) - marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade'''

v1 = 'A'
v2 = 'B'
print(id(v1))
print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True # flag
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
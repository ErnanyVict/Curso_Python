''' interpolação  básica de string
s - strings
d e i - int
f - float
x e X - hexadecimal
'''

nome = 'Ernany'
preco = 100.0122
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print("O hexadecimal de %i é %02x" % (15, 15))
'''
Operadores de atribuição
= += -= *= /= //= **= %= 
'''

linha = 0
qtd_linha = 5
qtd_coluna = 5

while linha < qtd_linha:
    linha += 1
    coluna = 1
    while coluna <= qtd_coluna:     
        print(f'{linha} {coluna}')
        coluna += 1
print("Acabou")
'''
Operadores de atribuição
= += -= *= /= //= **= %= 
'''

linha = 0
qtd_linha = 5

while linha < qtd_linha:
    linha += 1
   
    if linha == 40:
        break
    if linha > 10 and linha <20:
        continue
    print(linha)
    
print("Acabou")
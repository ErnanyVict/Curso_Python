frase = input("Frase: ")

i = 0
letra_mais_apareceu = ''
qtd_letra_mais_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_apareceu = frase.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_mais_apareceu < qtd_vezes_apareceu:
        letra_mais_pareceu = letra_atual
        qtd_letra_mais_apareceu = qtd_vezes_apareceu        
    i += 1
print(f'A letra {letra_mais_pareceu!r} foi a letra que mais apareceu, aparecendo {qtd_letra_mais_apareceu} vezes')
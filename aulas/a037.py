''' while/else '''

string = 'Valorqualquer'
i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
    if ' ' in string:
        break
else:
    print('O else foi executado')
print('fora do while')
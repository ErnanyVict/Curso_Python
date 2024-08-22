''' Formatação básica de Strings
'''

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{10.212021020:0>+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:05x}')
print(f'{variavel!r}')
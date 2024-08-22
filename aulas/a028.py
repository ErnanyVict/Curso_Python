''' Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar'''

try:
    n_str = input("Vou dobrar o número que você digitar: ")
    n_float = float(n_str)
    if n_str.isdigit():
        print(f'O dobro de {n_str} é {n_float * 2:.2f}')
except:
        print("Isso não é um número")
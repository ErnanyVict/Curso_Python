#Empacotamento e desempacotamento  de dicionários

'''(a1, a2), (b1, b2) = pessoa.items()

print(a1, a2)
print(b1, b2)'''

pessoa = {
    'Nome': 'Maria',
    'Sobrenome': 'Yvone'
}

dados_pessoa = {
    'idade': 1000,
    'altura': 1.5
}

pessoa_completa = {**pessoa, **dados_pessoa, 'Sobrenome2': 'Fernandes'}
print(pessoa_completa)

#kwargs - keywords arguments (argumentos nomeados)

def argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
        
argumentos_nomeados('lala', fruta="banana", verdura='Alface')

argumentos_nomeados(**pessoa_completa)
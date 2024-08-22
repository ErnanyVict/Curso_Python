# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

nomes = ['Ernany', 'Elaine', 'Beto', 'Juninho']
for nome in nomes:
    dar_bom_dia = criar_saudacao('Bom dia')
    dar_boa_noite = criar_saudacao('Boa noite')
    print(dar_bom_dia(nome))
    print(dar_boa_noite(nome))
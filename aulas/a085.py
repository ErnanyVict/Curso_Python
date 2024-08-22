# raise - lançando erros

'''def divide (n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print("Salvar erro")
        raise'''
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você não pode dividir por zero")
    
def int_or_float(d):
    if not isinstance(d, (int, float)):
        raise TypeError(f'{d} dever ser int ou float')
        
def divide (n, d):
    int_or_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(7 , '0'))
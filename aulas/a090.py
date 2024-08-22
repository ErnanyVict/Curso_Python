#Decoradores com parametros 

def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da execução da função.")
        resultado = func(*args, **kwargs)
        print("Depois da execução da função.")
        return resultado
    return wrapper

@decorador
def saudacao(string):
    return string

print(saudacao(1))
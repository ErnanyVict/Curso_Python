# Try, except, else, e finally

a = 'a'
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("Dividiu por zero.")
except (NameError, TypeError):
    print("Variavel não está definida")
except Exception:
    print("Erro desconhecido")    
print('Continuar')
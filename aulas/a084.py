# try, except, finally e else

try:
    print("Abrir arquivo")
    0/2
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print("Dividiu por zero")
else:
    print("Nao deu erro")
finally:
    print("Fechar arquivo")
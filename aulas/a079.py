# dir, hasattr, getattr em Python

string = "Ernany"
metodo = 'upper'
print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print("Esse método não existe nesse objeto")
''' Valores padrão para parâmetros
refatorar: editar o seu código'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} {x + y + z}')
    else:
        print(f'{x=} {y=} {x + y}')

soma(1, 2)
soma(3, 5, 5)
soma(100, 400)
soma(z=0, y=2, x=1)







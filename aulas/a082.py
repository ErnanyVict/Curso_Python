#Yield from

def gen1():
    print("Começou gen1")
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')
    
def gen2(gen):
    print("Começou gen2")
    yield from gen()
    yield 2
    yield 3
    print('Acabou gen2')
    
g1 = gen2(gen1)   
    
for n in g1:
    print(n)
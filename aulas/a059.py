# escopo de funções em python
# escopo siginifca o local onde aquele código pode atingir
# o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
# o escopo global é o escopo onde todo escopo pode acessar.

x = 10 

def escopo():
    global x
    x = 1
    def outra_funcao():
        y = 2
        global x
        x = 100
        print(x, y)
    outra_funcao()    

print(x)
escopo()
print(x)

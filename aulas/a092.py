# Combinations, Permutations, e Product - itertools

from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n')

pessoas = ['Joao', 'Joana', 'Luiz', 'Leticia']
camisetas = [['preto', 'braco'], ['p', 'm'], ['masc.', 'fem.']]

#print_iter(combinations(pessoas, 3))
#print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))


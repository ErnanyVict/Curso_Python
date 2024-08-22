# in (contém)
# not in (não contém)
# Strings são iteráveis

nome = "Ernany"
print(nome[0])
print(nome[-4])
print("rna" in nome)
print("rna" not in nome)

nome = input("Digite seu nome:")
encontrar = input("Digite o que deseja encontrar:")
if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
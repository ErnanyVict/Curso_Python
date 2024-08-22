for i in range(1, 10):
    if i == 2:
        print('Pulando o 2...')
        continue
    if i == 4:
        break
    for j in range(1, 4):
        print(i, j)


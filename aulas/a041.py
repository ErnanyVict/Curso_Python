texto = iter('Ernany')

while True:
    try:
        print(texto.__next__())
    except StopIteration:
        break
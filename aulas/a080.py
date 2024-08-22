# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
print(next(iterator))
generator = (n for n in range(100))
print(generator)

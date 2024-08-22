# count é um iterator sem fim

from itertools import count

c1 = count(1, 8)
c2 = range(1, 100, 8)

print('Count')
for i in c1:
    print(i)
    if(i >= 100):
        break

print('Range')
for i in c2:
    print(i)

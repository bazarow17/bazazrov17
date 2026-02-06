'''
j = 0
a = int(input(''))
if a == 1:
    n = int(input())
    b = list(map(int, input().split()))
elif a == 0:

    n = random.randint(1, 12)
    b = [random.randint(0, 99) for _ in range(n)]
d = b.copy()
for _ in range(len(b)):
    c = max(d)
    del b[b.index(c)]
    del d[d.index(c)]
    b.append(c)
    j=j+1
print(b, j)



import random
a = int(input(''))
if a == 1:
    n = int(input())
    b = list(map(int, input().split()))
elif a == 0:

    n = random.randint(1, 12)
    b = [random.randint(0, 99) for _ in range(n)]
d = b.copy()

b.sort()
print(b)





import random
a = int(input(''))
if a == 1:
    n = int(input())
    b = list(map(int, input().split()))
elif a == 0:

    n = random.randint(1, 12)
    b = [random.randint(0, 99) for _ in range(n)]
d = b.copy()
for i in range(len(b)-1):
    if b[i]>b[i+1]:
    j=j+1
        b[i], b[i+1] = b[i+1], b[i]
print(b, j)
'''

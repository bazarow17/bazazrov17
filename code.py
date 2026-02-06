'''
спрашиваем у пользователя по поводу режима
запришиваем или создаем на рандом массив для работы
повторяем действие n(длина массива) раз 
   ищем максимальный элемент
   удаляем его из массива
   вставляем его в конец массива
import random
j = 0
a = int(input(''))
d = []
if a == 1:
    b = list(map(int, input().split()))
elif a == 0:
    n = random.randint(1, 12)
    b = [random.randint(0, 99) for _ in range(n)]
k = 0
for i in range(len(b)):
    c = max(b)
    del b[b.index(c)]
    d.insert(k+i, c)
    j=j+1
print(d, j)


'''

'''
спрашиваем у пользователя по поводу режима
запришиваем или создаем на рандом массив для работы
повторяем действие n(длина массива) раз 
   ищем максимальный элемент
   удаляем его из массива
   вставляем его в конец массива
j = 0
a = int(input(''))
if a == 1:
    n = int(input())
    b = list(map(int, input().split()))
elif a == 0:

    n = random.randint(1, 12)
    b = [random.randint(0, 99) for _ in range(n)]
for _ in range(len(b)):
    c = max(d)
    del b[b.index(c)]
    d.append(c)
    j=j+1
print(d, j)




'''

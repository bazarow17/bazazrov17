'''
спрашиваем у пользователя по поводу режима
запришиваем или создаем на рандом массив для работы
повторяем действие n(длина массива) раз 
   ищем максимальный и минимальный элемент
   удаляем их из массива
   вставляем их в конец и начало нового массива

import random
print('интерактивный режим-1')
print('автономный режим-0')
schetchik = 0
rejim = int(input(''))
otv = []
if rejim == 1:
    spisok = list(map(int, input().split()))
elif rejim == 0:
    n = random.randint(1, 12)
    spisok = [random.randint(0, 99) for _ in range(n)]
ishod_spisok = spisok.copy()
for i in range(len(spisok)//2):
    minlist = min(spisok)
    if len(spisok)>=2:
        maxlist = max(spisok)
        del spisok[spisok.index(minlist)]
        otv.insert(i, minlist)
    del spisok[spisok.index(maxlist)]
    otv.insert(len(otv)-i, maxlist)
    schetchik+=1
print('исходный список-', ishod_spisok)
print('отсортированный список-', otv)
print('кол-во перестановок', schetchik)





спрашиваем у пользователя по поводу режима
запришиваем или создаем на рандом массив для работы
повторяем действие n(длина массива) раз 
   ищем максимальный элемент
   удаляем его из массива
   вставляем его в конец массива
import random
print('интерактивный режим-1')
print('автономный режим-0')
schetchik = 0
rejim = int(input(''))
otv = []
if rejim == 1:
    spisok = list(map(int, input().split()))
elif rejim == 0:
    n = random.randint(1, 12)
    spisok = [random.randint(0, 99) for _ in range(n)]
ishod_spisok = spisok.copy()
for i in range(len(spisok)):
    minlist = max(spisok)
    del spisok[spisok.index(minlist)]
    otv.insert(i, minlist)
    schetchik=schetchik+1
print('исходный список-', ishod_spisok)
print('отсортированный список-', otv)
print('кол-во перестановок', schetchik)



спрашиваем у пользователя по поводу режима
запришиваем или создаем на рандом массив для работы
повторяем действие n(длина массива) раз 
   сравниваем попарно элементов
   меняем местами больший и меньший
import random
print('интерактивный режим-1')
print('автономный режим-0')
schetchik = 0
regim = int(input(''))
if regim == 1:
   spisok = list(map(int, input().split()))
elif regim == 0:
   n = random.randint(1, 12)
   spisok = [random.randint(0, 99) for _ in range(n)]
ishod_spisok = spisok.copy()
for i in range(len(spisok)):
   for j in range(i+1, len(spisok)):
      if spisok[i]>spisok[j]:
         spisok[i], spisok[j] = spisok[j], spisok[i]
         schetchik+=1
print('исходный список-', ishod_spisok)
print('отсортированный список-', spisok)
print('кол-во перестановок', schetchik)



'''

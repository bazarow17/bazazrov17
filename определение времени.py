def chasu(chas):
    if chas > 12:
        chas = chas-12
    if chas == 1:
        return 'час'
    elif chas > 1 and chas <5:
        return 'часа'
    else:
        return 'часов'
def minutu(minut):
    if minut%10 == 0 and minut != 0 or minut >=10 and minut<=20:
        return 'минут'
    elif minut == 0:
        return 'ровно' 
    else:
        if minut%10 == 1:
            return 'минута'
        elif minut%10 >1 and minut%10<5:
            return 'минуты'
        else:
            return 'минут'
        
def vremyadnya(chas):
    if chas >= 0 and chas < 6:
        return 'ночи'
    elif chas >= 6 and chas < 12:
        return 'утра'
    elif chas >= 12 and chas <18:
        return 'дня'
    elif chas >=18 and chas<24:
        return 'вечера' 
vremya = input().split()
if vremya[0][0] != '-' and vremya[1][0] != '-':
    vremya = list(map(int, vremya))
    print(vremya)
    if vremya[0]<24 and vremya[0]>=0 and vremya[1]<60 and vremya[1]>=0  :
        if vremya[0] == 0 and vremya[1] == 0:
            print('полночь')
        elif vremya[0] == 12 and vremya[1] == 0:
            print('полдень')
        else:
            if vremya[1] == 0:
                if vremya[0] > 12:
                    print(vremya[0]-12, chasu(vremya[0]), vremyadnya(vremya[0]), minutu(vremya[1]), end=' ')
                else:
                    print(vremya[0], chasu(vremya[0]), vremyadnya(vremya[0]), minutu(vremya[1]), end=' ')
            else:
                if vremya[0] > 12:
                    print(vremya[0]-12, chasu(vremya[0]), vremya[1], minutu(vremya[1]), vremyadnya(vremya[0]), end=' ')
                else:
                    print(vremya[0], chasu(vremya[0]), vremya[1], minutu(vremya[1]), vremyadnya(vremya[0]), end=' ')
    else:
        if vremya[0] >=24:
            print('вводи норамльные данные(час должен быть от 0 до 23)')
        elif vremya[0] >=60:
            print('вводи норамльные данные(минута должна быть от 0 до 59)')
else:
    print('время должно быть положительным')

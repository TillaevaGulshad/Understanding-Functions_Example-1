# Функциянын максималдуу элементин табуу.
# Берилген эки озгормо анын элементтери болот
def max(x, y):
    if x > y:
        return " х озгормосунун мааниси у озгормосунон чон "
    else:
        return " y озгормосунун мааниси х озгормосунон чон "

res=max(int(input('x озгормосунун маанисин киргиз')), int(input('y озгормосунун маанисин киргиз')))
print(res)


#  Киргизилген 3 сандын максимум табуу
def max_1(a,b,c):
    if a>b:
        if a>c:
            max_=a
            return max_
        elif b>c:
            max_=b
            return max_
        else:
            max_=c
            return max_
print('Киргизилген 3 сандын максимуму = ',max_1(int(input('а маанисин киргиз :')), int(input('в маанисин киргиз :')), int(input('с маанисин киргиз :'))))


# II variant
def can(a,b,c,d):
    maxsim = max(a, b, c, d)
    minimum = min(a, b, c, d)
    return maxsim, minimum

a,b,c,d=map(int, input('Боштук менен ажыратылган 4 санды киргиз').split(','))
ma,mi=can(a,b,c,d)
print('4 canlin max=', ma,'\n ','4 candi min=',mi)
#jiuintik=can(int(input('a maanicin kirgis')), int(input('b maanicin kirgis')), int(input('c maanicin kirgis')), int(input('d maanicin kirgis')))
# print(jiuintik)
print(' 4 candin max= ',ma)
print(' 4 candin max= ',mi)

# мисалдын берилиши: Тизмени сорттоо.
# Берилген тизменин элементтерин жуп сандарын сорттоп андан сон так сандарды сорттоп кошуп чыгаргыла
# numbers =[8,3,5,2,10]

# Туура чыгарылышы

numbers=list(map(int, input('ведите число через пробелы:').split()))
result_1=sorted([i for i in numbers if i%2==0], reverse=True)
result_2=sorted([i for i in numbers if i%2!=0])
print(result_1 + result_2)



# туура чыкты
# мисалдын берилиши: Тизмени функциянын жардамында сорттоо.
# Берилген тизменин элементтерин жуп сандарын сорттоп андан сон так сандарды сорттоп кошуп чыгаргыла
# numbers =[8,3,5,2,10]

def func(numbers):
    result_1 = sorted([i for i in numbers if i % 2 == 0], reverse=True)
    result_2=sorted([i for i in numbers if i%2!=0])
    return result_1 +result_2
result=func(
        list(map(int, input('Пробелден сон санды киргиз: ').split()))
    )
print('Жыйынтык: ',result)



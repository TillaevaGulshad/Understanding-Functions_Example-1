# Функция — бул белгилүү бир тапшырманы аткаруучу коддун блогу. Аны бир нече
# жолу чакырып колдонсо болот. Бул кодду кайра-кайра жазбай, "бир жолу жазып — көп жолу колдонууга"
# мүмкүнчүлүк берет.
# def функциянын_аты(параметрлер):
#     # Функциянын ичиндеги код
#     return жыйынтык

# Мисал 1
def koshuu(a, b):
    return a + b

natija = koshuu(3, 5)
print(natija)  # Натыйжасы: 8
# Мисал 2

# Функцияны пайдаланып calculator эсептегиле.  мисал акырына чейин чыкты
def calculator(a,b,operation):
    if operation=='+':
        return a+b
    elif operation=='-':
        return a-b
result=calculator(int(input("Первое число:")), int(input("Второе число:")), input("Что делать:"))
print(result)


# туура чыкты
#
def add(a,b):
    c=a+b
    return c
rejultat=add(5,6)
print(rejultat)


# Эки сандын суммасы
# туура чыкты
def add(a,b):
    return a+b
print('Резултат от функции: ', add(5, 4))

# туура чыкты 2-варианты

def add(a,b):
    c=a+b
    return c
rejultat=add(5,6)
print('a жана в эки сандын суммасы = ',rejultat)

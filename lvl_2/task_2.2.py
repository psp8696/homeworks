# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

months = [
    ['январь', 1],
    ['февраль', 2], 
    ['март', 3],
    ['апрель', 4], 
    ['май', 5],
    ['июнь', 6],
    ['июль', 7],
    ['август', 8],
    ['сентярь', 9],
    ['октябрь', 10],
    ['ноябрь', 11],
    ['декабрь', 12],
    ]


def quarter_of():
    x = int(input('Введите номер месяца: '))
    if x in [1,2,3]:
        print(f'месяц {x} ({months[x-1][0]}) является частью первого квартала')
    elif x in [4,5,6]:
        print(f'месяц {x} ({months[x-1][0]}) является частью второго квартала')
    elif x in [7,8,9]:
        print(f'месяц {x} ({months[x-1][0]}) является частью третьего квартала')
    elif x in [10,11,12]:
        print(f'месяц {x} ({months[x-1][0]}) является частью четвертого квартала')
    else:
        print('Такого месяца нет')


quarter_of()

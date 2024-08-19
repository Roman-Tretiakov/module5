def add_everything_up(a, b):
    try:
        a + b
    except TypeError as err:
        print(f'Возникла ошибка: {err}. Тип первого аргумента: {type(a)}, тип второго аргумента: {type(b)}')
        return f'{str(a)}{str(b)}\n'
    else:
        return round(a + b, 3)
    finally:
        if type(a) is int and type(b) is str:
            print(f'Эта функция может также складывать числа и строки, результат: {a + len(b)}')
        elif type(a) is str and type(b) is int:
            print(f'Эта функция может также складывать строки и числа, результат: {len(a) + b}')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123, 7))
print(add_everything_up(123, 'строка'))

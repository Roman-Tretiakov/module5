def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        div = 2

        while div < result and result % div != 0:
            div += 1
        if div == result:
            print('Простое')
        else:
            print('Состовное')
        return result
    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return sum([num1, num2, num3])


result = sum_three(2, 3, 6)
print(result)

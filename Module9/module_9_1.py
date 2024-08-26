numbers = ['10', -1, '0', 100, 73, '-99', 5]


def apply_all_func(int_list, *functions):
    int_list = [int(el) if type(el) is str else el for el in int_list]
    dictionary = {}

    for func in functions:
        dictionary[func.__name__] = func(int_list)

    return dictionary


print(apply_all_func(numbers, min, max, len, sum, sorted))
class IncorrectVinNumber(Exception):
    def __init__(self, message, info):
        self.message = message
        self.additional_info = info


class IncorrectCarNumbers(Exception):
    def __init__(self, message, info):
        self.message = message
        self.additional_info = info


class Car:
    def __init__(self, model, vin_number, number):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(number):
            self.__number = number

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers(f'{self.model} - Invalid number type. ', f'Type is: {type(number)}, required: {str}.')
        if len(number) != 6:
            raise IncorrectCarNumbers(f'{self.model} - Invalid number length. ', f'Length is {len(number)}, required: 6.')
        return True

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'{self.model} - Invalid VIN type. ',
                                     f'Type is: {type(vin_number)}, required: {int}.')
        if vin_number not in range(1000000, 9999999 + 1):
            raise IncorrectVinNumber(f'{self.model} - Invalid range for VIN number. ',
                                     f'VIN number must be in range from 1000000 to 9999999.')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message, exc.additional_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.additional_info)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message, exc.additional_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.additional_info)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 9999999, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message, exc.additional_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.additional_info)
else:
    print(f'{third.model} успешно создан')
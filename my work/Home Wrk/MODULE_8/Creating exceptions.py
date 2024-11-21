# -*- coding: windows-1251 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='windows-1251')


class IncorrectVinNumber(Exception):
    """������ vin"""

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    """������ ������� ����"""

    def __init__(self, message):
        self.message = message


class Car:
    """����� ����"""

    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers

    def __str__(self):
        return f"{self.model}, {self.__numbers}"

    def __int__(self):
        return int(self.__vin)

    def __is_valid_vin(self, vin_number):
        """�������� vin"""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("������������ ��� vin �����")
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("�������� �������� ��� vin ������")

        return True

    def __is_valid_numbers(self, __numbers):
        """�������� ������"""
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers("������������ ��� ������ ��� �������")
        if len(__numbers) != 6:
            raise IncorrectCarNumbers("�������� ����� ������")
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} ������� ������')

try:
    second = Car('Model2', 300, '�001��')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} ������� ������')

try:
    third = Car('Model3', 2020202, '��� ������')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} ������� ������')

"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return num
    k = 2
    while k * k <= num and num % k != 0:
        k += 1
    return k * k > num

def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    elif filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers_list))
    else:
        print(f"ValueError. Filter type can not be {filter_type}")

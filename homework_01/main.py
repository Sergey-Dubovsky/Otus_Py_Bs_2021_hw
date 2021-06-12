"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    list_of_square=[]

    for num in args:
        list_of_square.append(num**2)

    return list_of_square    



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

# Функция проверки числа на простое/непростое
def is_prime(num):
    res=True

    for i in range(2,num-1):
        if num % i == 0:
            res=False
            break

    return res        


def filter_numbers(list_of_numbers,operation):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    result_list=[]

    if operation == ODD:
        for num in list_of_numbers:
            if num % 2 != 0 :  
                result_list.append(num)
    else:
        if operation == EVEN:
            for num in list_of_numbers:
                if num % 2 == 0 :  
                    result_list.append(num)
        else:
            if operation == PRIME:
                for num in list_of_numbers:
                    if is_prime(num) :  
                        result_list.append(num)
            else:
                #Если операция задана неверно, возвращать None
                result_list=None
    return result_list


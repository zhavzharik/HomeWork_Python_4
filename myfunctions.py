# Создание восьми функций

# Функция создает красивый разделитель из 10-ти звездочек

def simple_separator():
    return '*' * 10


print(simple_separator() == '**********')


# Функция создает разделитель из звездочек, число которых можно регулировать параметром count
def long_separator(count):
    return '*' * count


print(long_separator(3) == '***')
print(long_separator(4) == '****')

# Функция создает разделитель из любых символов любого количества

def separator(symbol, count):
    return symbol * count


print(separator('-', 10) == '----------')
print(separator('#', 5) == '#####')

'''
Функция печатает Hello World в формате:
**********
Hello World!
##########
'''
def hello_world():
    print('*' * 10)
    print('Hello World!')
    print('#' * 10)


hello_world()

'''
Функция печатает приветствие в красивом формате
**********
Hello {who}!
##########
'''
def hello_who(who='World'):
    print('*' * 10)
    print(f'Hello {who}!')
    print('#' * 10)


hello_who()
hello_who('Max')
hello_who('Kate')

# Функция складывает любое количество цифр и возводит результат в степень power
def pow_many(power, *args):
    sum = 0
    for n in args:
        sum +=n
    result = sum ** power
    return result


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

'''
Функция выводит переданные параметры в фиде key --> value
key - имя параметра
value - значение параметра
:param kwargs: любое количество именованных параметров
:return: None
'''
def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} --> {v}')


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

# Функция фильтрует последовательность iterable на основании переданной функции и возвращает новую последовательность
def my_filter(iterable, function):
    new_iterable = list(filter(function, iterable))
    return new_iterable


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
#Напишите функцию, которая принимает на вход строку —
#абсолютный путь до файла. Функция возвращает кортеж из трёх
#элементов: путь, имя файла, расширение файла.


import os

string = "C:/nik00/PycharmProjects/python_hw5.py"


def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')



# Напишите однострочный генератор словаря, который принимает
#на вход три списка одинаковой длины: имена str, ставка int,
#премия str с указанием процентов вида «10.25%». В результате
#получаем словарь с именем в качестве ключа и суммой
#премии в качестве значения. Сумма рассчитывается
#как ставка умноженная на процент премии


names = ['Никита', 'Илья', "Евгений"]
salaries = [10000, 15000, 30000]
awards = ['10.25%', '13%', '6%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Вывод:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})



#Создайте функцию генератор чисел Фибоначчи (см. Википедию).


a = int(input('введите число  '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))

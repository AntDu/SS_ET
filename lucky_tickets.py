"""
Счастливые билеты.
Есть 3 способа подсчёта счастливых билетов:
1. Простой — если на автобусном билете напечатано шестизначное число, и сумма первых трёх цифр равна сумме последних трёх, то этот билет считается счастливым.
2. Сложный — если сумма чётных цифр билета равна сумме нечётных цифр билета, то билет считается счастливым.
3. Смешанный — если сумма цифр на чётных позициях билета равна сумме цифр на нечётных позициях билета, то билет считается счастливым.
Задача:
Номер билета - шестизначное число. Нужно написать консольное приложение, которое может посчитать количество счастливых билетов. Для выбора алгоритма подсчёта читается текстовый файл. Путь к текстовому файлу задаётся в консоли после запуска программы. Индикаторы алгоритмов:
1 - слово 'Simple'
2 - слово `Difficult'
3 - слово ‘Mixed’
После задания всех необходимых параметров, программа в консоль должна вывести количество счастливых билетов для указанного способа подсчёта.

"""
from os import path

from yes_to_continue import yes_to_continue


def lucky_check(ticket, key):
    key = key.lower()
    if key == 'simple':
        if sum(ticket[:3]) == sum(ticket[3:]):
            return 1
        return 0
    if key == 'difficult':
        if sum(ticket[::2]) == sum(ticket[::-2]):
            return 1
        return 0
    if key == 'mixed':
        even = sum([i for i in ticket if i % 2 == 0])
        odd = sum([i for i in ticket if i % 2 == 1])
        if even == odd:
            return 1
        return 0


def lucky_counter(key, start=1, end=999999):
    count = 0
    empty_ticket = [0, 0, 0, 0, 0, 0]
    for number in range(start, end + 1):
        new = [int(i) for i in str(number)]
        ticket = empty_ticket[:(6 - len(new))] + new
        count += lucky_check(ticket, key)
    return count


def try_your_luck():
    algorithm_path = path.abspath('' + 'static')
    answer = True
    print(algorithm_path)

    while answer:
        user_input_path = input('FILE PASS: ')
        file_path = path.join(algorithm_path, user_input_path + '.txt')
        print(file_path)

        if path.isfile((file_path)):
            with open(file_path) as f:
                text = f.read().lower()
                print('Selected algorithm:', text)
                for key in ('mixed', 'simple', 'difficult'):
                    if key in text:
                        print(key, (lucky_counter(key)))
        else:
            print('FILE NOT FOUND')





if __name__ == "__main__":

    answer = True

    while answer:

        try_your_luck()

        print('Want to continue')
        user_choice = input('Enter Y/N')
        answer = yes_to_continue(user_choice)


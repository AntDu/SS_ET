"""
Анализ конвертов
Есть два конверта со сторонами (a,b) и (c,d) определить, можно ли один конверт вложить в другой.
Программа должна обрабатывать ввод чисел с плавающей точкой.
Программа спрашивает у пользователя размеры конвертов по одному параметру за раз.
После каждого подсчёта программа спрашивает у пользователя хочет ли он продолжить.
Если пользователь ответит “y” или “yes” (без учёта регистра), программа продолжает работу сначала,
в противном случае – завершает выполнение.

"""
import math
from yes_to_continue import yes_to_continue


class Envelope:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side


def validation(num):
    if type(num) == float:
        if num > 0:
            return num
    else:
        raise ValueError('one of the parameters is not a number')


def envelope_analysis(envelope1, envelope2):
    diag_a = envelope1.first_side ** 2 + envelope1.second_side ** 2
    diag_b = envelope2.first_side ** 2 + envelope2.second_side ** 2

    first_diag = math.sqrt(diag_a)
    second_diag = math.sqrt(diag_b)

    if first_diag == second_diag:
        return 'The same envelopes.\n'
    elif first_diag > second_diag:
        return 'Second envelope fit in First\n'
    elif second_diag > first_diag:
        return 'First envelope fit in Second\n'


if __name__ == '__main__':

    answer = True

    while answer:

        print('Enter the sides of the first envelope')
        first_side = float(input('first side = '))
        first_side = validation(first_side)
        second_side = float(input('second side = '))
        second_side = validation(second_side)
        first_envelope = Envelope(first_side, second_side)

        print('Enter the sides of the second envelope')
        first_side = float(input('first side = '))
        first_side = validation(first_side)
        second_side = float(input('second side = '))
        second_side = validation(second_side)
        second_envelope = Envelope(first_side, second_side)

        analysis_result = envelope_analysis(first_envelope, second_envelope)
        print(analysis_result)

        print('Want to continue')
        user_choice = input('Enter Y/N')
        answer = yes_to_continue(user_choice)






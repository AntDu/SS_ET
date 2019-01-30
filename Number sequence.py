"""
Числовая последовательность
Программа выводит ряд натуральных чисел через запятую, квадрат которых меньше заданного n.
Программа запускается через вызов главного класса с параметрами.

"""


def validation(num):
    if type(num) == int:
        return num
    else:
        print('Incorrect value, enter a number')
        return False


class NumericSequence:
    def __init__(self, user_num):
        self.user_num = user_num
        self.square_list = []

    def sequence_calculation(self):
        for n in range(self.user_num):
            if (n ** 2) < self.user_num:
                self.square_list.append(n)
        for x in self.square_list:
            print(x, end=", ")


if __name__ == '__main__':

    userInput = int(input('Enter number: '))
    num = validation(userInput)
    if num:
        sequence = NumericSequence(num)
        sequence.sequence_calculation()

"""
Ряд Фибоначчи для диапазона
Программа позволяет вывести все числа Фибоначчи, которые находятся в указанном диапазоне.
Диапазон задаётся двумя аргументами при вызове главного класса. Числа выводятся через запятую по возрастанию.

"""


class Fibonacci:
    def __init__(self, last, first=1):
        self.first = self.validation(first)
        self.last = self.validation(last)
        self.list = self.fib(first, last)

    @staticmethod
    def validation(param):
        if type(param) != int and type(param) != float:
            raise TypeError('One of the parameters is not an integer')
        return abs(round(param))

    @staticmethod
    def fib(first, last):
        if last < first:
            last, first = first, last
        fib_list = []
        a, b = 0, 1
        while a <= last:
            if first <= a <= last:
                fib_list.append(a)
            a, b = b, a + b
        return fib_list

    def __repr__(self):
        return ', '.join(map(str, self.list))


if __name__ == '__main__':

    print('Enter start point')
    start_point = int(input(' '))
    print('Enter end point')
    end_point = int(input(''))
    fibo = Fibonacci(start_point, end_point)
    print(fibo)





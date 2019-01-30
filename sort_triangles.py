"""
Сортировка треугольников
Разработать консольную программу, выполняющую вывод треугольников в порядке убывания их площади. После добавления каждого
нового треугольника программа спрашивает, хочет ли пользователь добавить ещё один.
Если пользователь ответит “y” или “yes” (без учёта регистра), программа попросит ввести данные для ещё одного треугольника,
 в противном случае – выводит результат в консоль.
•	Расчёт площади треугольника должен производится по формуле Герона.
•	Каждый треугольник определяется именем и длинами его сторон.
Формат ввода (разделитель - запятая):
<имя>, <длина стороны>, <длина стороны>, <длина стороны>
•	Приложение должно обрабатывать ввод чисел с плавающей точкой.
•	Ввод должен быть нечувствителен к регистру, пробелам, табам.
•	Вывод данных должен быть следующем примере:
============= Triangles list: ===============
1. [Triangle first]: 17.23 сm
2. [Triangle 22]: 13 cm
3. [Triangle 1]: 1.5 cm

"""

import math
from yes_to_continue import yes_to_continue


def validation(num):
    if type(num) == int or type(num) == float:
        if num > 0:
            return num
    else:
        raise ValueError('one of the parameters is not a number')


def triangle_is_exist(side_a, side_b, side_c):
    if (side_a + side_b) > side_c and (side_b + side_c) > side_a and (side_a + side_c) > side_b:
        return True


def triangle_is_valid(triangle_name, side_a, side_b, side_c):
    if side_a and side_b and side_c and triangle_name:
        if triangle_is_exist(side_a, side_b, side_c):
            return True


class Triangle:
    def __init__(self, triangle_name, side_a, side_b, side_c):
        self.name = triangle_name
        self.a = side_a
        self.b = side_b
        self.c = side_c
        self.area = Triangle.area(side_a, side_b, side_c)

    def __lt__(self, other):
        return self.area < other.area

    def __str__(self):
        return f'[Triangle {self.name}]: {self.area: .2f} cm'

    @staticmethod
    def area(side_a, side_b, side_c):
        p = (side_a + side_b + side_c) * 0.5
        s = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
        return s


if __name__ == '__main__':
    list_of_triangles = []
    answer = True

    while answer:

        triangle_name = input("name=")
        side_a = float(input("side a="))
        side_a = validation(side_a)
        side_b = float(input("side b="))
        side_b = validation(side_b)
        side_c = float(input("side c="))
        side_c = validation(side_c)
        if triangle_is_valid(triangle_name, side_a, side_b, side_c):
            triangle = Triangle(triangle_name, side_a, side_b, side_c)
            list_of_triangles.append(triangle)

        print('Want to continue')
        user_choice = input('Enter Y/N')
        answer = yes_to_continue(user_choice)

    list_of_triangles.sort(reverse=True)
    print('============= Triangles list: ===============')
    for t in list_of_triangles:
        print(t)



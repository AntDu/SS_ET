"""
Файловый парсер
Нужно написать программу, которая будет иметь два режима:
1.	Подсчитать количество вхождений строки в текстовом файле.
2.	Делать замену строки на другую в указанном файле
Программа должна принимать аргументы на вход при запуске:
1.	<путь к файлу> <строка для подсчёта>
2.	<путь к файлу> <строка для поиска> <строка для замены>

"""

from os import path

from yes_to_continue import yes_to_continue


def counting_elements(path, instance):

    filename = path
    with open(filename) as file:
        file_contents = file.read()

        return int(file_contents.count(instance))


def replace_element(path, instance, replaced):

    with open(path, "r") as file:
        file_contents = file.read()

        return file_contents.replace(instance, replaced)


if __name__ == "__main__":

    path_to_file = path.abspath('' + 'static\\test1.txt')
    print(path_to_file)

    answer = True

    while answer:
        instance = input("Enter what you are looking for in the text: ")
        replace = input("Enter what you want to replace it with: ")

        print(counting_elements(path_to_file, instance))
        print(replace_element(path_to_file, instance, replace))

        print('Want to continue')
        user_choice = input('Enter Y/N')
        answer = yes_to_continue(user_choice)


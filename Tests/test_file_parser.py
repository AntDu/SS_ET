from os import path
from unittest import TestCase

from File_parser import counting_elements
from File_parser import replace_element


class TestFileParser(TestCase):

    def test_counting_elements(self):
        path_to_file = path.abspath('' + 'test_file_parser_example.txt')
        instance = 'a'
        self.assertEqual(counting_elements(path_to_file, instance), 4)

    def test_replace_element(self):
        path_to_file = path.abspath('' + 'test_file_parser_example.txt')
        instance = 'a'
        replace = '*'
        self.assertEqual(replace_element(path_to_file, instance, replace), '****')


if __name__ == '__main__':
    TestFileParser()
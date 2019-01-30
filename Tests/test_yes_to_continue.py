from unittest import TestCase

from yes_to_continue import yes_to_continue


class TestFileParser(TestCase):

    def test_yes_answer(self):
        user_choice = 'yes'
        self.assertTrue(yes_to_continue(user_choice), 'Ok let\'s continue')

    def test__no_answer(self):
        user_choice = 'no'
        self.assertFalse(yes_to_continue(user_choice), 'Have a nice day')

    def test__not_valid_str_answer(self):
        user_choice = '123'
        self.assertFalse(yes_to_continue(user_choice), 'You entered something wrong')

    def test__not_valid_int_answer(self):
        user_choice = 123
        self.assertFalse(yes_to_continue(user_choice), 'You entered something wrong')


if __name__ == '__main__':
    TestFileParser()

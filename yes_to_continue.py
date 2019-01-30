NO_COMMANDS = ('n', 'no')
YES_COMMANDS = ('yes', 'y')


def yes_to_continue(user_choice):

    if str(user_choice).lower().isalpha():
        if user_choice.lower() in YES_COMMANDS and user_choice.lower() not in NO_COMMANDS:

            print('Ok let\'s continue')
            return True
        else:

            print('Have a nice day')
            return False
    else:

        print('You entered something wrong')
        return False

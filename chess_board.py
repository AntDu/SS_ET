"""
Шахматная доска
Вывести шахматную доску с заданными размерами высоты и ширины, по принципу:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
  *  *  *  *  *  *

"""

from yes_to_continue import yes_to_continue


class ChessBoard:
    def __init__(self, height, width):
        self.height = ChessBoard.validation(height)
        self.width = ChessBoard.validation(width)
        self.black = '*'
        self.white = '..'

    @staticmethod
    def validation(param):
        if type(param) != int and type(param) != float:
            raise ValueError('one of the parameters is not a number')
        return abs(round(param))

    def __repr__(self):
        board = []

        for i in range(self.height):
            s = ''.join(self.black if (i + j) % 2 == 0 else self.white for j in range(self.width))
            board.append(s)
        board = '\n'.join(board)
        return board


if __name__ == '__main__':

    answer = True

    while answer:
        print('Enter height')
        height = int(input('->'))
        print('Enter width')
        width = int(input('->'))
        chess_board = ChessBoard(height, width)
        print(chess_board)

        print('Want to continue')
        user_choice = input('Enter Y/N')
        answer = yes_to_continue(user_choice)



from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from custom_exceptions.exceptions import InvalidInteger, InvalidLength


@length
@input_integer_data_validation
class ChessDesk:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.chess_desk = []

    @property
    def create_chess_desk(self) -> list:
        '''
        genegate chess desk 2D list
        :return list of lists with generated chess desk:
        '''
        if self.chess_desk == []:
            self.chess_desk = [['*' if (row + elem) % 2 == 0 else ' ' for elem in range(self.__width)]
                               for row in range(self.__height)]
        return self.chess_desk

    def __str__(self):
        res = ''
        for row in self.chess_desk:
            for elem in row:
                res += elem
            res += '\n'
        return res


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to create new chess desk, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input integer height and width greater 0, split numbers with\',\'')
            input_data = [elem for elem in input('> ').split(',')]
            try:
                chess_desk = ChessDesk(input_data, param_numbers)
            except (InvalidInteger, InvalidLength) as error:
                print(error)
                continue
        else:
            print('Bye')
            want_to_continue = False
            continue
        print('Do you want to print chess desk, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            chess_desk.create_chess_desk
            print(chess_desk)
        else:
            print('Bye')
            want_to_continue = False

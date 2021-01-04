from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from custom_exceptions.exceptions import InvalidInteger, InvalidLength

@length
@input_integer_data_validation
def create_chess_desk(height: int, width: int) -> list:
    '''
    genegate chess desk 2D list
    :param height:
    :param width:
    :return list of lists with generated chess desk:
    '''
    return [['*' if (row + elem) % 2 == 0 else ' ' for elem in range(width)] for row in range(height)]


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to create new chess desk, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input integer height and width greater 0, split numbers with \',\'')
            input_data = [elem for elem in input('> ').split(',')]
            try:
                chess_desk = create_chess_desk(input_data, param_numbers)
            except (InvalidInteger, InvalidLength) as error:
                print(error)
                continue
        else:
            print('Bye')
            want_to_continue = False
            continue
        print('Do you want to print chess desk, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            for row in chess_desk:
                for elem in row:
                    print(elem, end='')
                print()
        else:
            print('Bye')
            want_to_continue = False

from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from custom_exceptions.exceptions import InvalidLength, InvalidInteger


@length
@input_integer_data_validation
def make_sequence(length: int, squere: int) -> str:
    '''
    generate str of number sequence with got length, power every number bigger than got squere
    :param length:
    :param squere:
    :return str:
    '''
    squere = squere ** 0.5
    if squere == int(squere):
        pow_res = int(squere)
    else:
        pow_res = int(squere) + 1
    sequence_list = [str(pow_res + step) for step in range(length)]
    return ','.join(sequence_list)


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to get numbers sequence, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input integer length of sequence and squered number, greater 0, split numbers with \',\'')
            try:
                print('result is', make_sequence([elem for elem in input('> ').split(',')], param_numbers))
            except(InvalidLength, InvalidInteger) as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

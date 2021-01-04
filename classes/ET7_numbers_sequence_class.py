from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from custom_exceptions.exceptions import InvalidLength, InvalidInteger


@length
@input_integer_data_validation
class NumberSequence:
    def __init__(self, length: int, squere: int):
        squere = squere ** 0.5
        self.__length = length
        self.res = []
        if squere == int(squere):
            self.__squere = int(squere)
        else:
            self.__squere = int(squere) + 1

    @property
    def make_sequence(self):
        if self.res == []:
            self.res = [str(self.__squere + step) for step in range(self.__length)]
        return self.res

    def __str__(self):
        return ','.join(self.res)


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to get numbers sequence, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input integer length of sequence and squered number, greater 0, split numbers with \',\'')
            try:
                sequence = NumberSequence([elem for elem in input('> ').split(',')], param_numbers)
            except(InvalidLength, InvalidInteger) as error:
                print(error)
            sequence.make_sequence
            print(sequence)
        else:
            print('Bye')
            want_to_continue = False

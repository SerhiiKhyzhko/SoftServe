from decorators_and_additional_vars.decorators import input_float_data_validator, length
from custom_exceptions.exceptions import InvalidFloat, InvalidLength


def envelops_comparison(envelop_1: list, envelop_2: list) -> str:
    if envelop_1 > envelop_2:
        return f'envelop with dimension {envelop_2} can be put in envelop with dimension {envelop_1}'
    elif envelop_2 > envelop_1:
        return f'envelop with dimension {envelop_1} can be put in envelop with dimension {envelop_2}'
    return 'it is imposiable to put one envelope in another'


@length
@input_float_data_validator
class Envelope:
    def __init__(self, data):
        self.height = data[0]
        self.width = data[1]

    def __str__(self):
        return ','.join((str(self.height), str(self.width)))

    def __eq__(self, other):
        return (self.height == other.height and self.width == other.width) \
               or (self.height == other.width and self.width == other.height)

    def __gt__(self, other):
        return (self.height > other.height and self.width > other.width) \
               or (self.height > other.width and self.width > other.height)

    def __lt__(self, other):
        return (self.height < other.height and self.width < other.width) \
               or (self.height < other.width and self.width < other.height)

    # overbundant
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to check is it posible to put one envelop in another, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input envelops` height and width greater 0, split numbers with \',\'')
            try:
                first_envelope = Envelope([elem for elem in input('> ').split(',')], param_numbers)
                second_envelope = Envelope([elem for elem in input('> ').split(',')], param_numbers)
            except (InvalidFloat, InvalidLength) as error:
                print(error)
                continue
            print(envelops_comparison(first_envelope, second_envelope))
        else:
            print('Bye')
            want_to_continue = False

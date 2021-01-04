from decorators_and_additional_vars.decorators import input_float_data_validator
from custom_exceptions.exceptions import InvalidFloat


@input_float_data_validator
def envelops_comparison(envelop_1: list, envelop_2: list) -> str:
    if (envelop_1[0] > envelop_2[0] and envelop_1[1] > envelop_2[1]) or \
            (envelop_1[0] > envelop_2[1] and envelop_1[1] > envelop_2[0]):
        return f'envelop with dimension {envelop_2} can be put in envelop with dimension {envelop_1}'
    elif (envelop_2[0] > envelop_1[0] and envelop_2[1] > envelop_1[1]) or \
            (envelop_2[0] > envelop_1[1] and envelop_2[1] > envelop_1[0]):
        return f'envelop with dimension {envelop_1} can be put in envelop with dimension {envelop_2}'
    return 'it is imposiable to put one envelope in another'


def main():
    want_to_continue, param_numbers = True, 2
    while want_to_continue:
        print('Do you want to check is it posible to put one envelop in another, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('Input envelops` height and width greater 0, split numbers with \',\'')
            first_envelope = [elem for elem in input().split(',')]
            second_envelope = [elem for elem in input().split(',')]
            try:
                print(envelops_comparison(first_envelope, second_envelope))
            except InvalidFloat as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

from decorators_and_additional_vars.decorators import is_valid_string, split_number
from decorators_and_additional_vars.additional_vars import ones, tenth1, tenth2, hundreds, digits, general
from custom_exceptions.exceptions import InvalidInteger


@is_valid_string
@split_number
def generate_number(input_data: list) -> str:
    '''
    accumulate turned group of numbers into string
    :param input_data:
    :return string:
    '''
    res = []
    for index, numbers in enumerate(input_data):
        if numbers == '000':
            continue
        step = len(input_data) - 1 - index
        res.append(convert_to_str(step, numbers))
    return ''.join(res)


def convert_to_str(step: int, numbers: str) -> str:
    '''
    turn group of 3 numbers into string
    :param step:
    :param numbers:
    :param ending using for get correct diigit of current part of sequence:
    :return string:
    '''
    ending, res = int(numbers[2]), ''
    if ending == 1:
        ending = 0
    elif 1 < ending < 5:
        ending = 1
    else:
        ending = 2
    for index, number in enumerate(numbers):
        if index == 1 and number == '1':
            res += (general[index][0][numbers[1:3]] + ' ' + digits[step][2])
            return res
        elif index == 1 and number != '1':
            res += (general[index][index][number] + ' ')
        else:
            res += (general[index][number] + ' ')
    return res + digits[step][ending] + ' '


def main():
    want_to_continue, supported_length = True, 33
    while want_to_continue:
        print('Do you want to convert integer number to string, input y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('You should input integer number greater 0 and amount of numbers must not be more than 33')
            input_data = input()
            if len(input_data) > supported_length:
                print('You should input integer number, amount of numbers must not be less than 34')
                continue
            try:
                print(f'Result is: {generate_number(input_data).strip()}')
            except InvalidInteger as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

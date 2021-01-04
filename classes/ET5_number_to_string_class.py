from decorators_and_additional_vars.decorators import is_valid_string, split_number
from decorators_and_additional_vars.additional_vars import ones, tenth1, tenth2, hundreds, digits, general
from custom_exceptions.exceptions import InvalidInteger


@is_valid_string
@split_number
class ConvertNumberToString:
    def __init__(self, data: list):
        self.data = data
        self.__res = []

    @property
    def converrtor(self):
        for index, numbers in enumerate(self.data):
            if numbers == '000':
                continue
            step = len(self.data) - 1 - index
            ending, result = int(numbers[2]), ''
            if ending == 1:
                ending = 0
            elif 1 < ending < 5:
                ending = 1
            else:
                ending = 2
            for index, number in enumerate(numbers):
                if index == 1 and number == '1':
                    result += (general[index][0][numbers[1:3]] + ' ' + digits[step][2])
                    return res
                elif index == 1 and number != '1':
                    result += (general[index][index][number] + ' ')
                else:
                    result += (general[index][number] + ' ')
            self.__res.append(result + digits[step][ending] + ' ')
            return self.__res

    def __str__(self):
        return ''.join(self.__res).strip()


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
                convert = ConvertNumberToString(input_data)
            except InvalidInteger as error:
                print(error)
                continue
            convert.converrtor
            print(f'Result is: {convert}')
        else:
            print('Bye')
            want_to_continue = False

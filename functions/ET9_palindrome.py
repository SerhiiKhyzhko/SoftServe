from decorators_and_additional_vars.decorators import is_valid_string
from custom_exceptions.exceptions import InvalidInteger


@is_valid_string
def find_palindromes(numbers:str) -> str or 0:
    '''
    looking for palindrom in numbers string
    :param numbers:
    :return list with palindrom or 0 if it is not include palindrome:
    '''
    list_of_palindromes, sequence_len, first_index, second_index = [], 2, 0, 2
    while sequence_len <= len(numbers):
        for _ in range(len(numbers) + 1 - sequence_len):
            sub_row = numbers[first_index:second_index]
            if sub_row == sub_row[::-1] and sub_row not in list_of_palindromes:
                list_of_palindromes.append(sub_row)
            first_index += 1
            second_index += 1
        sequence_len += 2
        first_index = 0
        second_index = sequence_len
    if list_of_palindromes == []:
        return 0
    return ','.join(list_of_palindromes)


def main():
    want_to_continue, min_length = True, 1
    while want_to_continue:
        print('Do you want to chack number to palindromes, input y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('You should input integer number greater 10')
            input_data = input('> ')
            if len(input_data) < 2:
                print('number must be greater than 10')
                continue
            try:
                print(f'Result is: {find_palindromes(input_data, min_length)}')
            except InvalidInteger as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

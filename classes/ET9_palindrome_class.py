from decorators_and_additional_vars.decorators import is_valid_string
from custom_exceptions.exceptions import InvalidInteger


@is_valid_string
class Palindrome:
    def __init__(self, number: str):
        self.number = number
        self.res = []

    def find_palindromes(self):
        '''
        looking for palindrom in numbers string
        :param numbers:
        :return list with palindrom or 0 if it is not include palindrome:
        '''
        if self.res == []:
            sequence_len, first_index, second_index = 2, 0, 2
            while sequence_len <= len(self.number):
                for _ in range(len(self.number) + 1 - sequence_len):
                    sub_row = self.number[first_index:second_index]
                    if sub_row == sub_row[::-1] and sub_row not in self.res:
                        self.res.append(sub_row)
                    first_index += 1
                    second_index += 1
                sequence_len += 2
                first_index = 0
                second_index = sequence_len
        if self.res == []:
            return self.res.append('0')
        return self.res

    def __str__(self):
        return ','.join(self.res)


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
            print('Result is:', end=' ')
            try:
                palindrome = Palindrome(input_data)
            except InvalidInteger as error:
                print(error)
                continue
            palindrome.find_palindromes()
            print(palindrome)
        else:
            print('Bye')
            want_to_continue = False

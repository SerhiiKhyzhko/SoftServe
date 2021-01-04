from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from decorators_and_additional_vars.additional_vars import fib_nums
from custom_exceptions.exceptions import InvalidLength, InvalidInteger


@length
@input_integer_data_validation
class Fibonacci:
    def __init__(self, length: int = 0, start: int = 0, finish: int = 0):
        self.__length = length
        self.__start = start
        self.__finish = finish
        self.res = []

    @property
    def fibonacci_length(self):
        if self.__length == 0:
            return self.__length
        first_num, second_num, fib_num = fib_nums[10][0], fib_nums[10][1], 0
        if self.__length < 10:
            first_num, second_num = fib_nums[length][0], fib_nums[length][1]
        while len(str(fib_num)) <= self.__length:
            fib_num = first_num + second_num
            first_num = second_num
            second_num = fib_num
            if len(str(fib_num)) == self.__length:
                self.res.append(str(fib_num))
        return self.res

    @property
    def fibonacci_range(self):
        if self.__start == 0:
            return self.__start
        first_num, second_num, fib_num = fib_nums[10][0], fib_nums[10][1], 0
        if len(str(self.__start)) < 10:
            first_num = fib_nums[len(str(self.__start))][0]
            second_num = fib_nums[len(str(self.__start))][1]
        while fib_num < self.__finish:
            fib_num = first_num + second_num
            first_num = second_num
            second_num = fib_num
            if fib_num >= self.__start and fib_num <= self.__finish:
                self.res.append(str(fib_num))
        return self.res

    def __str__(self):
        return ','.join(self.res)


def main():
    want_to_continue, param_numbers = True, [1, 2]
    while want_to_continue:
        print('Do you want to get Fibonacci sequence, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print(
                '1. Input range of Fibonacci sequence \n2. Input length of fibonacci number \nChoose an action(write a number)')
            action = input('> ')
            if action not in ['1', '2']:
                print('Invalid input, try again')
                continue
            input_data = [elem for elem in input('input data \n> ').split(',')]
            print('result is ', end='')
            try:
                fibonacci_numbers = Fibonacci(input_data, param_numbers[1] if action == '1' else param_numbers[0])
            except(InvalidLength, InvalidInteger) as error:
                print(error)
                continue
            if action == '1':
                fibonacci_numbers.fibonacci_range
            else:
                fibonacci_numbers.fibonacci_length
            print(fibonacci_numbers)
        else:
            print('Bye')
            want_to_continue = False

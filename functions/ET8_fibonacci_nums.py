from decorators_and_additional_vars.decorators import input_integer_data_validation, length
from decorators_and_additional_vars.additional_vars import fib_nums
from custom_exceptions.exceptions import InvalidLength, InvalidInteger


@length
@input_integer_data_validation
def fibonacci_length(length: int) -> list:
    '''
    generate fibonacci sequence with got length of number
    :param length:
    :param action:
    :return res:
    '''
    first_num, second_num, fib_num, res = fib_nums[10][0], fib_nums[10][1], 0, []
    if length < 10:
        first_num, second_num = fib_nums[length][0], fib_nums[length][1]
    while len(str(fib_num)) <= length:
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        if len(str(fib_num)) == length:
            res.append(str(fib_num))
    return ','.join(res)


@length
@input_integer_data_validation
def fibonacci_range(start: int, finish: int) -> list:
    '''
    generate fibonacci sequence in got range
    :param start:
    :param finish:
    :param action:
    :return res:
    '''
    first_num, second_num, fib_num, res = fib_nums[10][0], fib_nums[10][1], 0, []
    if len(str(start)) < 10:
        first_num, second_num = fib_nums[len(str(start))][0], fib_nums[len(str(start))][1]
    while fib_num < finish:
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        if fib_num >= start and fib_num <= finish:
            res.append(str(fib_num))
    return ','.join(res)


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
                if action == '1':
                    print(fibonacci_range(input_data, param_numbers[1]))
                else:
                    print(fibonacci_length(input_data, param_numbers[0]))
            except(InvalidLength, InvalidInteger) as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

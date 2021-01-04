from decorators_and_additional_vars.decorators import length, path_validation
from custom_exceptions.exceptions import InvalidPath, InvalidLength
import pathlib


@length
def count_string(file_path: str, to_count: str) -> int:
    '''
    count substring in text file
    :param file_path:
    :param to_count:
    :return counter:
    '''
    try:
        with open(file_path) as file_handler:
            counter = 0
            for line in file_handler:
                counter += line.lower().count(to_count.lower())
    except IOError:
        raise InvalidPath(file_path)
    return counter


@length
@path_validation
def change_string(file_path: str, find_string: str, change_string: str) -> str:
    '''
    change old substring to new one
    :param file_path:
    :param find_string:
    :param change_string:
    :return str, success message:
    '''
    path = pathlib.Path(file_path)
    path.write_text(path.read_text().replace(find_string, change_string))
    return 'Finished successfully'


def main():
    want_to_continue, param_numbers = True, [2, 3]
    while want_to_continue:
        print('Do you want to work with file, input y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('1. Count string in file \n2. Change old string to new one \nChoose an action(write a number)')
            action = input('> ')
            if action not in ['1', '2']:
                print('Invalid input, try again')
                continue
            if action == '1':
                print('Input path to file and string to count, split data with \',\'')
                try:
                    print(count_string([data for data in input().split(',')], param_numbers[0]))
                except(InvalidPath) as error:
                    print(error)
            else:
                print('Input path to file, string change to witch and string witch to change, split data with \',\'')
                try:
                    change_string([data for data in input().split(',')], param_numbers[1])
                except(InvalidPath, InvalidLength) as error:
                    print(error)
        else:
            print('Bye')
            want_to_continue = False

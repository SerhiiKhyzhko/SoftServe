from decorators_and_additional_vars.decorators import length, path_validation
from custom_exceptions.exceptions import InvalidPath, InvalidLength
import pathlib


@length
@path_validation
class FileParser:
    def __init__(self, data: list):
        self.file_path = data[0]
        self.count_or_find_string = data[1]
        self.__counter = 0
        self.__is_changed = 0
        if len(data) == 3:
            self.change = data[2]

    @property
    def count_string(self):
        if self.__counter == 0:
            try:
                with open(self.file_path) as file_handler:
                    for line in file_handler:
                        self.__counter += line.lower().count(self.count_or_find_string.lower())
            except IOError:
                return 'File not found'
        return self.__counter

    @property
    def change_string(self):
        if self.__is_changed == 0:
            path = pathlib.Path(self.file_path)
            path.write_text(path.read_text().replace(self.count_or_find_string, self.change))
            self.__is_changed = 1
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
            try:
                if action == '1':
                    print('Input path to file and string to count, split data with \',\'')
                    file = FileParser([data for data in input().split(',')], param_numbers[0])
                    print(f'Result of counting is: {file.count_string}')
                else:
                    print('Input path to file, string change to witch and string witch to change, split data with \',\'')
                    file = FileParser([data for data in input().split(',')], param_numbers[1])
                    print(file.change_string)
            except(InvalidPath, InvalidLength) as error:
                print(error)
        else:
            print('Bye')
            want_to_continue = False

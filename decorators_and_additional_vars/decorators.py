from custom_exceptions.exceptions import *
import pathlib


def input_integer_data_validation(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: list):
        '''
        walidate input data, is it integer numbers, raise error if invalid data
        :param input_data:
        :return object with walid parameters:
        '''
        for index, elem in enumerate(input_data):
            if elem.isdigit():
                input_data[index] = int(elem)
                if input_data[index] <= 0:
                    raise InvalidInteger(input_data)
            else:
                raise InvalidInteger(input_data)
        return obj(*input_data)

    return wrapper


def length(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: list, data_length: int):
        '''
        validate number of given paramethers, raise error if invalid data
        :param input_data:
        :param data_length:
        :return object with valid paramethers:
        '''
        if len(input_data) == data_length:
            return obj(input_data)
        raise InvalidLength(len(input_data), data_length)

    return wrapper


def input_float_data_validator(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(first_envelope: list, second_envelope: list = []):
        '''
        walidate inputed data, are they float numbers, raise error if invalid data
        :param first_envelope:
        :param second_envelope:
        :return object with valid data:
        '''
        try:
            for data_list in [first_envelope, second_envelope]:
                for num in data_list:
                    num = float(num)
                    if num < 0:
                        raise InvalidFloat(data_list)
        except(ValueError):
            raise InvalidFloat(data_list)
        if second_envelope == []:
            return obj(first_envelope)
        return obj(first_envelope, second_envelope)

    return wrapper


# only for ET3
def input_triangle_data_validator(obj):
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: list):
        '''
        validate sides of triangle, raise error if invalid data
        :param input_data:
        :return object with valid data:
        '''
        try:
            for num in range(4):
                input_data[num] = input_data[num].strip()
                if num != 0:
                    input_data[num] = float(input_data[num])
                    if input_data[num] < 0:
                        raise InvalidFloat(input_data[1:])
        except ValueError:
            raise InvalidFloat(input_data[1:])
        return obj(input_data)

    return wrapper


# only for ET3
def is_triangle(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: list):
        '''
        validate is triangle exist with inputed sides, raise error if invalid data
        :param input_data:
        :return object with valid data:
        '''
        if (input_data[1] + input_data[2] > input_data[3]) and (input_data[1] + input_data[3] > input_data[2]) \
                and (input_data[2] + input_data[3] > input_data[1]):
            return obj(input_data)
        raise InvalidTriangle

    return wrapper


def path_validation(obj) -> callable:
    '''
    :param obj:
    :return wrepper:
    '''

    def wrepper(data: list):
        '''
        validate path to file, raise error if invalid data
        :param data:
        :return object with valid peremethers:
        '''
        file_path = pathlib.Path(data[0])
        if file_path.exists():
            return obj(data)
        raise InvalidPath(data[0])

    return wrepper


# only for ET5
def is_valid_string(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: str):
        '''
        validate input length string and is it include only numbers, raise error if invalid data
        :param supported_length:
        :param input_data:
        :return object with valid data:
        '''
        if input_data.isdigit():
            return obj(input_data)
        raise InvalidInteger(input_data)

    return wrapper


# only for ET5
def split_number(obj) -> callable:
    '''
    :param obj:
    :return wrapper:
    '''

    def wrapper(input_data: str):
        '''
        split numbers into group of 3 numbers, if group is understaffed add '0' before numbers
        :param input_data:
        :return object with prelared data:
        '''
        if len(input_data) % 3 != 0:
            input_data = '0' * (3 - len(input_data) % 3) + input_data
        res = [input_data[index:index + 3] for index in range(0, len(input_data), 3)]
        return obj(res)

    return wrapper

class BaseException(Exception):
    def __init__(self, data):
        self.data = data


class InvalidInteger(BaseException):
    def __str__(self):
        return f'should input only integer numbers greater than 0, but got {self.data}'


class InvalidFloat(BaseException):
    def __str__(self):
        return f'should input only numbers greater than 0, but got {self.data}'


class InvalidPath(BaseException):
    def __str__(self):
        return f'inputed path {self.data} is invalid or file does not exist'


class InvalidLength(Exception):
    def __init__(self, data_length, length):
        self.data_length = data_length
        self.length = length

    def __str__(self):
        return f'input wrong number of paramethers, should be {self.length} but got {self.data_length}'


class InvalidTriangle(Exception):
    def __str__(self):
        return 'Triangle with inputed sides does not exist, sum of two sides should be bigger then third one'

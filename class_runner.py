from classes import ET1_chess_desk_class, ET2_envelop_analysis_class, ET3_triangle_sort_calss, ET4_file_parser_class, \
    ET5_number_to_string_class, ET7_numbers_sequence_class, ET8_fibonacci_nums_class, ET9_palindrome_class


class Runner:
    def __init__(self, task):
        self.task = task

    @property
    def call_task(self):

        self.task.main()


tasks = [
    '1.	Шахматная доска',
    '2.	Анализ конвертов',
    '3.	Сортировка треугольников',
    '4.	Файловый парсер',
    '5.	Число в пропись',
    '6.	Счастливые билеты',
    '7.	Числовая последовательность',
    '8.	Ряд Фибоначчи',
    '9. Палиндром'
]

run_task = {
    '1': Runner(ET1_chess_desk_class),
    '2': Runner(ET2_envelop_analysis_class),
    '3': Runner(ET3_triangle_sort_calss),
    '4': Runner(ET4_file_parser_class),
    '5': Runner(ET5_number_to_string_class),
    '6': 0,
    '7': Runner(ET7_numbers_sequence_class),
    '8': Runner(ET8_fibonacci_nums_class),
    '9': Runner(ET9_palindrome_class)
}


def main():
    print('============== tasks ==============')
    [print(task) for task in tasks]
    number = input('choose number of task \n> ')
    with open(r'D:\softserve\ET_Python\venv\tasks\\'+number+'.txt', encoding='utf-8') as dascription:
        for row in dascription:
            print(row.strip('\n'))
    run_task[number].call_task()


if __name__ == '__main__':
    main()

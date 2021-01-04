from functions import ET1_chess_desk, ET2_envelop_analysis, ET3_triangle_sort, ET4_file_parser, ET5_number_to_string, \
    ET7_numbers_sequance, ET8_fibonacci_nums, ET9_palindrome

tasks = [
    '1.	Шахматная доска',
    '2.	Анализ конвертов',
    '3.	Сортировка треугольников',
    '4.	Файловый парсер',
    '5.	Число в пропись',
    '6.	Счастливые билеты',
    '7.	Числовая последовательность',
    '8.	Ряд Фибоначчи',
    '9.  Палиндром'
]

run_task = {
    '1': ET1_chess_desk,
    '2': ET2_envelop_analysis,
    '3': ET3_triangle_sort,
    '4': ET4_file_parser,
    '5': ET5_number_to_string,
    '6': 0,
    '7': ET7_numbers_sequance,
    '8': ET8_fibonacci_nums,
    '9': ET9_palindrome
}


def main():
    print('============== tasks ==============')
    [print(task) for task in tasks]
    number = input('choose number of task \n> ')
    # need to change a path before '+number+' to path where was downloaded project
    with open(r'D:\softserve\ET_Python\venv\tasks\\'+number+'.txt', encoding='utf-8') as dascription:
        [print(row.strip('\n')) for row in dascription]
    run_task[number].main()


if __name__ == '__main__':
    main()

from decorators_and_additional_vars.decorators import length, input_triangle_data_validator, is_triangle
from custom_exceptions.exceptions import InvalidLength, InvalidFloat, InvalidTriangle


@length
@input_triangle_data_validator
@is_triangle
def count_squere(data):
    half_perimetr = sum(data[1:]) / 2
    print(half_perimetr)
    return round(
        (half_perimetr * (half_perimetr - data[1]) * (half_perimetr - data[2]) * (half_perimetr - data[3])) ** 0.5, 3), \
           data[0]


def main():
    want_to_continue, param_numbers = True, 4
    triangles = []
    while want_to_continue:
        print('Do You want to add triangle, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('input triangle name, and three sides, split data with \',\'')
            input_data = [data for data in input('> ').split(',')]
            try:
                squere = count_squere(input_data, param_numbers)
            except(InvalidLength, InvalidFloat, InvalidTriangle) as error:
                print(error)
                continue
            triangles.append(squere)
        else:
            print('============= Triangles list: ===============')
            triangles.sort(reverse=True)
            for elem in range(len(triangles)):
                print(f'{elem + 1}. {triangles[elem][1]}: {triangles[elem][0]} см')
            want_to_continue = False

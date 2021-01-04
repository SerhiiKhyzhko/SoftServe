from decorators_and_additional_vars.decorators import length, input_triangle_data_validator, is_triangle
from custom_exceptions.exceptions import InvalidLength, InvalidFloat, InvalidTriangle


@length
@input_triangle_data_validator
@is_triangle
class Triangle:
    def __init__(self, data):
        self.name = data[0]
        self.side1 = data[1]
        self.side2 = data[2]
        self.side3 = data[3]
        self.squere = 0

    @property
    def count_squere(self):
        if self.squere == 0:
            half_perimetr = (self.side1 + self.side2 + self.side3) / 2
            self.squere = round((half_perimetr * (half_perimetr - self.side1) * (half_perimetr - self.side2) *
                                (half_perimetr - self.side3)) ** 0.5, 3)
        return self.squere

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.squere == other.squere

    def __gt__(self, other):
        return self.squere > other.squere

    def __lt__(self, other):
        return self.squere < other.squere


def main():
    want_to_continue, param_numbers = True, 4
    triangles = []
    while want_to_continue:
        print('Do You want to add triangle, y\\n?')
        if input('> ').lower() in ['y', 'yes']:
            print('input triangle name, and three sides, split data with \',\'')
            input_data = [data for data in input('> ').split(',')]
            try:
                squere = Triangle(input_data, param_numbers)
            except(InvalidLength, InvalidFloat, InvalidTriangle) as error:
                print(error)
                continue
            squere.count_squere
            triangles.append(squere)
        else:
            print('============= Triangles list: ===============')
            triangles.sort(reverse=True)
            for elem in range(len(triangles)):
                current_elem = triangles[elem].count_squere
                print(f'{elem + 1}. {triangles[elem]}: {current_elem} см')
            want_to_continue = False

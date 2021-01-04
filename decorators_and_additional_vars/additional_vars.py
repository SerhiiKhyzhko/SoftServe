# ET8 Fibonacci numbers
fib_nums = {
    1: (0, 1), 2: (5, 8), 3: (55, 89), 4: (610, 987), 5: (4181, 6765), 6: (46368, 75025),
    7: (514229, 832040), 8: (5702887, 9227465), 9: (39088169, 63245986), 10: (433494437, 701408733)
}
# ET5 Convert numbers to string
ones = {
    '0': '', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
    '8': 'восемь', '9': 'девять'
}
tenth1 = {
    '10': 'десять', '11': 'одиннадцать', '12': 'двенадцать', '13': 'тринадцать', '14': 'четырнадцать',
    '15': 'пятнадцать',
    '16': 'шеснадцать', '17': 'семьнадцать', '18': 'восемнадцать', '19': 'девятнадцать'
}
tenth2 = {
    '0': '', '2': 'двадцать', '3': 'тридцать', '4': 'сорок', '5': 'пятдесят', '6': 'шестьдесят',
    '7': 'семдесят', '8': 'восемдесят', '9': 'девяносто'
}
hundreds = {
    '0': '', '1': 'сто', '2': 'двести', '3': 'триста', '4': 'четыресьта', '5': 'пятсот', '6': 'шестьсот',
    '7': 'семьсот', '8': 'восемьсот', '9': 'дявятьсот'
}
digits = {
    0: ['', '', ''], 1: ['тысяча', 'тысячи', 'тысяч'], 2: ['миллион', 'миллиона', 'миллионов'],
    3: ['миллиард', 'миллиарда', 'миллипрдов'], 4: ['триллион', 'триллиона', 'триллионов'],
    5: ['квадриллион', 'квадриллиона', 'квадриллионов'], 6: ['квинтиллион', 'квинтиллиона', 'квинтиллионов'],
    7: ['секстиллион', 'секстиллиона', 'секстиллионов'], 8: ['септиллион', 'септиллиона', 'септиллионов'],
    9: ['октиллион', 'октиллиона', 'октиллионов'], 10: ['нониллион', 'нониллиона', 'нониллионов']
}
general = {
    0: hundreds, 1: (tenth1, tenth2), 2: ones
}
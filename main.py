import string
import math
from math import sqrt
input_string = input('press enter size: ')
(input_string.replace(" ", "").isdigit())
values = input_string.split()
count = len(values)
if count == 1:
    type_figure = 'Circle'
    a = input_string
    radius = int(a)
    if radius <= 0:
        print ('No such figure exists')
    elif radius > 0:
        diameter = radius * 2
        square = int(math.pi * (radius**2))
        print(f'{type_figure}: {radius = }; {diameter = }, {square = }')
elif count == 2:
    a, b = values
    size_1 = int(a)
    size_2 = int(b)
    if size_1 and size_2:
        perimeter = (size_1 + size_2) * 2
        square = size_1 * size_2
        if size_1 == size_2:
            type_figure = 'Square'
        elif size_1 > size_2 or size_2 > size_1:
            type_figure = 'Rectsngle'
        print(f'{type_figure}: {size_1 = }, {size_2 = }; {perimeter = }, {square = }')
    else:
        print('No such figure exists')
elif count == 3:
    type_figure = 'Triangle'
    a, b, c = values
    size_1 = int(a)
    size_2 = int(b)
    size_3 = int(c)
    if 0 in (size_1, size_2, size_3):
        print('There are no such triangles')
    elif size_1 + size_2 <= size_3 or size_2 + size_3 <= size_1 or size_1 + size_3 <= size_2:
        print('There are no such triangles')
    elif size_1 and size_2 and size_3:
        perimeter = size_1 + size_2 + size_3
        p = (size_1 + size_2 + size_3) / 2
        square = int(sqrt(p * (p - size_1) * (p - size_2) * (p - size_3)))
        print(f'{type_figure}: {size_1 = }, {size_2 = }, {size_3 = }; {perimeter = }, {square = }.')


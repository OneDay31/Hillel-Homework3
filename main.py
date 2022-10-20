import string
import math
from math import sqrt
input_string = input('press enter size: ')
values = input_string.split()
count = len(values)
if count == 1:
    a = input_string
    radius = int(a)
    if radius == 0:
        print ('No such figure exists')
        quit()
    diameter = radius * 2
    square = int(math.pi *(radius**2))
    print('Circle: ' f'{radius = }; {diameter = }, {square = }')
elif count == 2:
    a, b = values
    size_1 = int(a)
    size_2 = int(b)
    if 0 in (size_1, size_2):
        print('No such figure exists')
        quit()
    if size_1 == size_2:
        type_figure = 'Square'
        perimeter = (size_1 + size_2) * 2
        square = size_1 * size_2
        print('type_figure : ' f'{size_1 = }, {size_2 = }; {perimeter = }, {square = }')
    if size_1 > size_2 or size_2 > size_1:
        type_figure = 'Rectangle'
        perimeter = (size_1 + size_2) * 2
        square = size_1 * size_2
        print('Rectangle: ' f'{size_1 = }, {size_2 = }; {perimeter = }, {square = }')
elif count == 3:
    type_figure = 'Triangle'
    a, b, c = values
    size_1 = int(a)
    size_2 = int(b)
    size_3 = int(c)
    if 0 in (size_1, size_2, size_3):
        print('There are no such triangles')
        quit()
    if size_1 + size_2 <= size_3 or size_2 + size_3 <= size_1 or size_1 + size_3 <= size_2:
        print('There are no such triangles')
        quit()
    perimeter = size_1 + size_2 + size_3
    p = (size_1 + size_2 + size_3) / 2
    square = int(sqrt(p * (p - size_1) * (p - size_2) * (p - size_3)))
    print('Triangle: ' f'{size_1 = }, {size_2 = }, {size_3 = }; {perimeter = }, {square = }')

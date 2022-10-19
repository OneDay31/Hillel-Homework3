import string
import math
from math import sqrt
input_string = input('press enter size: ')
values = input_string.split()
count = len(values)
if count == 1:
    (a) = input_string
    a = int(a)
    diameter = a * 2
    square = int(math.pi *(a**2))
    print('Circle: ' f'{a = }; {diameter = } {square = }')
elif count == 2:
    (a, b) = values
    a = int(a)
    b = int(b)
    perimeter = (a) + (b) * 2
    square = a * b
    print('Square or rectangle: ' f'{a = },{b = }; {perimeter = } {square = }')
elif count == 3:
    (a, b, c) = values
    a = int(a)
    b = int(b)
    c = int(c)
    perimeter = (a + b + c)
    p = (a + b + c) / 2
    square = int(sqrt(p * (p - a) * (p - b) * (p - c)))
    print('Triangle: ' f'{a = } , {b = } , {c = }; {perimeter = } , {square = }')

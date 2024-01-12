# WAP to find the area of triangle.
import math
try:
    print('Enter Your Choice.')
    print('Press 1 for Right angle Triangle.')
    print('Press 2 for Equilateral Triangle.')
    print('Press 3 for Isosceles Triangle.')
    print('Press 4 for Scalene Triangle.')
    n = int(input())
except ValueError:
    print('You have entered wrong choice ')
    exit(0)
area = 0.0
if 1 == n:
    b = float(input('Please Enter the base of triangle: '))
    h = float(input('Please Enter the Height of triangle: '))
    area = 0.5 * b * h
elif 2 == n:
    x = float(input('Enter the side of triangle: '))
    area = (1.732/4) * x**2
elif 3 == n:
    a = float(input('Enter the length of equal sides: '))
    b = float(input('Enter the length of non-equal side: '))
    area = 0.25 * math.sqrt(4*a**2 - b**2)
elif 4 == n:
    a = float(input('Enter the side a of Scalene Triangle: '))
    b = float(input('Enter the side b of Scalene Triangle: '))
    c = float(input('Enter the side c of Scalene Triangle: '))
    if not (a+b >c and a+c >b and b+c > a) :
        print('Your three given sides do not follow the triangle inequality')
        exit(1)
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
else:
    print('Your choice do not belong to choices given above.')
    exit(2)
print('The Area of Triangle is: ', area)

# WAP to find the area of triangle.
try:
    print('Enter Your Choice.')
    print('Press 1 for Right angle Triangle.')
    print('Press 2 for Equilateral Triangle.')
    print('Press 3 for Isosceles Triangle.')
    print('Press 4 for Scalene Triangle.')
    n = int(input())
except:
    print('You have entered wrong choice ')
    exit()
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






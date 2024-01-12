# WAP to check whether the given number are pythagorean triplet or not.
# Pythagorean triplet: three number which satisfies pythagoras theorem.
try:
    a, b, c = [int(x) for x in input('Enter three numbers separated by space: ').split()]
except ValueError:
    print('Sorry you have entered wrong value')
    exit()
h = max(a, b, c)
p = min(a, b, c)
b = a+b+c-(h+p)
if p**2 + b**2 == h**2:
    print('Yes, The number that you have entered are pythagorean triplet')
else:
    print('Sorry, but The number that you have entered are not pythagorean triplet')

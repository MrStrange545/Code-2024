# WAP to check whether a given number is prime or not.
# Prime Number: A number is said to be prime if number is only divisible by itself and 1.
try:
    n = int(input('Please Enter a Positive integer Number: '))
except ValueError:
    print('Sorry, Invalid input')
    exit()


def isPrime():
    if n == 1:
        return False
    i = 2
    c = n / 2
    while i <= c:
        if n % i == 0:
            return False
        i += 1
    return True


if isPrime():
    print('yes it is a Prime Number')
else:
    print('No it is not a Prime Number')

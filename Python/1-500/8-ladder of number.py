try:
    n = int(input('Enter the Number of Rows: '))
except ValueError:
    print('Invalid Input')
    exit(0)
i = 1
while i <= n:
    j = 1
    a = 1
    while j <= 2 * i - 1:
        print(a, end=' ')
        if j < i:
            a += 1
        else:
            a -= 1
        j += 1
    i += 1
    print()

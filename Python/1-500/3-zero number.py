# WAP to check whether a given number is zero number or not.
# Zero Number: A Number which contains zero in it.
try:
    n = input('Enter a valid number: ')
    s = float(n)
except ValueError:
    print('I have told you to enter a valid number')
    exit()
finally:
    print('Thank you ')
flag = False
for x in n:
    if x == '0':
        flag = True
        break
if flag:
    print('Yes, The above entered number is zero number')
else:
    print('I am really sorry, but this number is not a zero number.')

n = input('Enter the word or phrase: ')
rev = ''.join(reversed(n))
if rev == n:
    print('Yes it is palindrome ')
else:
    print('no it is not a palindrome ')

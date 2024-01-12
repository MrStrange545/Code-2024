# WAP to print how many times a digit has been occurred in a given number.
try:
    n = input('Kindly enter a valid Number: ')
    s = float(n)
except:
    print('I told you to enter a valid number')
    exit()
finally:
    print('Thank you')
l =list(n)
l1= []
for x in l:
    if(x  not in l1):
        l1.append(x)
        print(' {0} --> {1}.'.format(x,l.count(x)))


    

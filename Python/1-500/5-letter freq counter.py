# WAP to print frequency of every Letter.
try:
    n = list(input('Please enter a Statement: '))
except:
    print('Sorry for inconvience')
    exit()
finally:
    print('Thank you')
l =[]
for x in n:
    if(x not in l):
        l.append(x)
        print('{0} --> {1}'.format(x,n.count(x)))

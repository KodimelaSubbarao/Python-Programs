n=int(input('enter value....'))
a=1
if n<0:
    print('this is not consider the negative')
elif n==0:
    print('the fact of 0 is 1')
else:
    for i in range (1,n+1):
        a=a*i
    print('fact num',a)

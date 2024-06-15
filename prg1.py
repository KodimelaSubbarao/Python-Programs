'''a=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        a.append(i)
print("enter the values..")
print(a)

x=[]
n=int(input("enter the no.of elements..\n"))
for i in range(n):
    print("enter ele",(i+1))
    ele=int(input())
    x.append(ele)
print("the ele's are:") 
print(x)
print(" the min ele is:",min(x))
print(" the max ele is:",max(x))
'''
x=['a','b']
x=[]
n=int(input("enter the values ..\n"))
for i in range(1,n+1):
    ele1=x[0]+str(i)
    ele2=x[1]+str(i)
    x.append(ele1)
    x.append(ele2)
print("after concatenation..")
print(x)


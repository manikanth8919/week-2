n=int(input("the no to be printed"))
a=0
b=1
while(n>0):
    c=a+b
    print(a)
    a=b
    b=c
    n=n-1

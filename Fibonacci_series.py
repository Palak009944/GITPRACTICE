N=int(input("Enter the number of elements you want to see in the FIBONACCI series: "))
a=0
b=1

if N<=0:
    print("Please enter a positive number.")

elif N==1:
    print(a)

else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(3,N+1):
        c=a+b
        print(c,end=' ')

        a=b
        b=c


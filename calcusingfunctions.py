def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Welcome to a simple calculator")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division")
N=int(input("Enter a number of your choice from 1-4: "))
match N:
    case 1:
        print("Sum is: ",sum(num1,num2))
    case 2:
        print("Subtraction is: ",subtract(num1,num2))
    case 3:
        print("Multiplication is: ",multiply(num1,num2))
    case 4:
        if num2==0 :
            print("Division by zero isn't possible")
        else:
            print("Division is: ",divide(num1,num2))
    case _:        #'_' is used for default case in python
        print("Sum is: ",sum(num1,num2))
        print("Subtraction is: ",subtract(num1,num2))
        print("Multiplication is: ",multiply(num1,num2))
        if num2==0 :
            print("Division by zero isn't possible")
        else:
            print("Division is: ",divide(num1,num2))
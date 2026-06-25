class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
class Add(Calculator):
    def __init__(self,a,b):
        super().__init__(a,b)
    
    def calculate(self):
        return self.a + self.b

class Subtract(Calculator):
    def __init__(self,a,b):
        super().__init__(a,b)
    
    def calculate(self):
        return self.a-self.b

class Product(Calculator):
    def __init__(self,a,b):
        super().__init__(a,b)
       
    def calculate(self):
        return self.a*self.b
class Division(Calculator):
    def __init__(self,a,b):
        super().__init__(a,b)
        
    def calculate(self):
        if self.b==0:
            print("Division by 0 is not possible")

        else:
            return self.a/self.b


print("Welcome to a simple calculator")
p=int(input("Enter first number: "))
q=int(input("Enter second number: "))
print("Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division")
N=int(input("Enter a number of your choice from 1-4: "))
match N:
    case 1:
        o = Add(p, q)
        print("Sum is:", o.calculate())

    case 2:
        o = Subtract(p, q)
        print("Difference is:", o.calculate())

    case 3:
        o = Product(p, q)
        print("Product is:", o.calculate())

    case 4:
        o = Division(p, q)
        print("Division is:", o.calculate())

    case _:
        print("Invalid Choice")


#method overloading 
class Calculator:
    def add(self,*numbers): # *args-can take any number of arguments 
        print(sum(numbers))

c=Calculator()
c.add(2,3,4,9,8)

#constructor overloading is done using default parameter and *args

class Student:
    def __init__(self,*args):
        if len(args)==0:
            print("No data")
        elif len(args)==1:
            print("Name: ",args[0])
        elif len(args)==2:
            print("Name: ",args[0])
            print("Marks: ",args[1])

s=Student()
s1=Student("Palak")
s2=Student("Palak",95)

#overriding 
#Happens between child and parent class, parent method can be called using super()

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()
d.sound()

#decorator

def decorator(func):
    def wrapper():
        print("******")
        func()
        print("******")

    return wrapper

def greet():
    print("Hello")

greet=decorator(greet)
greet()

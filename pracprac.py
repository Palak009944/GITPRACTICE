class Dog:
    species="canine" # Class attribute
    def __init__(self, name, age):
        self.name = name #Instance attribute 
        self.age = age #Instance attribute

dog1=Dog("Tommy",3)
dog2=Dog("Jack",4)
dog3=Dog("Briar",6)

print(dog1.species)
print(dog2.species)
print(dog3.name,dog3.age)

#Example of inheritance 

class Animal:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping")

class cat(Animal):
    pass

class cow(Animal):
    pass 
c1=cat()
c1.eat()  #no print statement because the function called already has one
m1=cow()
m1.sleep()

#Example of Polymorphism 
#One method/function name, many behaviours

class Car:
    def speed_range(self):
        print("WARNING- overspeeding can be fatal")
        print("Maintain 40-60 Km/hr ")
class Truck:
    def speed_range(self):
        print("WARNING- overspeeding can be fatal")
        print("Maintain 60-80 Km/hr")

def show_speed(vehicle):
    vehicle.speed_range()

show_speed(Car())
show_speed(Truck())

#Example of Encapsulation 
#Encapsulation is the process of binding data (variables) and methods (functions) into a single unit (class) and controlling access to the data.

class BankAccount:
    def __init__(self):
        self.__balance=1000  #any variable starting with two underscores is a hidden variable or can't be accessed directly
    def show_balance(self):
        print(self.__balance) #the variable __balance can only be accessed through functions/methods
    
acc=BankAccount()
acc.show_balance()
#acc.__balance will show error

#Example of Data Abstraction
#Abstraction means hiding unnecessary details and showing only what the user needs.

class Jet:
    def start(self):
        print("Jet Started")

J1=Jet()
J1.start()

#The user will be displayed that JEt started and will not be shown how, this is abstraction



        


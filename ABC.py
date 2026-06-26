from abc import ABC, abstractmethod

class Animal(ABC):   #By inheriting from ABC, Animal became an abstract class
    @abstractmethod  #a decorator (a label that tells python that this method is compulsory)
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")
   

class Cat(Animal):
    def sound(self):
        print("Meow")

d=Dog()
d.sound()

c=Cat()
c.sound()


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("Area=",self.length * self.width)

R=Rectangle(34,45)
R.area()
    
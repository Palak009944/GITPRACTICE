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

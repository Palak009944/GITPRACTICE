from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


s = Square(4)
print("Square Area:", s.area())

r = Rectangle(5, 6)
print("Rectangle Area:", r.area())

#Program 2

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def __init__(self,name):
        self.name=name

    def start(self):
        print(self.name,"started.")

class Bike(Vehicle):
    def __init__(self,name):
        self.name=name

    def start(self):
        print(self.name,"started.")

car1=Car("BMW")
car1.start()
car1.stop()

bike1=Bike("Royal Enfield")
bike1.start()
bike1.stop()
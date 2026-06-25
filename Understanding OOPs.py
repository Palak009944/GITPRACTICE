class Car:
    def __init__(self,brand,model,year):  #to initialize the object
        self.brand=brand
        self.model=model
        self.year=year
    
    def introduce(self):       #function no.1
        print("Hello!")
        print("I am",self.brand)
        print("I was manufactured in",self.year)
    
    def start_engine(self):   #function no.2
        print(self.brand,self.model,"Engine started!")


c1=Car("Toyota","Corolla",2022)
c2=Car("BMW","X5",2024)
c1.introduce()
c2.introduce()
c1.start_engine()
c2.start_engine()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("My name is",self.name)
        print("I am",self.age,"years old")

class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course

    def study(self):
        print(self.name,"is studying",self.course)

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teach(self):
        print("Ms.Sharma is teaching",self.subject)

s1=Student("Palak",19,"CSE")
t1=Teacher("Ms.Sharma",40,"DSA")
s1.introduce()
s1.study()
t1.introduce()
t1.teach()
# need of @property
class Student:
    def __init__(self,marks):
        self.__marks=marks #the double underscore preceding marks makes the attribute private so that the particular attribute isn't directly accessible 

    def get_marks(self):   #method to access the marks
        return self.__marks
    
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks")

s=Student(90)

s.set_marks(150)
print(s.get_marks())
    

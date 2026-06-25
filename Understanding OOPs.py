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

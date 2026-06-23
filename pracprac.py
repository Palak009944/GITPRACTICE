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
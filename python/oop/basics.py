#it is clearly seen that self and obj is referring to the same object
 
from typing_extensions import Self


class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()

print("Address of obj is " , id(obj))


#Another self example

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print("Name : " , self.name)
        print("Age: ", str(self.age))


newPerson = person("Dush" , 25)

newPerson.show()

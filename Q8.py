#Create a Car Class
#Create a class named Car with:
#- brand
#- color
#Create 3 car objects and print their details.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
 
c1 = Car("Honda", "Red")
c2 = Car("Toyota", "White")
c3 = Car("Hyundai", "Black")
 
print(c1.brand, c1.color)
print(c2.brand, c2.color)
print(c3.brand, c3.color)
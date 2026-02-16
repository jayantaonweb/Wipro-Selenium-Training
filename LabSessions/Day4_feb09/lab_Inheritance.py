
#1.Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a= math.pi * self.radius* self.radius
        print("Area--> " , a)
    def perimeter(self):
        a= 2* math.pi * self.radius
        print("Perimeter-->",a)

c=Circle(7)
c.area()
c.perimeter()

#2.Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import  date
class Person:
    def __init__(self, name, country, dateOfBirth):
        self.name = name
        self.country= country
        self.dateOfBirth = dateOfBirth

    def Age(self):
        today = date.today()
        age = today.year - self.dateOfBirth.year
        return age


p1 = Person("Ram", "India", date(2011, 5, 10))
print("Name:", p1.name)
print("Country:", p1.country)
print("Age:", p1.Age())



#3.Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def show(self):
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


# Example
c = Circle(5)
s = Square(4)
t = Triangle(3, 4, 5)

c.show()
s.show()
t.show()


#4.Write a python program to create a child class Bus
# that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show_details(self):
        print("Vehicle Name:", self.name)
        print("Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 80, 12)

bus1.show_details()


#5.Write a python program to create  a Vehicle class
# without any variables and methods

class Vehicle:
    pass

v1 = Vehicle()
print("Vehicle object created:", v1)

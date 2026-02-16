#Lab 1: Method Overriding with Inheritance

#Create a base class Employee with a method calculate_salary().

#Create a subclass Manager that overrides calculate_salary() and adds a bonus.

#Demonstrate runtime polymorphism using parent class reference.

# Base class
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Subclass overriding the method
class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    # Overridden method
    def calculate_salary(self):
        return self.salary + self.bonus


# Runtime polymorphism using parent class reference
emp1 = Employee(30000)
emp2 = Manager(50000, 10000)

# Parent class reference list
employees = [emp1, emp2]

for emp in employees:
    print("Calculated Salary:", emp.calculate_salary())



#Lab 2: Polymorphism Using Function Arguments

#Create classes Dog, Cat, and Cow each with a method speak().

#Write a function animal_sound(obj) that calls speak().

#Pass different objects to the same function.

# Classes with same method name
class Dog:
    def speak(self):
        print("Dog says: Bark")

class Cat:
    def speak(self):
        print("Cat says: Meow")

class Cow:
    def speak(self):
        print("Cow says: Moo")


# Function using polymorphism (function arguments)
def animal_sound(obj):
    obj.speak()


# Creating objects
d = Dog()
c = Cat()
cw = Cow()

# Passing different objects to the same function
animal_sound(d)
animal_sound(c)
animal_sound(cw)


#Lab 3: Multilevel Inheritance with Polymorphism

#Create Vehicle → Car → ElectricCar.

#Each class overrides the method fuel_type().

#Call the method using different object references.

# Base class
class Vehicle:
    def fuel_type(self):
        print("Vehicle uses general fuel")


# Intermediate class
class Car(Vehicle):
    def fuel_type(self):
        print("Car uses Petrol/Diesel")


# Derived class
class ElectricCar(Car):
    def fuel_type(self):
        print("Electric Car uses Electricity")


# Creating objects
v = Vehicle()
c = Car()
e = ElectricCar()

# Calling method using different object references (polymorphism)
objects = [v, c, e]

for obj in objects:
    obj.fuel_type()

#Lab 4: Operator Overloading

#Create a class BankAccount with attribute balance.

#Overload + to add balances and > to compare balances.

#Demonstrate polymorphic behavior of operators.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Overloading + operator
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    # Overloading > operator
    def __gt__(self, other):
        return self.balance > other.balance

    def display(self):
        print("Balance:", self.balance)


# Creating objects
acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

# Using overloaded + operator
acc3 = acc1 + acc2
acc3.display()

# Using overloaded > operator
if acc1 > acc2:
    print("Account 1 has greater balance")
else:
    print("Account 2 has greater balance")


#Lab 6: Multiple Inheritance and MRO

#Create classes A, B, C, and D (diamond structure).

#Override the same method in B and C.

#Call method using D object and observe MRO.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("class c")

class D(B,C):
    pass
    #print("class D")

d=D()
d.show()
print(D.mro())

#Lab 7: Polymorphism with Exception Handling

#Create Calculator class with divide().

#Create SafeCalculator that overrides divide() and handles ZeroDivisionError.

#Demonstrate method overriding.

# Base class
class Calculator:
    def divide(self, a, b):
        result = a / b
        print("Result:", result)


# Derived class overriding method with exception handling
class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            result = a / b
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")


# Creating objects
calc = Calculator()
safe_calc = SafeCalculator()

# Demonstrating method overriding
calc.divide(10, 2)        # Normal division
safe_calc.divide(10, 2)   # Safe division
safe_calc.divide(10, 0)   # Exception handled


#Lab 8: Real-Time Payment System

#Create base class Payment with method pay().

#Create CreditCard, UPI, and NetBanking subclasses.

#Use a single function to process all payments.

# Base class
class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)


# Subclasses
class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class NetBanking(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")


# Single function to process all payments (polymorphism)
def process_payment(payment_method, amount):
    payment_method.pay(amount)


# Creating objects
p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

# Processing payments using the same function
process_payment(p1, 1000)
process_payment(p2, 500)
process_payment(p3, 2000)
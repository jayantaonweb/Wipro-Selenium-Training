# constructor- first function of the class when an object of the class is created
# syntax __init__()
# we can parameterized the constructors
# self is mandatory




class Student:
    def __init__(self):
        print("constructor is called ")

    def addSum(self):
        print("Adding 2 nums")
s1 = Student()
s1.addSum()

# parameterized constructor

# self.name is a instance variable or global variable(which belongs to object)
# name is a local parameter (exist inside the method)
# if we don't assign it to self.name object will not remember the value
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name--->",self.name,"\nSalary--->", self.salary)

e1 = Employee("Ram", 956552)
e2 = Employee("Jayanta", 6945544)

e1.display()
e2.display()


# using * argument in constructor


class Numbers:
    def __init__(self, *args):
        self.values = args


n = Numbers(10, 20, 30)
print(n.values)

m = Numbers(3, 4)
print(m.values)

p = Numbers(3)
print(p.values)



# parent and child constructor
# super keyword for accessing parent constructor
# calling Parent constructor
class Parent:
    def __init__(self):
        print(
            "I am the parent constructor"
        )

class child1(Parent):
    def __init__(self):
        super().__init__()
        print("i am the child1 constructor")
c = child1()

class child2(Parent):
    def __init__(self):
        super().__init__()
        print("i am the child2 constructor")
c = child2()


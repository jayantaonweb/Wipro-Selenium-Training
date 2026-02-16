# polymorphism means taking many forms

# same method / function name will behave differently depending on the
#object type
# input arguments
# class implementations

print(len("python"))
print(len([1,2,3]))
print(len({1,2,3}))

# input arguments no. of arguments / data types

class Calculator:
    def add(self, a , b=0, c=0):
        return a+b+c

c= Calculator()
print(c.add(10))
print(c.add(5,8))
print(c.add(4,5,6))


# run time polymorphism is supported
# achieved method overriding - child class method will override the parent class method

class Animal:
    def sound (self):
        print("animal make sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

a= Dog()
a.sound()
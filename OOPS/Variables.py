# variables = used to store the data
# instance variable - global variable at the class level
# local variable - inside the method only

# instance variable example

class Student:
    school = "D.A.V PS"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        schoolcity = "ARA"

        print(self.name,self.marks)
        print(self.school)
        print(schoolcity)

s1 = Student("Jayant", 88)
s2 = Student("Shyam",90)

s1.show()
s2.show()

class Employee:
    company = "Wipro"
e1 = Employee()
e2 = Employee()
print(e1.company)
print(e2.company)
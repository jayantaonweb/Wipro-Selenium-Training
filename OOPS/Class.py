# class is a blueprint or a template
# which describes the state / behaviour of its object

# data is put in variable
# behaviour is put in function

class Student:

    #data or properties
    studentName= "Ravi"
    studentID = 45425

    # self is used to access the attribute of the class we have defined
    # it is automatically loaded
    # self represent the instance of the class

# create a function to access the data

    def displayStudentDetail(self):
        print(self.studentName)
        print(self.studentID)

#create the object of the class
a= Student()
a.displayStudentDetail()



# Destructor - when we want to destroy the object
# post conditions closing of the browser , db connection closing, releasing of certain resource
# clean up operation
# for proper memory usage destructor should be used
# when db connection has to be closed -
# free the memory (garbage collection) which is automatically called
from pythonPrograming.Comp import active_employees


class Destructor:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("Closing the db collection")

a = Destructor()
print("End of the Program")
del a


# destructor in file handler

class Filehandler:
    def __init__(self,filename):
        self.file = open(filename ,'w')
        print("File is opened ")
    def readFile(self,filename):

        print("Reading the File ")

    def __del__(self):
        self.file.close()
        print("file Closed")

f= Filehandler("Test.txt")
f.readFile("Test.txt")
del f





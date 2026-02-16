# default Method





class Calculator:
    def add(self,a,b):
        print(a+b)
c=Calculator()
c.add(10,20)
c.add(2,5)

# default Parameter
class test:
    def run(self, browser = "chrome"):
        print("Running on ", browser)

t= test()
t.run()
t.run("firefox")


# *args parameterized method

class Numbers:
    def total (self, *args):
        print(sum(args))

n= Numbers()
n.total(10,5)
n.total(5)
n.total(45,62,45)
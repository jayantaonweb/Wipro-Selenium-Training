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
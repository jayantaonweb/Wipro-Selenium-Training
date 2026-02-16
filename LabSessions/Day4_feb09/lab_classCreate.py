#Create a class Book with attributes title and author.
#Create 3 different book objects and print all details.
class Book:
    def __init__(self, title,author):
        self.title=title
        self.author=author
    def show(self):
        print("title-->",self.title,"\n Author---> ",self.author)
a= Book("Science","NCERT")
b= Book("Mathematics", "R.S. Aggarwal")
c= Book("Social science", "NCERT")

a.show()
b.show()
c.show()

#Create a class Rectangle with a constructor that takes length and width
# and stores area and perimeter as object attributes.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width =width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return  2*(self.length+self.width)

r= Rectangle(54,32)

print(r.perimeter())
print(r.area())


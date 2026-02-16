#function are the block of code that perform specific task
from pythonPrograming.iter import value


#default function with no parameters
def printdata():
    print("hello world")

# calling the function
printdata()

#function with parameters
def printdata(name):
    print("hello",name)

# pass the argument
printdata("Ram")
printdata("Shyam")

#return statement
#to return the function value return statement is used

def sq (num):
    result = num*num
    return result

#function call
print('square:',sq(3))

#function pass
def func_pass():
    pass
#call the function
func_pass()

# multiply return values

def cal(a,b):
    return a+b, a-b, a*b

add,sub,mul =cal(46,5)
print (add)
print(sub)
print(mul)

def areaofrect(length , width):
   return length *width

def areaofsq(side):
    return side*side

value1 = areaofrect(4,10)
square=areaofsq(value1)

print(square)

def even (limit):
    for i in range (2,limit+1,2):
        print(i)
even(10)

#function with if else cond
def even (limit):
    if limit%2 == 0:
        return "even"
    else:
        return "odd"

print(even(10))
print(even(11))






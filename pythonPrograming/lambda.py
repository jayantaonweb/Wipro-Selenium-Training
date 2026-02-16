#function - function name , argument , return type, body code
from math import lgamma
from xmlrpc.server import list_public_methods


#lambda function - anonymous (nameless ) functions,one line , simple operations
# syntax lambda arguments : expression
# it can have any number of arguments
# must have only one expression
#the expression is automatically returned

#normal function add 2 number

def add(a,b):
    return a+b
print (add(3,4))

# lambda function

add = lambda a,b:a+b
print (add(3,4))

# square of a number
square= lambda x:x*x
print(square(4))

#check if even or not
even = lambda x:x%2==0
print(even(5))

# find the max of 2 nums

max = lambda a,b:a if a>b else b
print(max(8,7))


#filter , map and reduce in built function in lambda

# filter - select data - filtering the data
# map - transfer the data
# reduce - aggregate the data

#filter
numbers = [1,2,3,4,5,6]

even = list (filter(lambda x:x%2==0, numbers))
print(even)

# filter the failed test cases

status =['pass','fail','pass','fail']
failed= list(filter(lambda s:s=='fail', status))
print(failed)

#filter + ve numbers
nums=[-5, 10, -3, 7, 0, 2]
print(list(filter(lambda x:x>0,nums)))

#Filter non-empty strings
data = ["hello", "", "world", "", "python"]
print(list(filter(lambda x:x!="",data)))



# reduce -aggrigate -combining many values to a single result

from functools import reduce
nums=[10,20,30,40]
print (reduce(lambda x,y:x+ y, nums))

#multiply , maximum value, minimum value

#multiply
print(reduce(lambda x,y:x*y,nums))
# maximum value
print(reduce(lambda x,y:x if x>y else y,nums))
#minimum value
print(reduce(lambda x,y:x if x<y else y,nums))


#Map - transform the data - the function is applied to every element

nums =[10,20,30,40]

square = list (map(lambda x:x*x,nums))
print(square)


#sorting in lambda

data = [(1,3), (4,5), (2,2)]
sorteddata=sorted(data, key = lambda x:x[0])
print(sorteddata)

marks= {"A":75, "B":90, "C":60}
sorted_marks= dict(sorted(marks.items(),key = lambda x:x[1]))
print(sorted_marks)
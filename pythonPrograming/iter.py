#iter() method
#create a iterator from a iterable

#iteration - looping in the collection of item

a=[10, 20, 30, 40, 50]
#convert the list into a iterator

iterator = iter(a)


#next () allow the user to access the elements

print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))

#convert the string to a iterator
s= "hello"
iterator = iter(s)
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))

#convert the dict into a iterator
a={1:'a',2:'b',3:'c'}
iterator = iter(a)
print (next(iterator))
print (next(iterator))
print (next(iterator))

#for loop to iterate
for key in iterator:
    print(key)

a={1:'a',2:'b',3:'c'}

for key,value in a.items():
    print(key,"->",value)


#iter(callable, sentinel)

def get_input():
    return input ("inter value:")

for it in iter(get_input,"Quit"):
    print(it)





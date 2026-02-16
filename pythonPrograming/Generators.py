# generators - special type of function - return one value at a time , on demand

# yeald -
# memory  efficient
# use full set of data
# file , retries, batching

# normal function

def number():
    return [1,2,3,4]

print (number())
# normal function loads all the values into memory

# generator

def generator ():
    print("printing 1")
    yield 1
    print("printing 2")
    yield 2
    print("printing 3")
    yield 3
    print("printing 4")
    yield 4

ret_value = generator()
print(next(ret_value))
print(next(ret_value))
print(next(ret_value))

#Q1 What is the output?

list(enumerate(['a', 'b', 'c']))
#0 a, 1 b, 2 c

#Q2 What is the output?

for i, v in enumerate([10, 20, 30]):
    print(i, v)
 #0 10 , 1 20, 2 30


#Q3 Write code to print index + value from:
 #Index should start from 1.
colors = ['red', 'green', 'blue']
for i, v in enumerate(colors):
    print(i,v)

#Q4 What is the output?

list(enumerate("PYTHON", start=1))

# 0 P, 1 Y, 3 T, 4 H, 5 O, 6 N


#Q5 Find the index of value 50 using enumerate():

nums = [10, 20, 30, 40, 50, 60]
for i,v in enumerate(nums):
    if v==50:
        print(i)

#Q6 What is the output?

for i, n in enumerate(range(10, 60, 10)):
    print(i, n)
 #  0 10, 1 20, 2 30, 3 40, 4 50


#Q7 Convert this into an enumerate() loop:

#for i in range(len(data)):
#    print(i, data[i])

for i,v in enumerate("data"):
    print(i, v)


#Q8 What is printed?

items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)
 # 0, 1, 2

#Q9 What is the output?

list(enumerate([], start=5))

#Q10 What is the output?

for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)
 # -1 100, 0 200, 1 300


#Q11 What happens here?

#i, v = enumerate(['x', 'y', 'z'])
#value error
#Q12 Explain the difference:

#enumerate(data)


#enumerate(data, start=1)
#1.Write a Python function to check whether a number falls within a given range.

num=input()
for i in range(0,101):
    if i== num:
        print("found")
    else:
        continue


#2. Write a Python function to Print even numbers from 1 to 50

for i in range (1,51,1):
    if i%2==0:
        print(i)

#3. Write a Python function to Sum of numbers from 1 to 100

A=0
for i in range(1,101,1):
    A=A+i
print(A)


#4. Print all numbers divisible by 5 between 1 and 100

for i in range(0,101,1):
    if i%5 ==0:
        print (i)


#5.Create a list of numbers from 50 to 100 with a step of 5


print(list(range(50,101,5)))

#6. Print the square of each number from 1 to 10.


for i in range (0,11):
    print(i*i)


#7. Print numbers between -10 and 10.

for i in range (-10,11):
    print(i)
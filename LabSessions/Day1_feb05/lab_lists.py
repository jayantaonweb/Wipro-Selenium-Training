#Write a Python program to get the largest number from a list.

numbers=[1,2,3,4,3,6,7,8,4,7,3,9,55,7,23]
numbers.sort()
print(numbers[len(numbers)-1])

#remove the even numbers from the list
for i in numbers[:]:
    if numbers[i] % 2==0:
        numbers.pop(i)
print(numbers)

#multiply the items in the list
numbers=[1,2,3,4,3,6,7,8,4,7,3,9,55,7,23]
product=1
for i in numbers:
    product = product * numbers[i]
print(product)


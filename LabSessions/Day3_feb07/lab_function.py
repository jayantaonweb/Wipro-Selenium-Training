#1.Write a Python function to sum all the numbers in a list.

def sum_list(num):
    sum=0
    for i in num:
        sum+=i

    return sum
list1=[5,6,7,8]
print(sum_list(list1))

#2.Write a Python function to find the maximum of three numbers.

def max(x,y,z):
    large=x
    if y>large:
        large=y
    if z>large:
        large=z
    return large
print(max(5,8,1))
#Create a custom iterator that prints numbers from 1 to 5.

num = [1,2,3,4,5]
iterator = iter(num)
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))


#Write an iterator class that returns next even number.

num = [1,2,3,4,5,6,7,8,9]
iterator = iter(num)
for i in num:
    if i%2==0:
        print(next(iterator))





#Explain and demonstrate the use of __iter__() and __next__().
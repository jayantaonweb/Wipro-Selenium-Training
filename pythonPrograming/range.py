#all the numbers should be integer only

# step size cannot be zero
# start - default 0


#fetch values at index

a= range(5)
print(a[1])
print(a[3])

a1=range (2,5)
print(a1[1])


#for loop for range
a= range(2,5)
for i in a:
    print(1)

#for loop for range of 3 arguments
a= range(2,5,3)
for i in a :
    print(i)

#for loop for range of negative 3 arguments
a= range(2,15,-3)
for i in a :
    print(i)

#for loop for range of 3 arguments with step size zero
#a= range(2,15,0)
#for i in a :
 #   print(i)


#reverse counting

a= range(15,2,-1)
for i in a :
    print(i)


#scenario : allow 3 login attempt
for attempt in range (3):
    pin = input ("Enter the Pin:")
    if pin == "1234":
        print("Access Granted ")
        break
    else:
        print("Try again")

# scenario : Apply discount in the position (index) of the item
price = [100, 200, 300, 400]
for i in range (len(price)):
    if i % 2 == 0 :
        print ("discount given at index "+ i)

#scenario :  Simulate polling every second for 10 second

import time



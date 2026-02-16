#Q1
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
#From a list of numbers:
#Filter even numbers
print(list(filter(lambda x:x%2==0,nums)))
#Square them
print(list (map(lambda x:x*x,nums)))
#Find their sum
print(reduce(lambda x,y: x+y,nums))

#2.
salaries = [25000, 40000, 32000, 18000]
#from a list of salaries:
#Filter salaries > 30,000
higher_salaries=list(filter(lambda x:x>30000,salaries))
print(higher_salaries)
#Add 10% hike
hike=list(map(lambda x:x*1.10,higher_salaries))
print(hike)
#Find the total payout
print (reduce(lambda x,y:x+ y,hike))
#Total payout fo hiked salaries


#1.Write a Python program to sort a list of tuples using Lambda
data = [(1,3), (4,5), (2,2)]
sorteddata=sorted(data, key = lambda x:x[0])
print(sorteddata)

#2.Write a Python program to extract year, month, date and time using Lambda.
from _datetime import datetime
now = datetime.now()
print(now)

#print(map(lambda x: (x.year, x.month, x.day, x.strftime("%H:%M:%S")),now))
extract = lambda x: (x.year, x.month, x.day, x.strftime("%H:%M:%S"))
year, month, date, time = extract(now)

print("Year :", year, "Month:", month, "Date :", date, "Time :", time)


#3.Write a Python script to concatenate the following dictionaries to create a new one.
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3}
d3 = {'d': 4}
new_dict={}
new_dict.update(d1)
new_dict.update(d2)
new_dict.update(d3)
print(new_dict)

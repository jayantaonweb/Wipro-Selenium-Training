#Create a dictionary with student roll number as key and name as value. Print the dictionary.
from itertools import count

Student = {1:"Ram",2:"Shyam",3:"Sita",4:"Geeta"}
print(Student)

#Create an empty dictionary and add 5 key-value pairs dynamically.
name={}
name.update({1:"Ram",2:"Shyam",3:"Sita",4:"Geeta",5:"Jayant"})
print(name)

#Access the value of a key that exists and one that does not exist (handle safely).

print(name[5])
print(name.get(10))

#Update the value of an existing key in a dictionary.

name.update({2:"Mohan"})
print(name)

#Delete a key from a dictionary using:
#del
#pop()
del name [3]
print(name)

name.pop(4)
print(name)

#Find the number of key-value pairs in a dictionary.
print(len(name))

#Print only:
#keys
print(name.keys())
#values
print(name.values())
#key-value pairs
print(name.items())
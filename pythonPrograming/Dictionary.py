#dictionary items - key value
#similar to lists and tuples
#for integers , tuples and strings - keys must be immutable
#list can not be used in the key for the dict as it is mutable in nature

country = {
    "india": "Delhi",
    "canada": "Ottawa",
    "England": "London"
}
print(country)

#access values with key
print(country["canada"])

#add elements
country["italy"]="Rome"
print(country)

#remove element
del country["india"]
print(country)


#itrate among dict
for coun in country:
    print(coun)

#length of dict
print(len(country))


#clear
country.clear()
print(country)








#integer as a key
my_dict = {1:"one", 2:"two",3:"three"}
print(my_dict)

my_dict ={1:"one", 2:"two",3:"three", 1:"four"}
print(my_dict)

#tuple as a key

my_dict={(1,2):"one two",3:"three",3:"four"}
print(my_dict)

#list as a key

#my_dict = {1: "hello", [1,2]:"there you"}
#print(my_dict)



my_dict = {1:"one", 2:"two",3:"three"}
print(my_dict)

#pop()
my_dict.pop(1)
print(my_dict)

#update()
my_dict.update({1:"one"})

#key()
print(my_dict.keys())

#value()
print(my_dict.values())

#popitem()
my_dict.popitem()
print(my_dict)

#copy
A=my_dict.copy()



#dict inside a list

employes=[
    {"id":1, "name":"Jayant", "role":"QA"},
    {"id":2, "name":"Ram", "role":"Dev"},
    {"id":3, "name":"Jay", "role":"Manager"}
]

print(employes[0])
print(employes[0]["name"])


for emp in employes:
    print(emp["name"], emp["role"])

employes.append({"id":4, "name":"Sita", "role":"Tester"})
print(employes)

employes.pop(0)
print(employes)


#seach in the list
for emp in employes:
    if emp["name"]=="Jayant":
        print(emp)

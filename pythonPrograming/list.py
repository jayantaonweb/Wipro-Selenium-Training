from pythonPrograming.enums import fruit

empty_list =[]
numbers=[1,2,3,4,3,6,7,8]
mixeddata = [1,"hello", True , 6.67,1 ]
nested = [[1,2],[3,4]]

#accessing the list (indexing concept)
print(mixeddata[1])
print(mixeddata[2])

#modifying data
mixeddata[4]=6
print(mixeddata)

#add data at index

mixeddata.insert(5,10)
print(mixeddata)
#add data at the end
mixeddata.append("jhon")
print(mixeddata)


#remove data
mixeddata.remove("hello")
print(mixeddata)

mixeddata.pop()#LAAST ELEMENT
print(mixeddata)

mixeddata.pop(1)# at index
print(mixeddata)

#list methods
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.count(3))

print(numbers.index(3))

numbers.clear()
print(numbers)



fruits = ["apple","banana","cherry"]
for item in fruits:
    print(item)


for i , fruit in  enumerate(fruits):
    print(i,fruit)

#slicing -access a portion of list
my_list=['p','r','0','g','r','a','m']
print("my_list=" , my_list)

#get the list woth items from 2 to 5 (n-1)
print(my_list[2: 5])
#from index 5 to last (n)
print(my_list[5: ])

#from first item to last item
print(my_list[:])



#extend

numbers=[1,3,5]
even_numbers=[2,4,6]
#adding elements of one list to another
numbers.extend(even_numbers)
print(numbers)


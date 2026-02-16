#enumerate with list

fruits= ["orange","cherry","kiwi"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

#enumerate with start value changed
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


#enumerate with strings
word = "python"
for i, ch in enumerate(word):
    print(i,ch)

for i, ch in enumerate(word,start=2):
    print(i,ch)


#enumerate with tuples

fruits= ("orange","cherry","kiwi")

for index,fruit in enumerate(fruits):
    print(index,fruit)


#real time scenario

test_cases = ["login", "signup","checkout"]
for case_no,test in enumerate(test_cases,start=1):
    print (f"executing testcase {case_no}: {test}")



#accessing of the enumerate values
a=['God','is', 'greate']
b=enumerate(a)
nxt_val=next(b)
print(nxt_val)



#duplicate detection using enumerates
characters = ["Krillin", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]

character_map = {character: [] for character in set(characters)}

for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)





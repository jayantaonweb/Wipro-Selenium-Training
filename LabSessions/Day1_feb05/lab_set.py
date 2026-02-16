std_id = {112,113,114,115,115,116,117,5,9}
std_id.add(55)
print(std_id)

a={3,24,133,114,115,116,23}

b=std_id.copy()
std_id.clear()
print(std_id)
print(b)

b.pop()
print(b)

print(b.pop())


b.remove(115)
print(b)


print(a.symmetric_difference(b))

print(a.symmetric_difference_update(b))

print(a.intersection(b))
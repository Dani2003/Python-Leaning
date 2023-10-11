# Creating sets in pyhton
from turtledemo.chaos import f

a = set()

#adding values to the sets

a.add(1)
a.add(2)
a.add(3)
a.add(4)
#printing the value
print(a)
#for removing a element u just add the .remove(element)
a.remove(4)
print(a)

print(f"the set has {len(a)} elements")
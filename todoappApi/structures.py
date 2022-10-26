# list 

names = ['joseph', 'Isaac', 'Alex', 'Emerald']

print(names)

# list indexing
first_person = names[0]
second_person = names[1]

print(first_person)
print(second_person)

# list manipulation
# adding to a list, append method, insert method, addition method
names.append('Sarah')
print(names)

# insert method .insert(where to add new item, new item to be added): Output: None;
names.insert(1, 'Peculiar')
print(names)
names.insert(2, 'victoria')
print(names)

# adding multiple names to the list.
mul_names = ['Ade','Fatima', 'Aina']
names += mul_names
print(names)

# removing item in the list
# pop method, remove method, del command
 
del names[-3] #delete command
print(names)

names.remove('victoria')#remove method
print(names)

# pop method
poped_name = names.pop(0)
print(names)
print(poped_name)

names.insert(0, poped_name)
print(names)

# modify a list
names[0] = 'Osezele'
print(names)

# length of the list
print(len(names))

# Tuples 

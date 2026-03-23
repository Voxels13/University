#1.Create and Access Dictionary Elements
#2.Update Dictionary
#3.Removing Elements
#4.Merging Dictionaries

#Dictionaries are mutable (after Python 3.7+) key:value pairs stored within {}, In a dictionary, the keys must be unique and the values can be the same, the keys should always be immutable type , such as , string, num, tuple , etc.

#1

#Creating a dictionary

dict1={'Name':'John', 'Age':25,'Job': 'Salaryman'}

print(dict1)

#Accessing Elements of a dictionary

#We can access the elements through the keys, display all values or all keys as:

print(dict1['Name'])
print(dict1['Age'])
print(dict1['Job'])
print(dict1.keys())
print(dict1.values())

#Using loops to iterate through the dictionary

for i,j in zip(dict1.keys(),dict1.values()):
    print (f"{i}:{j}")


#2.Updating Dictionaries

#You can either update or add new key:value pairs to the existing dictionary using (dictionary_name)[key] = value as:

dict1['Salary'] = 10000

print(dict1)

#You can replace the value of an existing key by overwriting the value with the same key

dict1['Name'] = 'Bob'

print(f"After making changes to 'Name' key, we get :\n{dict1}")


#3

#For deleting key:value pairs from a dictionary, we can use , del, pop() and clear()

#del: (If you do -- del(dict1) --> The whole dictionary is gone and you will get an error if you try to output)

#if you want to delete a specific key --> del(dict_name(key_name))


del(dict1['Name'])


#pop():  dict_name.pop(key_name)

print(dict1.pop('Age')) #--> Removes the key and returns the value of the deleted key

print(dict1)

#clear()

dict1.clear() #--> Clears the entire dictionary

print(dict1)


#4

#WE can merge two dictionaries tgt using the update method as:

dict2={'Department':'Sales', 'Area':'Ohio','Season': 'Summer'}

dict1.update(dict2)

print(dict1)

#using |=

dict1 |= dict2

print(dict1)

#Unpacking

a,b,c = {**dict1}

print(f"After Unpacking || a = {a},b = {b},c = {c}")

#Using unpacking to merge

dict3 = {**dict1,**dict2}

print(dict3)
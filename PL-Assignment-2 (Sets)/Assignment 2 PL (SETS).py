#1. Creating and Acessing Sets
#2. Union of elements
#3. Intersection of elements
#4. Difference of the elements

#1. Sets are created by enclosing a set of non duplicate values within {} or by using the set() function
   # Sets are mutable and unordered data structures

set1= {1,2,3,4,5,1}
#OR
set2= set(map(int,input("Enter the values for a set of integers:").strip().split()))

print(f"Set1 = {set1}")
print(f"Set2 = {set2}")

#Accessing elements

set2= {1,2,3,4,5,1}

#You can access the elements of a set only through indexing (this is because, since a set is unordered, the value at the indexes change each time the prog is executed)

for i in set2:
    print(i,end=' ')
print()

#Union of Elements |

set2={2,3,4,5}
set3={'a','b','c',6}

print(set2|set3)

#Intersection of Elements of two sets --> &
#For no intersetion, it returns set()

set2={2,3,4,6}
set3={'a','b','c',6}

print(set2&set3)

#Difference of the elements of the two sets

set2={2,3,4,6}
set3={'a','b','c',6}

print(set2-set3)


#Removing elements from a set

set2.remove(3) #REmoves first occurence of given value
set2.pop() #Removes the first element
set2.discard(7) #Removes the first occurence of the given value and dosent return an error in case of missing value
print(set2)

#Adding elements to a set 

#Use add function --> set_name.add(value)

set1={1,2,3,4}
set1.add(9)

print(set1)
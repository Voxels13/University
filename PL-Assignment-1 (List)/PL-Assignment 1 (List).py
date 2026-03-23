#1. Create and access list elements
#2. Add and Remove list elements
#3. Sort list element
#4. Reverse list element


#1.

#We can create lists by encasing elements within square brackets or by using the list function

list1= [1,2,3,4,5]
#OR
list2 = list(map(int,input("Enter list of integers:").strip().split()))

print(list1,list2)

#Accessing
#Through their indexes AND by slicing

list1=[1,2,3,4,5,6,7]
print(list1[3:-1])
print(list1[5])


#2.

#WE can add elements to a list through their index/ concatenation 

list1=[1,2,3,4]
list1 = list1+[5]
list1.insert(len(list1),6) #insert ( index, value ) --> TO insert at the end of the list, use len(list)
list1[-1] = 7              #We remove the previous value and replace it with this value

print(list1)

#We can remove elements from a list using pop() and remove()

#remove(value)--> Removes / deletes the first incidence of the given value (dosent take in an index)
#pop()--> pop( index ) {By default i.e, pop() , removes the last element of the list}

list1=[1,2,3,4,5,6,7]
list1.remove(5)
print(list1)


#3.

#To sort , we can use sort() or sorted() {easy ways}

#sort sorts the list then and there and does not require a new list to be created
#sorted requires a new list to be created


#for sort()  --> list_name.sort()
#for sorted() --> sorted(list_name)

list1 = [2,4,3,1,6]
list1.sort()

list1 = [2,1,4,3,9,6,5,8]
sorted_list1 = sorted(list1)
print(sorted_list1)

#4.

#Strings can be reversed either through their indexes or by using the reverse() method

#reverse --> list_name.reverse()

list1=[1,2,3,4,5,6,7,8,9,10]
list1.reverse()

list1=[1,2,3,4,5,6,7,8,9,'a','b','c']

if 1 in list1:
    print("YES")
print(list1[::-1])

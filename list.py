#list 

#ordered
#mutable 
#allows duplicate elements
#heterogeneous elements
#indexed
#dynamic size


from numpy import sort


data = [10, "Ayu", 20.5, True, 10, "Ayu"]
print(data)

# creating list 

#empty list
list1 = []
list2 = list()


#list with elements
list3 = [10, 20, 30, 40, 50]
#list with constructor
list4 = list((10, 20, 30, 40, 50))
print(list4)

#using range 
list5 = list(range(10))
print(list5)

#nested list
list6 = [10, 20, [30, 40], 50]
print(list6)

#list indexing
print(list6[2][1]) #40

#negative indexing
print(list6[-2][-1]) #40

#list slicing
print(list6[1:3]) #[20, [30, 40]]

#list slicing with step
#list[start:stop:step]

print(list6[::2]) #[10, [30, 40]]

#: Slicing creates a new list (a shallow copy), not a new reference to the original list

#modifying list elements
list6[2][0] = 100

#modifying list elements using slicing
list6[1:3] = [200, 300]

#replacing with different number of elements
list6[1:3] = [400, 500, 600]
#output: [10, 400, 500, 600, 50]

#list methods 
#append() - adds an element to the end of the list
list6.append(700)

#extend() - adds multiple elements from an iterable to the end of the list
list6.extend([800, 900])

#insert() - adds an element at a specific index insert(index, element)
list6.insert(1, 1000)

#remove() - removes the first occurrence of an element from the list
list6.remove(1000)

#pop() - removes and returns the element at a specific index (default is the last element)
lastElm = list6.pop() #removes last element
print(lastElm) #900

#pop with index
secondElm = list6.pop(1) #removes element at index 1
print(secondElm) #1000

#clear() - removes all elements from the list
list6.clear()
print(list6) #[]

#index() - returns the index of the first occurrence of an element
list7 = [10, 20, 30, 40, 50]
index = list7.index(30)
print(index) #2

#count() - returns the number of occurrences of an element
count = list7.count(20)
print(count) #1

#sort() - sorts the list in ascending order
list8 = [50, 20, 30, 10, 40]
list8.sort()
print(list8) # [10, 20, 30, 40, 50]

#descending order
list8.sort(reverse=True)

#sort using custom key
list9 = ["apple", "banana", "cherry", "date"]
list9.sort(key=len)
print(list9) # ['date', 'apple', 'banana', 'cherry']

#reverse() - reverses the order of the list
list9.reverse()
print(list9) # ['cherry', 'banana', 'apple', 'date']

#copy() - returns a shallow copy of the list

list10 = list9.copy()
list10.append("fig")
print(list9) # ['cherry', 'banana', 'apple', 'date']
print(list10) # ['cherry', 'banana', 'apple', 'date', 'fig']

list10[0] = "grape"
print(list9) # ['cherry', 'banana', 'apple', 'date']

print(list10) # ['grape', 'banana', 'apple', 'date']


#differnce between append, extend and insert
#append adds the entire object as a single element to the end of the list
a = [1, 2, 3]
a.append([4, 5])
print(a) # [1, 2, 3, [4, 5]]

#extend adds each element of an iterable to the end of the list
list11 = [1, 2, 3]
list11.extend([4, 5])
print(list11) # [1, 2, 3, 4, 5]

#insert adds an element at a specific index
list12 = [1, 2, 3]
list12.insert(1, 10)
print(list12) # [1, 10, 2, 3]
# insert(2,5,6) - this will give error because insert takes only 2 arguments, index and element

# insert() accepts one index and one object. The object itself can be a list, tuple, dictionary, or another data type.


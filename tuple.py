#tuple
#immutable - cannot be changed after creation
#ordered - maintains the order of elements
#ordered - maintains the order of elements
#duplicate elements - allows duplicate elements
#different data types - can contain elements of different data types


numbers = (10, 20, 30, 40, 50)
print(numbers) #(10, 20, 30, 40, 50)


# number[0] = 100 #TypeError: 'tuple' object does not support item assignment

#creating tuple

#using parentheses
numbers1 = (10, 20, 30, 40, 50)

#without parentheses
numbers2 = 10, 20, 30, 40, 50
print(numbers2) #(10, 20, 30, 40, 50)

#using tuple constructor
numbers2 = tuple((10, 20, 30, 40, 50))
print(numbers2) #(10, 20, 30, 40, 50)


#creating tuple with single element
single_element_tuple = (10,)


#accessing tuple elements using indexing
print(numbers1[0]) #10

#accessing tuple elements using negative indexing
print(numbers1[-1]) #50

#accessing tuple elements using slicing
print(numbers1[1:4]) #(20, 30, 40)

#accessing tuple elements using slicing with step
print(numbers1[::2]) #(10, 30, 50)

#accessing tuple elements using slicing with for loop 
tuple1 = (10, 20, 30, 40, 50)
for i in tuple1:
    print(i) #10, 20, 30, 40, 50

#iterating over tuple using enumerate() - returns both index and value
tuple1 = (10, 20, 30, 40, 50)
for index, value in enumerate(tuple1):
    print(index, value) #0 10, 1 20, 2 30, 3 40, 4 50


#tuple packing and unpacking

#packing - combining multiple values into a single tuple
packed_tuple = 10, 20, 30, 40, 50

print(packed_tuple) #(10, 20, 30, 40, 50) - python automatically packs the values into a tuple

# tuple unpacking - extracting values from a tuple into individual variables
student = ("Ayu", 20, "Female")
name, age, gender = student

print(name) #Ayu
print(age) #20
print(gender) #Female

# the number of variables on the left side must match the number of elements in the tuple on the right side, otherwise it will raise a ValueError

# tuple unpacking using * operator - allows us to unpack a tuple into multiple variables, with one variable capturing the remaining elements as a list
numbers = (10, 20, 30, 40, 50)
a, *b, c = numbers
print(a) #10
print(b) #[20, 30, 40]
print(c) #50


# built in tuple methods

#count() - returns the number of occurrences of a specified element in the tuple
numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.count(20)) #3

#index() - returns the index of the first occurrence of a specified element in the tuple
numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.index(20)) #1


#convert tuple to list
temp_list = list(numbers)
print(temp_list) #[10, 20, 30, 20, 40, 20, 50]

# deleting tuple 
del numbers

# nested tuple

data = (10, 20, (30, 40), 50)
print(data) #(10, 20, (30, 40), 50) 

#tuple containing mutable elements

data = (10, 20, [30, 40], 50)
data[2][0] = 100
print(data) #(10, 20, [100, 40], 50) 


#returing multiple values from a function using tuple
def get_student_info():
    name = "Ayu"
    age = 20
    gender = "Female"
    return name, age, gender #returns a tuple
print(get_student_info()) #('Ayu', 20, 'Female')

name , age, gender = get_student_info()
print(name) #Ayu

# named tuple - allows us to create a tuple with named fields, making it more readable and self-documenting

from collections import namedtuple

student = namedtuple('Student', ['name', 'age', 'gender'])
s1 = student('Ayu', 20, 'Female')
print(s1.name) #Ayu

#tuple type annotation - allows us to specify the expected types of the elements in a tuple, providing better type checking and documentation
from typing import Tuple

def get_student_info() -> Tuple[str, int, str]:
    name = "Ayu"
    age = 20
    gender = "Female"
    return name, age, gender

#fixed-length tuple - allows us to create a tuple with a fixed number of elements, ensuring that the tuple always has the same length   
student: Tuple[str, int, str] = ("Ayu", 20, "Female")

#variable-length tuple - allows us to create a tuple with a variable number of elements, providing flexibility in the number of elements that can be stored in the tuple

numbers: Tuple[int, ...] = (10, 20, 30, 40, 50) #tuple of integers with variable length


#tuple concatenation - allows us to combine two or more tuples into a single tuple
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
print(tuple1 + tuple2) #(10, 20, 30, 40, 50, 60)

#tuple repetition - allows us to create a new tuple by repeating the elements of an existing tuple a specified number of times
tuple1 = (10, 20, 30)
tuple2 = tuple1 * 3
print(tuple2) #(10, 20, 30, 10, 20, 30, 10, 20, 30)

#nested tuple unpacking - allows us to unpack elements from a nested tuple into individual variables
nested_tuple = (10, 20, (30, 40), 50)
a, b, (c, d), e = nested_tuple
print(a) #10
print(b) #20
print(c) #30
print(d) #40


#using zip 
names = ("Ayu", "Budi", "Citra")
ages = (20, 21, 22)

result = list(zip(names, ages))
print(result) #[('Ayu', 20), ('Budi', 21), ('Citra', 22)] - returns a list of tuples, where each tuple contains the corresponding elements from the input tuples

#using tuple as dictionary keys - allows us to use tuples as keys in a dictionary, since tuples are immutable and hashable

location = {
    (43.5, 23.5): "New York",
    (34.5, 45.5): "Los Angeles",
    (12.5, 67.5): "Chicago"
}


#tuple comprehension misconception
numbers = (x for x in range(10)) #this is a generator expression, not a tuple comprehension
print(numbers) #<generator object <genexpr> at 0x7f8c8c8c8c8c>
print(type(numbers)) #<class 'generator'>

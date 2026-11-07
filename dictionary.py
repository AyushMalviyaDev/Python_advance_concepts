#dictionary 

# key-value pairs - allows us to store data in a structured way, where each key is unique and maps to a specific value
# dictionaries are mutable - we can add, remove, and modify key-value pairs
# dictionaries are unordered - the order of key-value pairs is not guaranteed to be preserved
# dictionaries are defined using curly braces {} and key-value pairs are separated by colons :
# duplicate keys are not allowed - if we try to add a key that already exists, the value will be updated
# different data types - keys can be of any immutable data type (e.g., strings, numbers, tuples), while values can be of any data type (e.g., strings, numbers, lists, dictionaries)

# creating a dictionary
dictionary1 = {"name": "Ayu", "age": 25, "city": "New York"}
print(dictionary1) # {'name': 'Ayu', 'age': 25, 'city': 'New York'}
print(dictionary1["name"]) # Ayu

#creating an empty dictionary
empty_dict = {}
print(empty_dict) # {}
print(type(empty_dict)) # <class 'dict'>

#creating a dictionary using dict() constructor
dictionary2 = dict(name="Ayu", age=25, city="New York")
print(dictionary2) # {'name': 'Ayu', 'age': 25, 'city': 'New York'}

# using a list of tuples to create a dictionary
list_of_tuples = [("name", "Ayu"), ("age", 25),
    ("city", "New York")]
dictionary3 = dict(list_of_tuples)
print(dictionary3) # {'name': 'Ayu', 'age': 25, 'city': 'New York'}


#using fromkeys() method to create a dictionary with default values
keys = ["name", "age", "city"]

fromkeys_dict = dict.fromkeys(keys, "unknown") # common value for all keys
print(fromkeys_dict) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

keys["name"] = "Ayu"
print(fromkeys_dict) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'} - changing the value of a key in the original list does not affect the dictionary created using fromkeys() method

#however

keys = ["name", "age", "city"]
data = dict.fromkeys(keys, []) # common value for all keys is a mutable list
data["name"].append("Ayu")
print(data) # {'name': ['Ayu'], 'age': ['Ayu'], 'city': ['Ayu']} - changing the value of a key in the original list affects the dictionary created using fromkeys() method, since the value is a mutable list

#dictionary comprehension - allows us to create a dictionary using a single line of code, by specifying the key-value pairs in a concise way
data = {x: x**2 for x in range(5)}
print(data) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16} - creates a dictionary where the keys are numbers from 0 to 4 and the values are their squares


#accessing dictionary elements using square brackets
print(dictionary1["name"]) # Ayu
#accessing a key that does not exist in the dictionary will raise a KeyError******
#accessing dictionary elements using get() method - 
# 
#acessing a key that does not exist in the dictionary will return None instead of raising a KeyError

print(dictionary1.get("name")) # Ayu
print(dictionary1.get("gender")) # None - key does not exist in the dictionary

#default value for get() 

print(dictionary1.get("gender", "Not specified")) # Not specified 
print(dictionary1.get("weight", "Not available")) # Not available - key does not exist in the dictionary, returns the default value specified

#adding dictionary elements using square brackets
dictionary1["gender"] = "Female"

print(dictionary1) # {'name': 'Ayu', 'age': 25, 'city': 'New York', 'gender': 'Female'}

#updating dictionary elements using square brackets
dictionary1["age"] = 26
print(dictionary1) # {'name': 'Ayu', 'age': 26, 'city': 'New York', 'gender': 'Female'}

# using update() method to add or update dictionary elements
dictionary1.update({"city": "Los Angeles", "country": "USA"})
print(dictionary1) # {'name': 'Ayu', 'age': 26, 'city': 'Los Angeles', 'gender': 'Female', 'country': 'USA'}

# using union operator 

student = {"name": "Ayu", "age": 25, "city": "New York"}
updated_student = student | {"age": 26, "country": "USA"}
print(updated_student) # {'name': 'Ayu', 'age': 26, 'city': 'New York', 'country': 'USA'} - creates a new dictionary with the updated values, does not modify the original dictionary


#removing dictionary elements using del statement
del dictionary1["gender"]
print(dictionary1) # {'name': 'Ayu', 'age': 26, 'city': 'Los Angeles', 'country': 'USA'}


# pop() remove a particular key and return its value

removed_value = dictionary1.pop("city")
print(removed_value) # Los Angeles

#popitem() - removes and returns the last inserted key-value pair as a tuple
last_item = dictionary1.popitem()
print(last_item) # ('country', 'USA') 

# del - deletes a particular key-value pair from the dictionary If the key does not exist, it raises KeyError
del dictionary1["age"]

#clear() - removes all key-value pairs from the dictionary
dictionary1.clear()



#built in dictionary methods

#keys() - returns a view object that displays a list of all the keys in the dictionary
print(dictionary1.keys()) # dict_keys(['name', 'age', 'city', 'gender', 'country'])

#values() - returns a view object that displays a list of all the values in the dictionary
print(dictionary1.values()) # dict_values(['Ayu', 26, 'Los Angeles', 'Female', 'USA'])

#items() - returns a view object that displays a list of all the key-value pairs in the dictionary
print(dictionary1.items()) # dict_items([('name', 'Ayu'), ('age', 26), ('city', 'Los Angeles'), ('gender', 'Female'), ('country', 'USA')])

#get() - returns the value for a specified key if the key is in the dictionary, otherwise returns None (or a default value if specified)
print(dictionary1.get("name")) # Ayu

#update() - updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs
dictionary1.update({"age": 27, "country": "Canada"})

#copy() - returns a shallow copy of the dictionary
dictionary_copy = dictionary1.copy()

#setdefault() - returns the value of a specified key if the key is in the dictionary, otherwise inserts the key with a specified value and returns that value
value = dictionary1.setdefault("gender", "Not specified")


#iterating through a dictionary using a for loop

for key in dictionary1:
    print(key, dictionary1[key]) # prints each key and its corresponding value

for value in dictionary1.values():
    print(value) # prints each value in the dictionary

for key, value in dictionary1.items():
    print(key, value) # prints each key-value pair in the dictionary

#enumarate() - returns an enumerate object that contains the index and value of each key-value pair in the dictionary
for index, (key, value) in enumerate(dictionary1.items()):
    print(index, key, value) 
    # 0 name Ayu
    # 1 age 27
    # 2 city Los Angeles
    # 3 gender Female
    # 4 country Canada

#checking wether a key exists in the dictionary using the in operator
if "name" in dictionary1:
    print("Key 'name' exists in the dictionary") # Key 'name' exists in the dictionary

if "gender" not in dictionary1:
    print("Key 'gender' does not exist in the dictionary") # Key 'gender' does not exist in the dictionary

print("gender" in dictionary1) # True
print("weight" in dictionary1) # False


#nested dictionaries - a dictionary that contains another dictionary as a value

nested_dict = {
    
    "person1": {"name": "Ayu", "age": 25, "city": "New York"},
    "person2": {"name": "John", "age": 30, "city": "Los Angeles"},
    "person3": {"name": "Jane", "age": 28, "city": "Chicago"}
}

print(nested_dict["person1"]["name"]) # Ayu
print(nested_dict["person2"]["age"]) # 30

nested_dict["person3"]["city"] = "San Francisco"

nested_dict["person4"] = {"name": "Mike", "age": 35, "city": "Houston"}


#iterating through a nested dictionary using a for loop

for person, details in nested_dict.items():
    for key, value in details.items():
        print(person, key, value)
        # person1 name Ayu
        # person1 age 25
        # person1 city New York
        # person2 name John
        # person2 age 30
        # person2 city Los Angeles
        # person3 name Jane
        # person3 age 28
        # person3 city San Francisco
        # person4 name Mike
        # person4 age 35
        # person4 city Houston


#dictionary comprehension - allows us to create a dictionary using a single line of code, by specifying the key-value pairs in a concise way
squared_dict = {x: x**2 for x in range(5)}

#dictionary comprehension with condition - allows us to create a dictionary using a single line of code, by specifying the key-value pairs in a concise way, and filtering the elements based on a condition
even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}

print(squared_dict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    
print(even_squared_dict) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#converting values 

prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

updated_prices = {key: value * 1.1 for key, value in prices.items()} # increase all prices by 10%
print(updated_prices) # {'apple': 0.55, 'banana': 0.275, 'orange': 0.825}

#conditional expressions

marks = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}
result  = {key: "Pass" if value >= 70 else "Fail" for key, value in marks.items()}
print(result) # {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Pass', 'David': 'Fail'}


#shallow copy vs deep copy vs assignment

# assignment 

a = { "key1": "value1", "key2": "value2" }
b = a
b["key1"] = "new_value1"
print(a) # {'key1': 'new_value1', 'key2': 'value2'} - changing the value of a key in b also changes the value of the same key in a, since both a and b refer to the same dictionary object


# shallow copy - creates a new dictionary object, but the values are still references to the same objects as in the original dictionary

c = a.copy()
c["key1"] = "another_value1"
print(a) # {'key1': 'new_value1', 'key2': 'value2'} - changing the value of a key in c does not change the value of the same key in a, since c is a new dictionary object


#deep copy 

import copy

a = {
    "name": "Ayush",
    "marks": [80, 90]
}

b = copy.deepcopy(a)

b["marks"].append(100)

print(a)
print(b)

#mergin dictionaries 
#using update 
a = {"name": "Ayush", "age": 21}
b = {"city": "Indore", "age": 22}

a.update(b)

print(a)

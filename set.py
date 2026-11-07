
# 1. CREATING SETS

numbers = {10, 20, 30, 40}
print(numbers)

a = {}
b = set()

print(type(a))  # dict
print(type(b))  # set


# 2. DUPLICATES

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)


# 3. DIFFERENT DATA TYPES

my_set = {10, "hello", 3.14, True}
print(my_set)


# 4. INDEXING (NOT SUPPORTED)

numbers = {10, 20, 30, 40}

# print(numbers[0])  # TypeError


# 5. ITERATION

for num in numbers:
    print(num)


# 6. MEMBERSHIP

print(10 in numbers)
print(50 not in numbers)


# 7. ADD()

numbers.add(50)
print(numbers)


# 8. UPDATE()

numbers.update([60, 70, 80])
print(numbers)


# 9. REMOVE()

numbers.remove(10)
print(numbers)


# 10. DISCARD()

numbers.discard(100)
print(numbers)


# 11. POP()

removed = numbers.pop()
print("Removed:", removed)
print(numbers)


# 12. CLEAR()

numbers.clear()
print(numbers)

# mathematical set methods 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


# 13. UNION

print(A | B)
print(A.union(B))


# 14. INTERSECTION

print(A & B)
print(A.intersection(B))


# 15. DIFFERENCE

print(A - B)
print(A.difference(B))

print(B - A)


# 16. SYMMETRIC DIFFERENCE

print(A ^ B)
print(A.symmetric_difference(B))


A = {1, 2, 3, 4}
B = {1, 2}
C = {5, 6}


# 17. SUBSET

print(B.issubset(A))
print(B <= A)


# 18. SUPERSET

print(A.issuperset(B))
print(A >= B)


# 19. DISJOINT

print(A.isdisjoint(C))


# 20. EQUALITY

X = {1, 2, 3}
Y = {3, 2, 1}

print(X == Y)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


# 21. UPDATE

A.update(B)
print(A)


# 22. INTERSECTION UPDATE

A = {1, 2, 3, 4}
A.intersection_update(B)
print(A)


# 23. DIFFERENCE UPDATE

A = {1, 2, 3, 4}
A.difference_update(B)
print(A)


# 24. SYMMETRIC DIFFERENCE UPDATE

A = {1, 2, 3, 4}
A.symmetric_difference_update(B)
print(A)


# 25. IMMUTABLE SET

numbers = frozenset([1, 2, 3, 4])
print(numbers)

# numbers.add(5)  # AttributeError


# 26. FROZENSET AS DICTIONARY KEY

data = {
    frozenset([1, 2]): "Numbers"
}

print(data[frozenset([1, 2])])


# 27. SQUARES

squares = {x**2 for x in range(1, 6)}
print(squares)


# 28. EVEN NUMBERS

even = {x for x in range(1, 11) if x % 2 == 0}
print(even)


# 29. UNIQUE CHARACTERS

word = "programming"
unique = {ch for ch in word}
print(unique)



# 30. HASHABLE OBJECTS

print(hash(10))
print(hash("hello"))
print(hash((1, 2, 3)))

# print(hash([1, 2]))  # TypeError



numbers = {10, 20, 30, 40}


# 31. LENGTH

print(len(numbers))


# 32. MINIMUM AND MAXIMUM

print(min(numbers))
print(max(numbers))


# 33. SUM

print(sum(numbers))


# 34. COPY

A = {1, 2, 3}
B = A.copy()

print(B)


# 35. ALL AND ANY

A = {True, True, True}
B = {True, False, True}

print(all(A))
print(any(B))

# 36. REMOVE DUPLICATES FROM LIST

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)


# 37. COMMON ELEMENTS BETWEEN TWO LISTS

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

common = set(A) & set(B)
print(common)


# 38. FIND UNIQUE VOWELS

word = "programming interview"

vowels = {ch for ch in word if ch in "aeiou"}
print(vowels)


# 39. FIND MISSING ELEMENTS

registered = {101, 102, 103, 104}
active = {101, 103}

missing = registered - active
print(missing)


# 40. CHECK PERMISSIONS

required = {"read", "write"}
user_permissions = {"read", "write", "delete"}

if required.issubset(user_permissions):
    print("Access Granted")
else:
    print("Access Denied")


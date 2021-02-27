# TUPLES LESSON
# Tuples
# What is a Tuple in Python?
# A Python tuple is a collection type data structure which is immutable bydesign and holds a sequence of heterogeneous elements.
# It functions almost like a Python list but with the following distinctions. Tuples store a fixed set of elements
# and don’t allow changes whereas the list has the provision to update its content. The list uses square brackets
# for opening and closing whereas, and a tuple has got parentheses for the enclosure. A tuple can come quite handy for
# programmers in different situations.

# Python Tuple - Learn with Examples
# Python Tuple Data Structure How to instantiate a Tuple in Python?
# You can create a tuple by placing a sequence of desired elements separated using commas inside a pair of round
# brackets(), i.e., parentheses.
#  Please note that you can create a tuple even without using the parentheses.
#  Also, the elements of a tuple can be of any valid Python data types ranging from numbers, strings, lists, etc.

# Simple examples to create a tuple with different inputs
# create an empty tuple
py_tuple = ()
print("A blank tuple:", py_tuple)
# create a tuple without using round brackets
py_tuple = 33, 55, 77
print("A tuple set without parenthesis:", py_tuple, "type:", type(py_tuple))
# create a tuple of numbers
py_tuple = (33, 55, 77)
print("A tuple of numbers:", py_tuple)
# create a tuple of mixed numbers
# such as integer, float, imaginary
py_tuple = (33, 3.3, 3 + 3j)
print("A tuple of mixed numbers:", py_tuple)
# create a tuple of mixed data types
# such as numbers, strings, lists
py_tuple = (33, "33", [3, 3])
print("A tuple of mixed data types:", py_tuple)
# create a tuple of tuples
# i.e. a nested tuple
py_tuple = (('x', 'y', 'z'), ('X', 'Y', 'Z'))
print("A tuple of tuples:", py_tuple)
# output
# A blank tuple: ()
# A tuple set without parenthesis: (33, 55, 77)
# #### type: < class 'tuple'>
# A tuple of numbers: (33, 55, 77)
# A tuple of mixed numbers: (33, 3.3, (3 + 3j))
# A tuple of mixed data types: (33, '33', [3, 3])
# A tuple of tuples: (('x', 'y', 'z'), ('X', 'Y', 'Z'))

# Using the built - in function “tuple()” to create a tuple
# We can invoke the tuple function and get the desired result.
# creating a tuple from a set
py_tuple = tuple({33, 55, 77})
type(py_tuple)
# <class 'tuple'>
py_tuple
# (33, 77, 55)
# creating a tuple from a list
py_tuple = tuple([33, 55, 77])
type(py_tuple)
# <class 'tuple'>
py_tuple
# (33, 55, 77)
# Creating a tuple of size one
# Create a tuple with a single element.It’s not as easy to achieve as it looks so.
# A single element surrounded by parenthesis will create a string instead of a tuple
py_tuple = ('single')
type(py_tuple)
# <class 'str'>
# You need to place a comma after the first element to create a tuple of size "one"
py_tuple = ('single',)
type(py_tuple)
# <class 'tuple'>
# You can use a list of one element and convert it to a tuple
py_tuple = tuple(['single'])
type(py_tuple)
# <class 'tuple'>
# You can use a set of one element and convert it to a tuple
py_tuple = tuple({'single'})
type(py_tuple)
# <class 'tuple'>

# How can you access a tuple in Python?
# Python provides various intuitive mechanisms to access a single or a range of elements from a tuple.

# Via Indexing
# The simplest is the direct access method where you use the index operator[] to pick an item from the tuple.
# You can start indexing from the 0th position. It means if a tuple holds ten elements, then the index will begin at 0th
# and will end at 9th position. Violating the boundaries of a tuple will result in an IndexError.

# If the tuple contains other tuples as its elements, then you would need to index the elements tuple-by-tuple.
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print("The tuple:", vowel_tuple, "Length:", len(vowel_tuple))
# Indexing the first element
print("OP(vowel_tuple[0]):", vowel_tuple[0])
# Indexing the last element
print("OP(vowel_tuple[length-1]):", vowel_tuple[len(vowel_tuple) - 1])
# Indexing a non-existent member
# will raise the IndexError
try:
    print(vowel_tuple[len(vowel_tuple) + 1])
except Exception as ex:
    print("OP(vowel_tuple[length+1]) Error:", ex)
# Indexing with a non-integer index
# will raise the TypeError
try:
    print(vowel_tuple[0.0])
except Exception as ex:
    print("OP(vowel_tuple[0.0]) Error:", ex)
# Indexing in a tuple of tuples
t_o_t = (('jan', 'feb', 'mar'), ('sun', 'mon', 'wed'))
# Accessing elements from the first sub tuple
print("OP(t_o_t[0][2]):", t_o_t[0][2])
# Accessing elements from the second sub tuple
print("OP(t_o_t[1][2]):", t_o_t[1][2])
# output
# The tuple: ('a', 'e', 'i', 'o', 'u')
# Length: 5
# OP(vowel_tuple[0]): a
# OP(vowel_tuple[length - 1]): u
# OP(vowel_tuple[length + 1])
# Error: tuple index out of range
# OP(vowel_tuple[0.0])
# Error: tuple indices must be integers or slices, not float
# OP(t_o_t[0][2]): mar
# OP(t_o_t[1][2]): wed

# Via Reverse Indexing
# Python tuple supports reverse indexing, i.e., accessing elements using the(-ve) index values.
# The reverse indexing works in the following manner. The index - 1 represents the last item.
# An index with value - 2 will refer to the second item from the rear end.
vowels = ('a', 'e', 'i', 'o', 'u')
vowels
# ('a', 'e', 'i', 'o', 'u')
vowels[-1]
# 'u'
vowels[-2]
# 'o'
vowels[-5]
# 'a'
# vowels[-6]
# Traceback(most recent call last): File "<pyshell#64>", line 1, in < module > vowels[-6]
# IndexError: tuple index out of range

# Via Slicing Operator
# If you need to access not one but more than one element from a tuple, then Python’s slicing operator can come to use.
# The single colon, i.e., a “:” represents the slicing operator in Python.
weekdays = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
weekdays
# ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements leaving the first one
weekdays[1:]
# ('tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements between the first and fifth positions
# excluding the ones at the first and fifth position
weekdays[1:5]
# ('tue', 'wed', 'thu', 'fri')
# accessing elements after the fifth position
weekdays[5:]
# ('sat', 'sun')
# accessing the first five elements
weekdays[:5]
# ('mon', 'tue', 'wed', 'thu', 'fri')
# accessing elements that appears after
# counting five from the rear end
weekdays[:-5]
# ('mon', 'tue')
# accessing five elements from the rear
weekdays[-5:]
# ('wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements from the start to end
weekdays[:]
# ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

# How to modify / update a tuple in Python?
# Since tuples are immutable, so it seems no way to modify them. Once you assign a set of elements to a tuple,
# Python won’t allow it to change. But, there is a catch, what if the items you set are modifiable.
# If there is such a case, then you can change the elements instead of directly modifying the tuple.
# You can even set a tuple to have different values.
py_tuple = (22, 33, 55, 66, [88, 99])
print("Tuple before modificaton:", py_tuple)
# Let's try to modify py_tuple
# It'll return a TypeError
try:
    py_tuple[0] = 11
except Exception as ex:
    print("OP(py_tuple[0]) Error:", ex)
# We can change the values of mutable
# elements inside the py_tuple i.e. list
py_tuple[4][0] = 77
py_tuple[4][1] = 88
print("Tuple after modificaton:", py_tuple)
# We can assign a tuple with new data
py_tuple = ('mon', 'tue', 'wed')
print("Tuple after reassignment:", py_tuple)
# output
# Tuple before modificaton: (22, 33, 55, 66, [88, 99])
# OP(py_tuple[0])
# Error: 'tuple' object does not support item assignment
# Tuple after modificaton: (22, 33, 55, 66, [77, 88])
# Tuple after reassignment: ('mon', 'tue', 'wed')
# You can extend the behavior of a tuple by using the + (concatenation) and *(repeat) operators.

# The plus operator helps you join the two distinct tuples.

first_tuple = ('p', 'y', 't')
second_tuple = ('h', 'o', 'n')
full_tuple = first_tuple + second_tuple
full_tuple
# ('p', 'y', 't', 'h', 'o', 'n')
# The star operator helps you repeat the elements in a tuple for a specified number of times.
init_tuple = ("fork",)
fork_tuple = init_tuple * 5
fork_tuple
# ('fork', 'fork', 'fork', 'fork', 'fork')
# How to remove / delete a tuple in Python?
# Immutability of a tuple would again prevent you from deleting it in a Python program.
# While you can’t delete a tuple directly, but here is something which can help.

# The Python’s del keyword can make you delete a tuple.
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
# you can't delete a particular item from a tuple
try:
    del py_tuple[0]
except Exception as ex:
    print("OP(del py_tuple[0]) Error:", ex)
# but you can delete a whole tuple
del py_tuple
try:
    print(py_tuple)
except Exception as ex:
    print("print(py_tuple) => Error:", ex)
# output
# del py_tuple[0] = > Error: 'tuple'
# object doesn't support item deletion
# print(py_tuple) = > Error: name 'py_tuple' is not defined

# Miscellaneous Tuple Operations
# Testing membership in Python tuple

# Just like we did in Python set, here also, the “ in ” keyword will help us exercise the membership test on a tuple.
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print("First Test: Does 'p' exist?", 'p' in py_tuple)
# First Test: Does 'p' exist? True
print("Second Test: Does 'z' exist?", 'z' in py_tuple)
# Second Test: Does 'z' exist? False
print("Third Test: Does 'n' exist?", 'n' in py_tuple)
# Third Test: Does 'n' exist? True
print("Last Test: Does 't' not exist?", 't' not in py_tuple)
# Last Test: Does 't' not exist? False

# Traversing in a Python tuple
# You can form a for loop and one by one access all the elements in a tuple.
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
for item in py_tuple:
    print("Item:", item)
#
# Item: p
# Item: y
# Item: t
# Item: h
# Item: o
# Item: n

# Usage of Python Tuples
# Used for grouping data
# The tuple provides a quick way of grouping and arranging data.
# It can help you combine any number of elements into a single unit.
# They can help us representing information in the form of records such as the employee record.
# A tuple allows us to group related information and use it as a single entity.
emp_records = ('john', 'hr', 2010, 'robert', 'account', 2015, 'bill', 'mis', 2018)
emp_records[3]
# 'robert'

# Assign to a tuple
# Python tuple supports a very intuitive feature know as “tuple assignment.”
# It lets us assign a tuple of variables on the left of a statement to initialize from the tuple on the right side.
emp_records = ('john', 'hr', 2010, 'robert', 'account', 2015, 'bill', 'mis', 2018)
(emp_name, emp_dept, emp_join_date) = emp_records[0:3]
emp_name
# 'john'
emp_dept
# 'hr'
emp_join_date
# 2010

# Using tuples in functions as return values
# Usually, aFunctiononlyreturnsonevalue.However, we can introduce a tuple and set it as theReturn Value for the Function.
# It means, we can combine multiple values and store them in a tuple and finally return it.
# It could come quite handy in situations when we want to know the hours, minutes, seconds consumed by a job, or to
# get the counts of different types of accessories or the prices of multiple books written by a particular author.
def square(n1, n2):
    return (n1 * n1, n2 * n2)
print(type(square(2, 3)))
# output
# <class 'tuple'>

# Mixed Data Structures in the form of tuples
# Tuples are a type of container which can embed another tuple as an element.
# We call such an object as a nested tuple.
# For example, if we have to maintain employee counts in each department along with their
# names, position, and salaries, the nested tuples can let us do this efficiently.
# employes = [
#     ("HR", 2, [('david', 'manager', 100000), ('bruno', 'asst manager', 50000)])
#     ("IT", 2, [('kirk', 'team lead', 150000), ('matt', 'engineer', 45000)])
#     ("Sales", 2, [('billy', 'sales lead', 250000), ('tom', 'executive', 95000)])
# ]
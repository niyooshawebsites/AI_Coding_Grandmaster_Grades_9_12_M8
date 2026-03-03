# 1) Create different types of tuples:
#    a) Empty tuple, tuple of integers, tuple with mixed data types, and a nested tuple.

# 2) Access tuple elements using indexing:
#    a) Print the first element and last element using indexes like `[0]` and `[last]`.

# 3) Access elements inside a nested tuple:
#    a) Use double indexing to access:
#       - a character from a string inside the tuple
#       - a value from a list inside the tuple

# 4) Slice the tuple:
#    a) Print a portion of the tuple using slicing like `[start:end]`.

# 5) Iterate through the tuple:
#    a) Use a `for` loop to print each element with a message.

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])   
print(my_tuple[5])   

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       
print(n_tuple[1][1])      

# Slicing
print("Sliced :", my_tuple[1:4])

# Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)
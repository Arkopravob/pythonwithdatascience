#tuple
#creating an empty tuple
Tuple1 =()
print(Tuple1)
print(type(Tuple1))

#creating a tuple with strings

str ="arko" , "tani" ,"soura" , "vicky"
Tuple1 = str
print(Tuple1)
print(type(Tuple1))

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple with the
# use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
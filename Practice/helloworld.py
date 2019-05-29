# intro to github and intro
# print always has brackets - print ()
print("Hello World")
print(25)

# variables don't have a dollar sign!
# when naming we use snake_case, to no uppercase letters or symbols other than underscore
first_name = "Harrison"
last_name = "Collett"

# we can print variables or even text and variables
print(first_name)
print("Hello", first_name)
# using format() it's a more elegant way of combining text and variables
print("Hello {} {}".format(first_name, last_name))

# to get user input, we use input() function. Input should be assigned to a variable
city_of_birth = input("Where were you born {}?".format(first_name))
print("Wow! I was also born in {}".format(city_of_birth))

# when we are expecting non-string input. we "cast" our input as a specific data type
year_of_birth = int(input("What year were you born? {}".format(first_name)))
print("Wow! I was also born in {}".format(year_of_birth))

# Python is GREAT for maths!
age = 2019 - year_of_birth
print("So that means you are approximately {} years old".format(age))

# lists are a way storing more than 1 piece of data
my_list = ["bananas", 25, True, "Gold"]
# the index of an item refers to its location in the list. It starts with zero.
# when retrieving data from a list we pull it out of it's index
print(my_list[0])
# lists are mutable, meaning we can edit them after they are set
# to add them to a list, we can either insert() or append()
my_list.append("Table")
print(my_list)
my_list.insert(1, "YEET")
print(my_list)
# to update a list item, just overwrite it
my_list[0] = "DAB"
print(my_list)

# to delete a item from the list we use del
del my_list[4]
print(my_list)

name = input("What is your name again?")
my_list.append(name)
print(my_list)

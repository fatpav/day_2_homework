# def command 'defines' a function
# The colon at the end indicates there will be code inside the function

# def greet():
#      print("Hey there")
# greet()

# The function is 'called' with the function name and brackets 

# the return command is used when you want something from the function.
# instead of printing :"Hey there" it will return it
# def greet():
#     print("Hey there")

# greeting = greet()
# print(greeting)

# The value none indicates an absence of a value

# def greet(name):
#     return "Hey " + name
# greeting = greet("Paul")
# print(greeting)

# I gave the function a parameter and instructed it to give it's return to the variable greetign
# Now I'm going to give the function multiple parameters

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name + "."
# greeting = greet("Paul", "morning")
# print(greeting)

def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name + "."

name_1 = "Paul"
time_of_day_1 = "morning"
greeting = greet(name_1, time_of_day_1)
print(greeting)

name_2 = "Amy"
time_of_day_2 = "afternoon"
greeting = greet(name_2, time_of_day_2)
print(greeting)

# names of variables passed as arguments don't have to match the function's original parameters

# def greet():
#     words = "Hey"
#     return words

# def greet_2():
#     return words

# print(greet_2())

# the function greet_2 has no knowledge of the variable inside greet therefore returns an error

#  I will create a dictionary of chickens
chickens = [
    { "name": "Marge", "age": 2, "eggs": 0 },
    { "name": "Beyonce", "age": 1, "eggs": 3 },
    { "name": "Clucky", "age": 4, "eggs": 7 },
    { "name": "Susan", "age": 2, "eggs": 4 },
]

total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0

print(f"{total_eggs} eggs collected")



'''Description:
Create a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]'''

# MY SOLUTION
def greet(name):
    return f"Hello, {name} how are you doing today?"

#  ALTERNATIVELY
def greet(name):
    return "Hello, {} how are you doing today?".format(name)
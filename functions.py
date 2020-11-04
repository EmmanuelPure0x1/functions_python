# Creating a greeting function

# Syntax: def name_of_function():
# Each function has a block of code to execute to ideally run it's task

# Block of code
def greeting():
    print("Welcome on board")

# In order to execute the program we need to call it.
#Syntax to call the function - calling our greeting function
greeting()

# Adding Arguments
def greeting(name):
    print("Welcome on board", name.capitalize())

# Above we have defined a function that takes an argument (name)
# Calling this will throw an error.
# When calling the function you will have to specify an argument in the function call.
# Example below:

greeting("emmanuel")
# The argument will be passed in function and capitalized.

# Creating a new function

# Function below will take 2 arguments
def add(num1, num2):
#Creating a an addition task to the function with the 2 arguments taken.
    print(num1 + num2)

# calling the function with the arguments (args)
add(4,9)

# calling the functiron with 1 number will throw an error
#add(4)

# calling the function with 3 number will also throw errors
#add(5,9,4)

# Substract function

def subs(num1, num2, num3):
    print(num1 - num2 - num3)

subs(456486498,41564864,4561321586)

# declaring the argument name outside the function wilkl have no effect on the function
num1 = 1

# Create a function to multiply (*)
def multip(num1, num2):
# arguments called in function are multiplied within the print statement
    print(num1*num2)
multip(2,2)

# Create a function to divide (/)
def divide(num1, num2):
# arguments called in function are divided within the print statement
    print(num1/num2)
divide(2,2)

# Create a function to modulo (%)
def modulo(num1, num2):
# remainder of the division of both args printed
    print(num1%num2)
modulo(2,2)

# Create a function to the power squared
def powers(num):
# argument passed is square rooted within print statement
    print(num**2)
powers(12)
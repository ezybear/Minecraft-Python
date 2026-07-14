from minecraft import *
import time

# time.sleep(number)
# Stops the progam for the given number of seconds. 
# It is not used very often in real progams. 

# print('1')
# time.sleep(1)   # Print 1, then wait for 1 second. 
# print('2')
# time.sleep(2)   # Print 2, then wait for 2 seconds. 
# print('3')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('text' or variable or number)
# The print () function prints the 'text', number, or value of
# the variable inside the bracket and then adds a newline. 
# To print multiple items, use a comma (,)
# If you use print() with nothing inside, it prints an empty line

# name = 'Python'
# age = 28
# height = 188
# print(name)
# print()         # prints an empty line
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input('text' or variabe)
# It shows text and waits for user to type something and press Enter. 
# The text or variable can be left out.
# variable = input('text')
# This is the most common way to use input(). 
# If you only use input(), the entered value is not saved. 
# input() always saves the value as a str type. 

# name = input()
# print(name)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Adding strings
# You can join strings using the + operator. 

# first = "cit"
# second = "academy"

# name1 = "cit" + " " + "academy"
# print(name1)

# name2 = "cit" + " " + second
# print(name2)

# name3 = first + " " + second
# print(name3)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# chat()
# chat("text") shows text in Minecraft. 
# You can also use a variable with chat().
# Unlike print(, chat() cannot show many things with commas. 

# chat("Hello! Welcome!")

# message = "Nice to meet you!"
# chat(message)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# say = input()
# chat(say)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# say1 = input()
# chat(say1)

# say2 = input()
# chat(say2)

# say = say1 + say2
# chat(say)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# say = "Hello, welcome!"
# chat(say)

# say = input()
# chat(say)

# say = input("say again in python : ")
# chat(say)

# saycon = input("we concatenate text : ")
# chat(say + " " + saycon)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# say = input("what is your name? : ")    # Input is used for putting in words.
# chat(say)

# text = "your name is " + say 
# print(text)                             # print is for printing words below or in chat.
# chat(text)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Type casting 
# str(variable or value)    -> Changes it to a string.
# float(variable or value)  -> Changes it to a float. 
# int(variable or value)    -> Changes it to a integer. 
# If you use type casting only in a calculation,
# the original variable does naot change.
# To chane the original variable's data type,
# save the changed value back into the variable
# Example: a = int(a)

one = "1"
two = "2"
three = int(one) + int(two)     # The strings in one and two are changed to integers.

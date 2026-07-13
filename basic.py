from minecraft import *


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# variable = value
# Save the value in variable in the format above
# = Unlike the meaning of the symbol, the value is simply stored in a variable.
# Variable can be whatever you want as long as you follow the rules below.
# 1. Impossible to start with a number
# 2. Special characters are not possible except the symbol "_"
# 3. No spacing
# 4. Reserved words not possible

# my_name = "Ezra"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Data types (Type of value)
# Str   -> String   => made up of quotes " "  ' '
# float -> Float    => no quotes and has a decimal point
# int   -> Integer  => no quotes and no decimal point
# Everyday words (English, Chinese, Korean, etc.) without quotes => error

# a = 10  # saves the integer 10 in the variable a
# b = 'cit'   #saves the string 'cit' in the variable b   


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# setpos(x, y, z)
# Use numbers or variables that store numbers for x, y, and z.
# Move to the position you want.

# setpos(700, 100, 700)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 0
# y = 200
# z = 0
# setpos(x, y, z)     # Using variables


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# getpos()
# You can use getpos() to get your current position.
# But if you only use use getpos(), you can get the current position but cannot see it. 
# So use it together with print()

# getpos()        # Gets the current position, but you cannot see it
# print(getpos()) # Gets the current position and prints it


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Move to the position 500, 100, 300 using variables

# x = 500
# y = 100
# z = 300
# setpos(x, y, z)
# print ('location :', getpos())


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# setblock(x, y, z, b)
# Creates one block at the x, y, z position,
# The block ID is b. 
# x, y, z, and b must all be numbers or variables that store numbers. 

# setpos(100, 100, 100)
# setblock(100, 100, 100, 2)  # Creates a block with block ID 2 at position 100, 100, 100


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 100
# y = 100
# z = 100
# b = 2
# setpos(x, y, z)
# setblock(x, y, z, b)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Move to(100, 100, 100), then place a grass block under your feet. 

# x = 100
# y = 100
# z = 100
# b = 2
# setpos(x, y, z)
# setblock(x, y-1, z, b)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 100
# y = 100
# z = 100
# b = 2
# gold = 41
# setpos(x, y, z)
# setblock(x, y-1, z, b)
# setblock(x-1, y-1, z, gold)
# setblock(x-1, y-1, z-1, gold)
# setblock(x-1, y-1, z-2 ,gold)
# setblock(x-1, y-1, z-3, gold)
# setblock(x-1, y-1, z-4, gold)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# setblocks(x1, y1, z1, x2, y2, z2, b)
# Creates many blocks from x1 to x2, y1 to y2, and z1 to z2.
# x1, y1, z1, x2, y2, z2, and b must all be numbers or variables that store numbers. 
# x1, y1, z1    => starting position
# x2, y2, z2    => ending position
# It creates blocks of type b. 
# The starting position is included, and the ending position is also included. 

# setpos(100, 100, 100)
# setblocks(100, 100, 100, 101, 101, 101, 2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 100
# y = 100
# z = 100
# b = 2
# gold = 41
# setpos(x, y, z)
# setblock(x, y-1, z, b)
# setblocks(x-1, y-1, z, x-1, y-1, z-4, gold)     # No need to make many variables if they are the same value, 
#                                                 # allowed to use same coordinates from other builds


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


x = 100
y = 100
z = 100
b = 2
gold = 41
setpos(x, y, z)
setblocks(x-1, y-1, z, x-5, y-1, z-4, gold)
setblocks(x-2, y, z, x-5, y-1, z-4, gold)
setblocks(x-3, y+1, z, x-5, y-1, z-4, gold)
setblocks(x-4, y+2, z, x-5, y-1, z-4, gold )
setblocks(x-5, y+3, z, x-5, y-1, z-4, gold)

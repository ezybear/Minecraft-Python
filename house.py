from minecraft import *

pos = getpos()
x = pos.x
y = pos.y
z = pos.z

# Used blocks
air = 0
grass = 2
plank = (5, 2)
planks = (5, 3)
water = 9
glass = 20
quartz = 155


# Floor/Layout
setblocks(x, y, z, x-9, y, z, quartz)
setblocks(x, y, z, x, y, z-9, quartz)
setblocks(x-9, y, z-9, x-9, y, z, quartz)
setblocks(x-9, y, z-9, x, y, z-9, quartz)
setblocks(x-1, y, z-5, x-8, y, z-8, grass)
setblock(x-6, y, z-6, plank)
setblocks(x, y, z-4, x-9, y, z-4, quartz)

#Pool
setblocks(x-1, y, z-3, x-8, y, z-1, water)

#Outline of house
setblocks(x-6, y+1, z-5, x-2, y+2, z-5, planks)
setblocks(x-2, y+1, z-5, x-2, y+2, z-8, planks)
setblocks(x-2, y+1, z-8, x-6, y+2, z-8, planks)

#First floor
setblocks(x-3, y+2, z-8, x-5, y+2, z-8, glass)
setblocks(x-6, y+1, z-7, x-6, y+2, z-7, planks)

#Outer detail 1
setblocks(x-1, y+1, z-8, x-1, y+3, z-8, quartz)
setblocks(x-7, y+1, z-8, x-7, y+3, z-8, quartz)
setblocks(x-1, y+3, z-8, x-7, y+3, z-4, quartz)

# Second floor
setblocks(x-6, y+3, z-5, x-3, y+3, z-7, air)
setblocks(x-1, y+4, z-4, x-7, y+4, z-4, quartz)
setblocks(x-2, y+4, z-5, x-2, y+4, z-8, glass)
setblocks(x-2, y+4, z-8, x-5, y+4, z-8, glass)
setblocks(x-6, y+3, z-7, x-6, y+3, z-5, planks)
setblock(x-6, y+4, z-8, planks)
setblocks(x-6, y+4, z-5, x-6, y+4, z-7, glass)

# Ceiling/Skylight
setblocks(x-1, y+5, z-4, x-7, y+5, z-8, quartz)
setblocks(x-3, y+5, z-7, x-5, y+5, z-5, glass)

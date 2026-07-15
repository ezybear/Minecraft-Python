from minecraft import *

x = 10
y = 99
z = 140

setblocks(x, y, z, x-9, y, z, 155)
setblocks(x, y, z, x, y, z-9, 155)
setblocks(x-9, y, z-9, x-9, y, z, 155)
setblocks(x-9, y, z-9, x, y, z-9, 155)
setblocks(x-1, y, z-5, x-8, y, z-8, 2)
setblock(x-6, y, z-6, 5,2)
setblocks(x, y, z-4, x-9, y, z-4, 155)
setblocks(x-1, y, z-3, x-8, y, z-1, 9)
setblocks(x-6, y+1, z-5, x-2, y+2, z-5, 5,3)
setblocks(x-2, y+1, z-5, x-2, y+2, z-8, 5,3)
setblocks(x-2, y+1, z-8, x-6, y+2, z-8, 5,3)
setblocks(x-3, y+2, z-8, x-5, y+2, z-8, 20)
setblocks(x-6, y+1, z-7, x-6, y+2, z-7, 5, 3)

setblocks(x-1, y+1, z-8, x-1, y+3, z-8, 155)
setblocks(x-7, y+1, z-8, x-7, y+3, z-8, 155)
setblocks(x-1, y+3, z-8, x-7, y+3, z-4, 155)

setblocks(x-6, y+3, z-5, x-3, y+3, z-7, 0)

from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

ARTILEA = 35
LANDAREA = 103
OSTOA = 18
ENBORRA = 17

def hostoa():
    mc.setBlock (x+1,y+6,z+1,ENBORRA)
    mc.setBlocks(x+1,y+6,z+1,x+2,y+6,z+2,LANDAREA)

#while True:
x,y,z = mc.player.getPos()

for altuera in range(1,3):
        mc.setBlocks(x,y,z+1,x+1,y+7,z+2,LANDAREA)
        hostoa()
        mc.setBlocks(x+1,y+7,z,x+2,y+14,z+1,LANDAREA)
        mc.setBlocks(x+2,y+14,z+1,x+3,y+21,z+2,LANDAREA)
        mc.setBlocks(x+1,y+21,z+2,x+2,y+28,z+3,LANDAREA)
        y=y+25
    

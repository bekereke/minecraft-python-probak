from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

ARTILEA = 35
LANDAREA = 18

#while True:
x,y,z = mc.player.getPos()

for altuera in range(1,3):
        mc.setBlocks(x,y,z+1,x+2,y+7,z+3,LANDAREA)
        mc.setBlocks(x+1,y+7,z,x+3,y+14,z+2,LANDAREA)
        mc.setBlocks(x+2,y+14,z+1,x+4,y+21,z+3,LANDAREA)
        mc.setBlocks(x+1,y+21,z+2,x+3,y+28,z+4,LANDAREA)
        y=y+7
    

from mcpi.minecraft import Minecraft
from random import randint
from time import sleep

ARTILEA = 35
LANDAREA = 103
OSTOA = 18
ENBORRA = 17

def hostoa(behera=0, aldea='eskuin'):
    if aldea=='eskuin':
        mc.setBlock (x+5,y+behera,z+2,ENBORRA)
        mc.setBlock (x+6,y+behera+1,z+2,ENBORRA)
        mc.setBlocks(x+7,y+behera+1,z+1,x+8,y+behera+1,z+3,OSTOA)
        mc.setBlock (x+7,y+behera+2,z+2,OSTOA)
    elif aldea=='ezker':
        mc.setBlocks (x,y+behera,z+2,x+1,y+behera,z+2,ENBORRA)
        mc.setBlock (x-1,y+behera+1,z+2,ENBORRA)
        mc.setBlocks(x-2,y+behera+1,z+1,x-3,y+behera+1,z+3,OSTOA)
        mc.setBlock (x-2,y+behera+2,z+2,OSTOA)
    #elif aldea=='aurre': #hemen
    #elif aldea=='atze': #hemen
    return;

def altuera(posx=1, posz=1):
    mc.setBlocks(x+posx+1,y,z+posz,x+posx+2,y+2,z+posz,LANDAREA)
    sleep(0.1)
    mc.setBlocks(x+posx,y,z+posz+1,x+posx+3,y+2,z+posz+2,LANDAREA)
    sleep(0.1)
    mc.setBlocks(x+posx+1,y,z+posz+3,x+posx+2,y+2,z+posz+3,LANDAREA)
    sleep(0.1)
    return;

#hasi mundua
mc = Minecraft.create()

#jokalariaren posizioa eskuratu    
x,y,z = mc.player.getPos()

#landare igokaria sortu
for altuerak in range(1,10):
    altuera()
    hostoa(behera=randint(0,3),aldea='eskuin')
    y+=3
    altuera(posx=2)
    hostoa(behera=randint(0,3),aldea='ezker')    
    y+=3
    altuera(posx=2, posz=2)
    hostoa(behera=randint(0,3)) #hemen
    y+=3
    altuera(posz=2)
    hostoa(behera=randint(0,3)) #hemen   
    y+=3
    

    

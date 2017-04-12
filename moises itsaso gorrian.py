from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

URA = 9

while True:
    x,y,z = mc.player.getPos()
    behe1 = mc.getBlock(x,y-1,z)
    #avatarrak bi bloke luze (altuera) ditu
    goi = mc.getBlock(x,y+2,z)
    beheaurre11 = mc.getBlock(x+1,y-1,z)
    beheatze11 = mc.getBlock(x-1,y-1,z)
    beheezker11 = mc.getBlock(x,y-1,z-1)
    beheeskuin11 = mc.getBlock(x,y-1,z+1)
    behediagonala11 = mc.getBlock(x-1,y-1,z+1)
    behediagonalb11 = mc.getBlock(x+1,y-1,z+1)
    behediagonalc11 = mc.getBlock(x-1,y-1,z-1)
    behediagonald11 = mc.getBlock(x+1,y-1,z-1)
    #airearekin ordezkatu baldin eta ura badu inguruan


    if behe1 == URA:
        mc.setBlocks(x,y-1,z,x,y+5,z,0)

    if beheaurre11 == URA:
        mc.setBlocks(x+1,y-1,z,x+1,y+5,z,0)

    if beheatze11 == URA:
        mc.setBlocks(x-1,y-1,z,x-1,y+5,z,0)

    if beheezker11 == URA:
        mc.setBlocks(x,y-1,z-1,x,y+5,z-1,0)        

    if beheeskuin11 == URA:
        mc.setBlocks(x,y-1,z+1,x,y+5,z+1,0)

    if behediagonala11 == URA:
        mc.setBlocks(x-1,y-1,z+1,x-1,y+5,z+1,0)


    sleep(0.5)
    

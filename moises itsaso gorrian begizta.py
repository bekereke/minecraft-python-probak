from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

URA = 9
URERAUNTSIA = 8

erantzuna = input("Moises eta Ramsesen istorioa ezagutu nahi al duzu? B/e")
if erantzuna == "B" or erantzuna == "b":
    mc.postToChat("Hurbildu zaitez ur ertzera...")
    sleep(5)
    x,y,z = mc.player.getPos()
    aurrean = mc.getBlock(x,y,z+1)
    behean = mc.getBlock(x,y-1,z+1)
    beherago = mc.getBlock(x,y-2,z+1)
    if aurrean == URA or behean == URA or beherago == URA:
        print("Zabaldu bedi Itsaso Gorria nire herriak gurutzatu dezan!")
        mc.postToChat("Zabaldu bedi Itsaso Gorria nire herriak gurutzatu dezan!")

        #z.hamartarretik z.osora pasa beharko ditugu begiztan erabiltzeko
        xi = int(round(x))
        yi = int(round(y))
        zi = int(round(z))
        #for a in range(xi-2,xi+2):
        #    for b in range(yi-5,yi):
        #        for c in range(zi-20,zi+20):
        for b in range(yi-30,yi):
            for c in range(zi,zi+60):
                for a in range(xi-3,xi+3):
                    blokea = mc.getBlock(a,b,c)
                    if blokea == URA or blokea == URERAUNTSIA:
                        mc.setBlocks(a,b,c,a,yi+50,c,0)
        print("Ramses iritsi orduko, ORAIN, gurutzatu semeok Itsaso Gorria!")
        mc.postToChat("Ramses iritsi orduko, ORAIN, gurutzatu semeok Itsaso Gorria!")

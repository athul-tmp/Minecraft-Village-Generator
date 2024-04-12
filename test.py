#for spawning 5 houses for test purposes

from mcpi.minecraft import Minecraft
from House import House
import random
mc = Minecraft.create()
x, y, z = mc.player.getPos()

for value in range(5):
    length = random.randrange(20,28, 2) #x-axis
    width = random.randrange(16,32, 2) #z-axis
    height = random.randrange(6,11, 2) #y-axis
    newHouse_A = House(x,y,z)
    newHouse_A.build_house(length,height,width)
    x += 40
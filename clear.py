#FOR TESTING PURPOSES
from mcpi.minecraft import Minecraft
from House import House
import random
mc = Minecraft.create()

mc.postToChat("Cleared")
x, y, z = mc.player.getPos()
mc.setBlocks(x-200,y,z-200,x+200,y+30,z+200,0)
mc.setBlocks(x-200,y,z-200,x+200,y,z+200,2)

from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

#to be called in backyard class
class Terraform:
    def __init__(self,x1,y1,z1,x2,z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.z2 = z2

    def terraform_land(self):
        mc.setBlocks(self.x1,self.y1,self.z1,self.x2,self.y1+40,self.z2,0)#empty the land
        mc.setBlocks(self.x1,self.y1-1,self.z1,self.x2,self.y1-1,self.z2,2)#grass below house
        #add grass below in a pyramidal way
        for i in range(20):
            mc.setBlocks(self.x1-1-i,self.y1-2-i,self.z1-1-i,self.x2+1+i,self.y1-2-i,self.z2+1+i,2)
        
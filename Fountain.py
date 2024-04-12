from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

class Fountain:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def small_fountain(self):
        mc.setBlocks(self.x-1,self.y-1,self.z-1,self.x+5,self.y+4,self.z+5,0)#clearing area above path
        mc.setBlocks(self.x-1,self.y-1,self.z-1,self.x+5,self.y-1,self.z+5,4)#path around fountain 
        mc.setBlocks(self.x-1,self.y-2,self.z-1,self.x+5,self.y-10,self.z+5,3)#dirt below path
        mc.setBlocks(self.x+1,self.y,self.z, self.x+3 , self.y-1, self.z,98)#x axis
        mc.setBlocks(self.x+4,self.y,self.z+1, self.x+4 , self.y-1, self.z+3,98)#z axis
        mc.setBlocks(self.x+3,self.y,self.z+4,self.x+1,self.y-1,self.z+4,98)#-x axis
        mc.setBlocks(self.x,self.y,self.z+3,self.x,self.y-1,self.z+1,98)#-z axis
        mc.setBlocks(self.x+1,self.y-1,self.z+1,self.x+3,self.y-1,self.z+3,98)
        mc.setBlocks(self.x+2,self.y,self.z+2,self.x+2,self.y+2,self.z+2,98)#pillar
        mc.setBlock(self.x+2,self.y+3,self.z+2,8) #water
    
    def medium_fountain(self):
        mc.setBlocks(self.x-2,self.y-1,self.z,self.x+6,self.y+5,self.z+8,0)#clearing area above path
        mc.setBlocks(self.x-2,self.y-1,self.z,self.x+6,self.y-1,self.z+8,4)#path around fountain 
        mc.setBlocks(self.x-2,self.y-2,self.z,self.x+6,self.y-10,self.z+8,3)#dirt below path
        #x axis
        mc.setBlock(self.x,self.y,self.z+2,98)#single block
        mc.setBlocks(self.x+1,self.y,self.z+1,self.x+3,self.y,self.z+1,98)
        mc.setBlock(self.x+4,self.y,self.z+2,98)#single block
        
        #z axis
        mc.setBlocks(self.x+5,self.y,self.z+3,self.x+5,self.y,self.z+5,98)
        mc.setBlock(self.x+4,self.y,self.z+6,98)#single block

        #x axis
        mc.setBlocks(self.x+1,self.y,self.z+7,self.x+3,self.y,self.z+7,98)
        mc.setBlock(self.x,self.y,self.z+6,98)#single block

        #z axis
        mc.setBlocks(self.x-1,self.y,self.z+3,self.x-1,self.y,self.z+5,98)

        #floor
        mc.setBlocks(self.x,self.y-1,self.z+2,self.x+4,self.y-1,self.z+6,98)

        #pillar
        mc.setBlocks(self.x+2,self.y,self.z+4,self.x+2,self.y+3,self.z+4,98)

        mc.setBlocks(self.x+2,self.y,self.z+3,self.x+2,self.y+1,self.z+3,98)
        mc.setBlocks(self.x+3,self.y,self.z+4,self.x+3,self.y+1,self.z+4,98)
        mc.setBlocks(self.x+2,self.y,self.z+5,self.x+2,self.y+1,self.z+5,98)
        mc.setBlocks(self.x+1,self.y,self.z+4,self.x+1,self.y+1,self.z+4,98)
        
        #water
        mc.setBlock(self.x+2,self.y+4,self.z+4,8)


    def big_fountain(self):
        mc.setBlocks(self.x-4,self.y-1,self.z-1,self.x+7,self.y+6,self.z+10,0)#clearing area above path
        mc.setBlocks(self.x-4,self.y-1,self.z-1,self.x+7,self.y-1,self.z+10,4)#path around fountain 
        mc.setBlocks(self.x-4,self.y-2,self.z-1,self.x+7,self.y-10,self.z+10,3)#dirt below path
        mc.setBlocks(self.x-1,self.y,self.z+1,self.x,self.y,self.z+1,98)#x axis
        mc.setBlocks(self.x+1,self.y,self.z,self.x+2,self.y,self.z,98)#x axis
        mc.setBlocks(self.x+3,self.y,self.z+1,self.x+4,self.y,self.z+1,98)#x axis

        mc.setBlocks(self.x+5,self.y,self.z+2,self.x+5,self.y,self.z+3,98)#z axis
        mc.setBlocks(self.x+6,self.y,self.z+4,self.x+6,self.y,self.z+5,98)#z axis
        mc.setBlocks(self.x+5,self.y,self.z+6,self.x+5,self.y,self.z+7,98)#z axis
        
        mc.setBlocks(self.x-1,self.y,self.z+8,self.x,self.y,self.z+8,98)#x axis
        mc.setBlocks(self.x+1,self.y,self.z+9,self.x+2,self.y,self.z+9,98)#x axis
        mc.setBlocks(self.x+3,self.y,self.z+8,self.x+4,self.y,self.z+8,98)#xaxis

        mc.setBlocks(self.x-2,self.y,self.z+2,self.x-2,self.y,self.z+3,98)#z axis
        mc.setBlocks(self.x-3,self.y,self.z+4,self.x-3,self.y,self.z+5,98)#z axis
        mc.setBlocks(self.x-2,self.y,self.z+6,self.x-2,self.y,self.z+7,98)#z axis

        #floor
        mc.setBlocks(self.x-1,self.y-1,self.z+1,self.x+4,self.y-1,self.z+8,98)
        mc.setBlocks(self.x-2,self.y-1,self.z+2,self.x+5,self.y-1,self.z+7,98)

        #pillar
        mc.setBlocks(self.x+1,self.y,self.z+4,self.x+2,self.y+4,self.z+5,98)
        mc.setBlocks(self.x+1,self.y,self.z+3,self.x+2,self.y+1,self.z+3,98)#x axis
        mc.setBlocks(self.x+3,self.y,self.z+4,self.x+3,self.y+1,self.z+5,98)#z axis
        mc.setBlocks(self.x+2,self.y,self.z+6,self.x+1,self.y+1,self.z+6,98)#x axis
        mc.setBlocks(self.x,self.y,self.z+4,self.x,self.y+1,self.z+5,98)#z axis

        #water
        mc.setBlocks(self.x+1,self.y+5,self.z+4,self.x+2,self.y+5,self.z+5,8)

    def random_fountain(self):
        ch = random.randint(0,2)
        if ch == 0:
            self.small_fountain()
        if ch == 1:
            self.medium_fountain()
        if ch == 2:
            self.big_fountain()

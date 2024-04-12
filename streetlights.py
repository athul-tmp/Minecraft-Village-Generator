from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Streetlights():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y+1
        self.z = z

    def build_streetlight(self):
        mc.setBlocks(self.x,self.y,self.z,self.x,self.y+3,self.z,85)#pole
        mc.setBlock(self.x,self.y+4,self.z,126)#slab ontop
        mc.setBlock(self.x+1,self.y+4,self.z,126)#slab ontop
        mc.setBlock(self.x-1,self.y+4,self.z,126)#slab ontop
        mc.setBlock(self.x,self.y+4,self.z+1,126)#slab ontop
        mc.setBlock(self.x,self.y+4,self.z-1,126)#slab ontop

        mc.doCommand(f'setblock {int(self.x)-1} {int(self.y)+3} {int(self.z)} minecraft:lantern[hanging=true]')#lantern
        mc.doCommand(f'setblock {int(self.x)+1} {int(self.y)+3} {int(self.z)} minecraft:lantern[hanging=true]')#lantern
        mc.doCommand(f'setblock {int(self.x)} {int(self.y)+3} {int(self.z)+1} minecraft:lantern[hanging=true]')#lantern
        mc.doCommand(f'setblock {int(self.x)} {int(self.y)+3} {int(self.z)-1} minecraft:lantern[hanging=true]')#lantern

    

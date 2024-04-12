#NOT IMPLEMENTED
from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

class Trees:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.random_tree_type = [0, 1, 2, 3]

    def random_tree(self):
        random_tree_choice = random.choice(self.random_tree_type)
        self.random_tree_height = random.randint(3,8)
        mc.setBlocks(self.x+1,0,self.z, self.x+1 , self.y+self.random_tree_height, self.z,17, random_tree_choice)#trunk of tree
        mc.setBlocks(self.x+3,0+self.random_tree_height,self.z+2, self.x-1 , self.y+self.random_tree_height+1, self.z-2,18,random_tree_choice)#bottom leaf of tree
        mc.setBlocks(self.x+2,0+self.random_tree_height,self.z+1, self.x , self.y+self.random_tree_height+3, self.z-1,18, random_tree_choice)#top leaf of tree
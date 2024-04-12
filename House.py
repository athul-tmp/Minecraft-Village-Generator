
from mcpi.minecraft import Minecraft
from mcpi import block
import random
from Backyard import Backyard
from Roof import Roof
mc = Minecraft.create()

class House:
    def __init__(self,x, y,z,dir=''):
        self.x = x
        self.y = y
        self.z = z
        self.dir = dir
        

    def stairs(self,split):
        #check for remainder stairs for turning 
        remainder_stairs = split - 3
        # remove ground for second floor for stairs
        mc.setBlocks(self.x+1, self.y+split, self.z+3, self.x+1, self.y+split, self.z+1,0)
        mc.setBlocks(self.x+1, self.y+split, self.z+1, self.x+remainder_stairs+1, self.y+split, self.z+1,0)
        mc.setBlocks(self.x+1, self.y+split-1, self.z+3, self.x+1, self.y+split, self.z+1,0)
        mc.setBlocks(self.x+1, self.y+split-1, self.z+1, self.x+remainder_stairs+1, self.y+split, self.z+1,0)
        #set stairs north facing 
        for move in range(1,3):
            mc.setBlocks(self.x+1, self.y+move, self.z+4-move,  self.x+1, self.y+move, self.z+4-move,53,3) #face north

        #set block for turning and support
        mc.setBlocks(self.x+1, self.y+1, self.z+2,  self.x+1, self.y+1, self.z+2,5)
        mc.setBlocks(self.x+1, self.y+1, self.z+1,  self.x+1, self.y+2, self.z+1,5)
        mc.setBlocks(self.x+2, self.y+1, self.z+1,  self.x+2, self.y+2, self.z+1,5)
        
        #set stairs facing east 
        remainder_stairs = split - 3
        for move in range(0,remainder_stairs+1):
            mc.setBlocks(self.x+2+move, self.y+move+3, self.z+1,  self.x+2+move, self.y+move+3, self.z+1,53,0) #face east
        mc.setBlocks(self.x+2+move, self.y+move+3+1, self.z+1,  self.x+2+move, self.y+move+3+1, self.z+1,0)
        #fence for second floor 
        
    def windows(self,length,width,split = 0, floor = 1):
        #set windows 1st floor 
        #front windows
        if floor  == 1:
            mc.setBlocks(self.x+(length/2)-4, self.y+2, self.z, self.x+(length/2)-2, self.y+3, self.z+0, 20)
            mc.setBlocks(self.x+(length/2)+4, self.y+2, self.z, self.x+(length/2)+2, self.y+3, self.z+0, 20)

            #right-side windows
            mc.setBlocks(self.x, self.y+2, self.z+(width/2)-4, self.x+0, self.y+3, self.z+(width/2)-2, 20)
            mc.setBlocks(self.x, self.y+2, self.z+(width/2)+4, self.x+0, self.y+3, self.z+(width/2)+2, 20)
            #left-side windows
            mc.setBlocks(self.x+length, self.y+2, self.z+(width/2)-4, self.x+length, self.y+3, self.z+(width/2)-2, 20)
            mc.setBlocks(self.x+length, self.y+2, self.z+(width/2)+4, self.x+length, self.y+3, self.z+(width/2)+2, 20)

            #backside windows
            mc.setBlocks(self.x+(length/2)-4, self.y+2, self.z+width, self.x+(length/2)-2, self.y+3, self.z+width, 20)
            mc.setBlocks(self.x+(length/2)+4, self.y+2, self.z+width, self.x+(length/2)+2, self.y+3, self.z+width, 20)
        
        #set windows 2nd floor 
        else:
        #front windows
            mc.setBlocks(self.x+(length/2)-4, self.y+1+split, self.z, self.x+(length/2)-2, self.y+split+2, self.z+0, 20)
            mc.setBlocks(self.x+(length/2)+4, self.y+1+split, self.z, self.x+(length/2)+2, self.y+split+2, self.z+0, 20)

            #right-side windows
            mc.setBlocks(self.x, self.y+1+split, self.z+(width/2)-4, self.x+0, self.y+split+2, self.z+(width/2)-2, 20)
            mc.setBlocks(self.x, self.y+1+split, self.z+(width/2)+4, self.x+0, self.y+split+2, self.z+(width/2)+2, 20)
            #left-side windows
            mc.setBlocks(self.x+length, self.y+1+split, self.z+(width/2)-4, self.x+length, self.y+split+2, self.z+(width/2)-2, 20)
            mc.setBlocks(self.x+length, self.y+1+split, self.z+(width/2)+4, self.x+length, self.y+split+2, self.z+(width/2)+2, 20)

            #backside windows
            mc.setBlocks(self.x+(length/2)-4, self.y+1+split, self.z+width, self.x+(length/2)-2, self.y+split+2, self.z+width, 20)
            mc.setBlocks(self.x+(length/2)+4, self.y+1+split, self.z+width, self.x+(length/2)+2, self.y+split+2, self.z+width, 20)

    def door_step(self,length,width,dir = ''):
        #include step for door
            door_step = random.choice([53, 134, 135, 136, 163, 164])
            #oak wood
            if door_step == 53:
                door_fence = 85
                door_step_block = 0
            #spruce wood
            elif door_step == 134:
                door_fence = 188
                door_step_block = 1
            #birch wood
            elif door_step == 135:
                door_fence = 189
                door_step_block = 2
            #jungle wood
            elif door_step == 136:
                door_fence = 190
                door_step_block = 3
            #acacia wood
            elif door_step == 163:
                door_fence = 192
                door_step_block = 4
            #dark oak wood
            elif door_step == 164:
                door_fence = 191
                door_step_block = 5
            # steps orientation    
            #3 south    
            #2 north
            #1 west
            #0 east
            if dir == 'S':
                mc.setBlocks(self.x+(length/2), self.y, self.z-1, self.x+(length/2), self.y, self.z-1,door_step,2)
                mc.setBlocks(self.x+(length/2), self.y-1, self.z-1, self.x+(length/2), self.y-1, self.z-1-5,208)
                for i in range(1,20):
                    mc.setBlock(self.x+(length/2), self.y-1-i, self.z-1-5-i,208)
                mc.setBlocks(self.x+(length/2), self.y+3, self.z-1, self.x+(length/2), self.y+3, self.z-1,5,door_step_block)         
                mc.setBlocks(self.x+(length/2)+1, self.y, self.z-1, self.x+(length/2)+1, self.y, self.z-1,5,door_step_block)
                mc.setBlocks(self.x+(length/2)+1, self.y+1, self.z-1, self.x+(length/2)+1, self.y+2, self.z-1,door_fence)
                mc.setBlocks(self.x+(length/2)+1, self.y+3, self.z-1, self.x+(length/2)+1, self.y+3, self.z-1,door_step,1)
                mc.setBlocks(self.x+(length/2)-1, self.y, self.z-1, self.x+(length/2)-1, self.y, self.z-1,5,door_step_block)
                mc.setBlocks(self.x+(length/2)-1, self.y+1, self.z-1, self.x+(length/2)-1, self.y+2, self.z-1,door_fence)
                mc.setBlocks(self.x+(length/2)-1, self.y+3, self.z-1, self.x+(length/2)-1, self.y+3, self.z-1,door_step,0)
                
            elif dir == 'N':
                mc.setBlocks(self.x+(length/2), self.y, self.z+width+1, self.x+(length/2), self.y, self.z+width+1,door_step,3)
                mc.setBlocks(self.x+(length/2), self.y-1, self.z+width+1, self.x+(length/2), self.y-1, self.z+width+1+7,208)
                for i in range(1,20):
                    mc.setBlock(self.x+(length/2), self.y-1-i, self.z+width+1+7+i,208)
                mc.setBlocks(self.x+(length/2), self.y+3, self.z+width+1, self.x+(length/2), self.y+3, self.z+width+1,5,door_step_block)         
                mc.setBlocks(self.x+(length/2)+1, self.y, self.z+width+1, self.x+(length/2)+1, self.y, self.z+width+1,5,door_step_block)
                mc.setBlocks(self.x+(length/2)+1, self.y+1, self.z+width+1, self.x+(length/2)+1, self.y+2, self.z+width+1,door_fence)
                mc.setBlocks(self.x+(length/2)+1, self.y+3, self.z+width+1, self.x+(length/2)+1, self.y+3, self.z+width+1,door_step,1)
                mc.setBlocks(self.x+(length/2)-1, self.y, self.z+width+1, self.x+(length/2)-1, self.y, self.z+width+1,5,door_step_block)
                mc.setBlocks(self.x+(length/2)-1, self.y+1, self.z+width+1, self.x+(length/2)-1, self.y+2, self.z+width+1,door_fence)
                mc.setBlocks(self.x+(length/2)-1, self.y+3, self.z+width+1, self.x+(length/2)-1, self.y+3, self.z+width+1,door_step,0)
                
            elif dir == 'E':
                mc.setBlocks(self.x-1, self.y, self.z+(width/2), self.x-1, self.y, self.z+(width/2),door_step,0)
                mc.setBlocks(self.x-1, self.y-1, self.z+(width/2), self.x-1-4, self.y-1, self.z+(width/2),208)
                for i in range(1,20):
                    mc.setBlock(self.x-1-4-i, self.y-1-i, self.z+(width/2),208)
                mc.setBlocks(self.x-2, self.y, self.z+(width/2), self.x-2, self.y, self.z+(width/2),0)
                mc.setBlocks(self.x-1, self.y+3, self.z+(width/2), self.x-1, self.y+3, self.z+(width/2),5,door_step_block)         
                mc.setBlocks(self.x-1, self.y, self.z+(width/2)+1, self.x-1, self.y, self.z+(width/2)+1,5,door_step_block)
                mc.setBlocks(self.x-1, self.y+1, self.z+(width/2)+1, self.x-1, self.y+2, self.z+(width/2)+1,door_fence)
                mc.setBlocks(self.x-1, self.y+3, self.z+(width/2)+1, self.x-1, self.y+3, self.z+(width/2)+1,door_step,3)
                mc.setBlocks(self.x-2, self.y, self.z+(width/2)+1, self.x-2, self.y, self.z+(width/2)+1,0)
                mc.setBlocks(self.x-1, self.y, self.z+(width/2)-1, self.x-1, self.y, self.z+(width/2)-1,5,door_step_block)
                mc.setBlocks(self.x-1, self.y+1, self.z+(width/2)-1, self.x-1, self.y+2, self.z+(width/2)-1,door_fence)
                mc.setBlocks(self.x-1, self.y+3, self.z+(width/2)-1, self.x-1, self.y+3, self.z+(width/2)-1,door_step,2)
                mc.setBlocks(self.x-2, self.y, self.z+(width/2)-1, self.x-2, self.y, self.z+(width/2)-1,0)
                
            elif dir == 'W':
                mc.setBlocks(self.x+length+1, self.y, self.z+(width/2), self.x+length+1, self.y, self.z+(width/2),door_step,1)
                mc.setBlocks(self.x+length+2, self.y, self.z+(width/2), self.x+length+2, self.y, self.z+(width/2),0)
                mc.setBlocks(self.x+length+1, self.y-1, self.z+(width/2), self.x+length+1+7, self.y-1, self.z+(width/2),208)
                for i in range(1,20):
                    mc.setBlock(self.x+length+1+7+i, self.y-1-i, self.z+(width/2),208)

                mc.setBlocks(self.x+length+1, self.y+3, self.z+(width/2), self.x+length+1, self.y+3, self.z+(width/2),5,door_step_block)         
                mc.setBlocks(self.x+length+1, self.y, self.z+(width/2)+1, self.x+length+1, self.y, self.z+(width/2)+1,5,door_step_block)
                mc.setBlocks(self.x+length+1, self.y+1, self.z+(width/2)+1, self.x+length+1, self.y+2, self.z+(width/2)+1,door_fence)
                mc.setBlocks(self.x+length+1, self.y+3, self.z+(width/2)+1, self.x+length+1, self.y+3, self.z+(width/2)+1,door_step,3)
                mc.setBlocks(self.x+length+2, self.y, self.z+(width/2)+2, self.x+length+2, self.y, self.z+(width/2)+1,0)

                mc.setBlocks(self.x+length+1, self.y, self.z+(width/2)-1, self.x+length+1, self.y, self.z+(width/2)-1,5,door_step_block)
                mc.setBlocks(self.x+length+1, self.y+1, self.z+(width/2)-1, self.x+length+1, self.y+2, self.z+(width/2)-1,door_fence)
                mc.setBlocks(self.x+length+1, self.y+3, self.z+(width/2)-1, self.x+length+1, self.y+3, self.z+(width/2)-1,door_step,2)
                mc.setBlocks(self.x+length+2, self.y, self.z+(width/2)-1, self.x+length+2, self.y, self.z+(width/2)-1,0)



    #function for lights
    def lights(self, length, height, width,split = None):
        light = 169
        mc.setBlocks(self.x+1, self.y+height, self.z+1, self.x+length-1, self.y+height, self.z+1, light)#x axis lights
        mc.setBlocks(self.x+length-1, self.y+height, self.z+1, self.x+length-1, self.y+height, self.z+width-1, light)#z axis lights
        mc.setBlocks(self.x+length-1, self.y+height, self.z+width-1, self.x+1, self.y+height, self.z+width-1, light)#-x axis lights
        mc.setBlocks(self.x+1, self.y+height, self.z+width-1, self.x+1, self.y+height, self.z+1, light)#-z axis lights
        mc.setBlocks(self.x+(length/2), self.y+height, self.z+1, self.x+(length/2), self.y+height, self.z+width-1, light)#lights doorway line

        if height >=8:
            global carpet 
            carpet = random.choice([0,7,8,12,15])
            mc.setBlocks(self.x+1, self.y+split, self.z+1, self.x+length-1, self.y+split, self.z+1, light)
            mc.setBlocks(self.x+length-1, self.y+split, self.z+1, self.x+length-1, self.y+split, self.z+width-1, light)
            mc.setBlocks(self.x+length-1, self.y+split, self.z+width-1, self.x+1, self.y+split, self.z+width-1, light)
            mc.setBlocks(self.x+1, self.y+split, self.z+width-1, self.x+1, self.y+split, self.z+1, light)
            mc.setBlocks(self.x+(length/2), self.y+split, self.z+1, self.x+(length/2), self.y+split, self.z+width-1, light)
            mc.setBlocks(self.x+1, self.y+split+1, self.z+1, self.x+length-1, self.y+split+1, self.z+width-1, 171, carpet)


    def build_house(self,length,height,width):
        house_block_id = [1, 4, 5, 45]
        block_id = random.choice(house_block_id)
        block_data = 0
        if block_id == 1:
            block_data = random.choice([0,1,2,3,4,5,6])
        if block_id == 5:
            block_data = random.choice([0,1,2,3,4,5])
        corner_id = 17
        corner_data = random.choice([0,1,2,3])
        doors_id = [64,193,194,195,196,197]
        door_id = random.choice(doors_id)

        split = 0
        floor = 1
        
        if self.dir == 'W':
            if height >= 8:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height,width, rand_backyard_choice,'W')
                split = height//2
                door = width/2
                floor = 2
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #splits into 2 floor
                mc.setBlocks(self.x, self.y+split, self.z, self.x+length, self.y+split, self.z+width, block_id, block_data)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id, corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id, corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                
                #include door
                mc.setBlocks(self.x+length, self.y+2, self.z+(width/2), self.x+length, self.y+2, self.z+(width/2), door_id,8)
                mc.setBlocks(self.x+length, self.y+1, self.z+(width/2), self.x+length, self.y+1, self.z+(width/2), door_id,1)
                
                self.door_step(length,width,'W')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                #stairs
                self.stairs(split)
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'W')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)                
            else:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height,width, rand_backyard_choice,'W')
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id,corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x+length, self.y+2, self.z+(width/2), self.x+length, self.y+2, self.z+(width/2), door_id,8)
                mc.setBlocks(self.x+length, self.y+1, self.z+(width/2), self.x+length, self.y+1, self.z+(width/2), door_id,1)
                
                self.door_step(length,width,'W')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
            
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'W')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)

            self.recursive_split(length, width, height,block_id,block_data)
                
        elif self.dir == 'E':
            if height >= 8:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height,width, rand_backyard_choice,'E')
                split = height//2
                door = width/2
                floor = 2
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #splits into 2 floor
                mc.setBlocks(self.x, self.y+split, self.z, self.x+length, self.y+split, self.z+width, block_id, block_data)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id, corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id, corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x, self.y+2, self.z+(width/2), self.x, self.y+2, self.z+(width/2), door_id,9)
                mc.setBlocks(self.x, self.y+1, self.z+(width/2), self.x, self.y+1, self.z+(width/2), door_id,1)
                
                self.door_step(length,width,'E')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                #stairs
                self.stairs(split)
           
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'E')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)
                
            else:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height,width, rand_backyard_choice,'E')
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id,corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x, self.y+2, self.z+(width/2), self.x, self.y+2, self.z+(width/2), door_id,9)
                mc.setBlocks(self.x, self.y+1, self.z+(width/2), self.x, self.y+1, self.z+(width/2), door_id,1)
                
                self.door_step(length,width,'E')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'E')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)

            self.recursive_split(length, width, height,block_id,block_data)
                
        elif self.dir == 'N':
            if height >= 8:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height,width, rand_backyard_choice,'N')
                split = height//2
                door = width/2
                floor = 2
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #splits into 2 floor
                mc.setBlocks(self.x, self.y+split, self.z, self.x+length, self.y+split, self.z+width, block_id, block_data)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id, corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id, corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x+(length/2), self.y+2, self.z+width, self.x+(length/2), self.y+2, self.z+width, door_id,9)
                mc.setBlocks(self.x+(length/2), self.y+1, self.z+width, self.x+(length/2), self.y+1, self.z+width, door_id,1)  
        
                self.door_step(length,width,'N')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                #stairs
                self.stairs(split)
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'N')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)
            else:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height, width, rand_backyard_choice,'N')
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id,corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x+(length/2), self.y+2, self.z+width, self.x+(length/2), self.y+2, self.z+width, door_id,9)
                mc.setBlocks(self.x+(length/2), self.y+1, self.z+width, self.x+(length/2), self.y+1, self.z+width, door_id,1)    
                
                self.door_step(length,width,'N')
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'N')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)

            self.recursive_split(length, width, height,block_id,block_data)
                    
        #blocks for house material
        else:
            # 2 stories house
            if height >= 8:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height, width, rand_backyard_choice, 'S')
                split = height//2
                door = width/2
                floor = 2
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #splits into 2 floor
                mc.setBlocks(self.x, self.y+split, self.z, self.x+length, self.y+split, self.z+width, block_id, block_data)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id, corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id, corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x+(length/2), self.y+2, self.z, self.x+(length/2), self.y+2, self.z+0, door_id,9)
                mc.setBlocks(self.x+(length/2), self.y+1, self.z, self.x+(length/2), self.y+1, self.z+0, door_id,1)

                #include step for door
                self.door_step(length,width, "S")
                #windows
                self.windows(length,width,split,floor)
                #lights
                self.lights(length, height, width,split)
                #stairs
                self.stairs(split)
                
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'S')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)
            else:
                #backyard
                backyard_choices = ['garden', 'pool']
                rand_backyard_choice = random.choice(backyard_choices)
                backyard = Backyard(self.x, self.y, self.z, length, height, width, rand_backyard_choice, 'S')
                #create random rectangular block
                mc.setBlocks(self.x,self.y,self.z, self.x+length, self.y+height, self.z+width, block_id, block_data) 
                #hollow the block
                mc.setBlocks(self.x+1, self.y+1, self.z+1, self.x+length-1, self.y+height-1, self.z+width-1, 0)
                #set corner pillars
                mc.setBlocks(self.x,self.y,self.z,self.x+0,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z,self.x+length,self.y+height,self.z+0,corner_id,corner_data)
                mc.setBlocks(self.x+length,self.y,self.z+width,self.x+length,self.y+height,self.z+width,corner_id,corner_data)
                mc.setBlocks(self.x,self.y,self.z+width,self.x+0,self.y+height,self.z+width,corner_id,corner_data)
                #include door
                mc.setBlocks(self.x+(length/2), self.y+2, self.z, self.x+(length/2), self.y+2, self.z+0, door_id,9)
                mc.setBlocks(self.x+(length/2), self.y+1, self.z, self.x+(length/2), self.y+1, self.z+0, door_id,1)
                #front windows
                self.windows(length,width)
                #lights
                self.lights(length, height, width,split)
                #include step for door
                self.door_step(length,width, 'S')
                
                #roof
                roof = Roof(self.x, self.y, self.z)
                self.rooftype = random.randint(0,2)
                if self.rooftype == 0:
                    roof.triangle_roof(height,length,width,'S')
                elif self.rooftype == 1:
                    roof.fenced_roof(length,height,width,block_id,block_data)
                elif self.rooftype == 2:
                    roof.pyramid_roof(length, height, width)
                    
            self.recursive_split(length, width, height,block_id,block_data)
            

    def recursive_split(self,rec_length, rec_width, rec_height, block_id,block_data):
        door_loc = rec_length//2
        if rec_length <= 12 and rec_width <= 12:
            return
        else:
            shift_split = random.randint(1,2)
            #splits on z, horizontal
            mc.setBlocks(self.x, self.y+1, self.z+(rec_width/2)+ shift_split, self.x+rec_length-1, self.y+rec_height-1, self.z+(rec_width/2) + shift_split, block_id,block_data)           
            mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+1, self.z, self.x+(rec_length/2) + shift_split, self.y+rec_height-1, self.z+rec_width-1, block_id,block_data)
                 
            #creates a hole thru the walls
            random_hole = random.randrange(1, rec_length//2)
            #creates a hole thru left horizontal wall
            mc.setBlocks(self.x + random_hole, self.y+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole, self.y+2, self.z+(rec_width/2)+ shift_split, 0)
            if rec_height >= 8:
                mc.setBlocks(self.x + random_hole, self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole, self.y+(rec_height/2)+2, self.z+(rec_width/2+ shift_split), 0) 
                mc.setBlocks(self.x + random_hole, self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole, self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, 171,carpet)
            #creates a hole thru right horizontal wall
            mc.setBlocks(self.x + random_hole + (rec_length/2), self.y+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole+(rec_length/2), self.y+2, self.z+(rec_width/2)+ shift_split, 0)  
            if rec_height >= 8:
                mc.setBlocks(self.x + random_hole + (rec_length/2), self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole+(rec_length/2), self.y+(rec_height/2)+2, self.z+(rec_width/2)+ shift_split, 0)  
                mc.setBlocks(self.x + random_hole + (rec_length/2), self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, self.x+random_hole+(rec_length/2), self.y+(rec_height/2)+1, self.z+(rec_width/2)+ shift_split, 171,carpet)  
            #creates a hole thru front vertical wall
            mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+1, self.z + random_hole , self.x+(rec_length/2) + shift_split, self.y+2, self.z+random_hole, 0)
            if rec_height >= 8:
                mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z + random_hole , self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+2, self.z+random_hole, 0)
                mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z + random_hole , self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z+random_hole, 171,carpet)
            #creates a hole thru back vertical wall
            mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+1, self.z + random_hole + (rec_width//2)+ shift_split, self.x+(rec_length/2) + shift_split, self.y+2, self.z+random_hole + (rec_width//2)+ shift_split, 0)
            if rec_height >= 8:
                mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z + random_hole + (rec_width//2)+ shift_split , self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+2, self.z+random_hole + (rec_width//2)+ shift_split, 0)
                mc.setBlocks(self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z + random_hole + (rec_width//2)+ shift_split , self.x+(rec_length/2) + shift_split, self.y+(rec_height/2)+1, self.z+random_hole + (rec_width//2)+ shift_split, 171,carpet)
            
            #recursive call
            self.recursive_split((rec_length//2) + shift_split, (rec_width//2) + shift_split, rec_height, block_id, block_data)



        

       
            
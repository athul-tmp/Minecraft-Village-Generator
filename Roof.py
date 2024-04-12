from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

class Roof:
    def __init__(self,x, y,z):
        self.x = x
        self.y = y
        self.z = z

    #triangle roof
    def triangle_roof(self,height, length,width, dir = ''):
        
        count = height+1
        times_build = -1
        count_outer = height+1
        times_build_outer = 0   

        roof_ids = [4, 5, 45, 98]
        data = 0
        if roof_ids == 5:
            data = random.choice([0,1,2,3,4,5])
        random_roof = random.choice(roof_ids)

        if random_roof == 4:
            random_roof_slope = 67

        elif random_roof == 5:
            if data == 0:
                random_roof_slope = 53
            elif data == 1:
                random_roof_slope = 134
            elif data == 2:
                random_roof_slope = 135
            elif data == 3:
                random_roof_slope = 136
            elif data == 4:
                random_roof_slope = 163
            else:
                random_roof_slope = 164

        elif random_roof == 45:
            random_roof_slope = 108

        else:
            random_roof_slope = 109

        #for south and north
        if dir == 'N' or dir == 'S':
            counter = length//2 + 1
            counter_inner = counter
            while counter > 0:               
                # outer roof
                mc.setBlocks(self.x+times_build,self.y+count,self.z-1,self.x+times_build,self.y+count,self.z+width+1,random_roof_slope, 0)
                mc.setBlocks(self.x+times_build+1,self.y+count,self.z-1,self.x+times_build+1,self.y+count,self.z+width+1,random_roof)
                #outer roof
                mc.setBlocks(self.x+length-times_build,self.y+count,self.z-1,self.x+length-times_build,self.y+count,self.z+width+1,random_roof_slope, 1) 
                mc.setBlocks(self.x+length-times_build-1,self.y+count,self.z-1,self.x+length-times_build-1,self.y+count,self.z+width+1,random_roof)
                count+=1
                times_build+=1
                counter-=1
            
            while counter_inner > 1:
                #fill inner area of roof
                mc.setBlocks(self.x+times_build_outer+1,self.y+count_outer,self.z,self.x+length-times_build_outer-1,self.y+count_outer,self.z+width,random_roof) 
                count_outer+=1
                times_build_outer+=1
                counter_inner-=1
        
        #for east and west
        else:
            counter = width//2 + 1
            counter_inner = counter
            while counter > 0:    
                # outer roof
                mc.setBlocks(self.x-1,self.y+count,self.z+times_build,self.x+length+1,self.y+count,self.z+times_build,random_roof_slope, 2)
                mc.setBlocks(self.x-1,self.y+count,self.z+times_build+1,self.x+length+1,self.y+count,self.z+times_build+1,random_roof)
                #outer roof
                mc.setBlocks(self.x-1,self.y+count,self.z+width-times_build,self.x+length+1,self.y+count,self.z+width-times_build,random_roof_slope, 3) 
                mc.setBlocks(self.x-1,self.y+count,self.z+width-times_build-1,self.x+length+1,self.y+count,self.z+width-times_build-1,random_roof)
                count+=1
                times_build+=1
                counter-=1
            
            while counter_inner > 1:
                #fill inner area of roof
                mc.setBlocks(self.x,self.y+count_outer,self.z+times_build_outer+1,self.x+length,self.y+count_outer,self.z+width-times_build_outer-1,random_roof) 
                count_outer+=1
                times_build_outer+=1
                counter_inner-=1



    #roof with fencing
    def fenced_roof(self,length,height,width,block_id,block_data):
        fence_ids = [85, 113, 188, 189, 190, 191, 192]
        random_fence = random.choice(fence_ids)
        mc.setBlocks(self.x-1,self.y+height+1,self.z-1, self.x+length+1, self.y+height+1, self.z+width+1, block_id, block_data)
        mc.setBlocks(self.x-1,self.y+height+2,self.z-1, self.x+length+1, self.y+height+2, self.z+width+1, block_id, block_data)
        mc.setBlocks(self.x,self.y+height+2,self.z, self.x+length, self.y+height+2, self.z+width, 0)
        mc.setBlocks(self.x-1,self.y+height+3,self.z-1, self.x+length+1, self.y+height+3, self.z+width+1, random_fence)
        mc.setBlocks(self.x,self.y+height+3,self.z, self.x+length, self.y+height+3, self.z+width, 0)

        #sets blocks around fenced area so that fences connect properly
        mc.setBlocks(self.x-1-1,self.y+height+3,self.z-1-1, self.x+length+1+1, self.y+height+3, self.z-1-1, 1)
        mc.setBlocks(self.x+length+1+1, self.y+height+3, self.z-1-1,self.x+length+1+1, self.y+height+3, self.z+width+1+1, 1)
        mc.setBlocks(self.x+length+1+1, self.y+height+3, self.z+width+1+1, self.x-1-1, self.y+height+3, self.z+width+1+1, 1)
        mc.setBlocks(self.x-1-1, self.y+height+3, self.z+width+1+1, self.x-1-1, self.y+height+3, self.z-1-1, 1)
        #deletes the blocks after the fences connect
        mc.setBlocks(self.x-1-1,self.y+height+3,self.z-1-1, self.x+length+1+1, self.y+height+3, self.z-1-1, 0)
        mc.setBlocks(self.x+length+1+1, self.y+height+3, self.z-1-1,self.x+length+1+1, self.y+height+3, self.z+width+1+1, 0)
        mc.setBlocks(self.x+length+1+1, self.y+height+3, self.z+width+1+1, self.x-1-1, self.y+height+3, self.z+width+1+1, 0)
        mc.setBlocks(self.x-1-1, self.y+height+3, self.z+width+1+1, self.x-1-1, self.y+height+3, self.z-1-1, 0)

    #pyramid roof
    def pyramid_roof(self, length, height, width):
        roof_height_start = height+1
        roof_height_end = height+1
        roof_width_end = width+1
        roof_length_end = length+1
        roof_length_width_start = -1
        roof_block_id = random.choice([4, 5, 45, 98])

        if roof_length_end > roof_width_end:
            max = roof_length_end
        elif roof_width_end > roof_length_end:
            max = roof_width_end
        else: 
            max = roof_width_end

        while max > 0:
            mc.setBlocks(self.x+roof_length_width_start,self. y+roof_height_start, self.z+roof_length_width_start, self.x+roof_length_end,  self.y+roof_height_end, self.z+roof_width_end, roof_block_id)
            roof_height_start+=1
            roof_height_end+=1
            roof_length_end-=1
            roof_width_end -=1
            roof_length_width_start +=1

            max -=3
    
        #fenced roof types
        house_block_id = [1, 4, 5, 45]
        block_id = random.choice(house_block_id)
        block_data = 0
        if block_id == 1:
            block_data = random.choice([0,1,2,3,4,5,6])
        if block_id == 5:
            block_data = random.choice([0,1,2,3,4,5])
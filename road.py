from mcpi.minecraft import Minecraft
from mcpi import block
import random
from Streetlights import Streetlights
from House import House
from Trees import Trees

mc = Minecraft.create()


class NewPath:
    def __init__(self,start_x,start_y,start_z,dir=''):
        self.x = start_x
        self.y = start_y
        self.z = start_z
        self.dir = dir

    def min_max_height(self,min,max, y):
        #temp_min = 0
        if y < min:
            return y, max
        return min , y
    def fill_beneath_path(self, x_val, curr_y, prev_y, z_val):
        # num = prev_y - curr_y
        # for x in range(1,num):
        #     mc.setBlocks(x_val, curr_y + x, z_val, 2)
        #     lll = mc.getHeight(x_val, z_val)
        #     print(lll)
        num = abs(prev_y - curr_y)
        if num > 2:
            mc.setBlocks(x_val, curr_y, z_val, x_val, prev_y, z_val,2)
            
    def cut_path(self, x_val, curr_y, next_y, z_val):
        diff = next_y - curr_y
        if diff > 2:
            mc.setBlocks(x_val, curr_y, z_val, x_val, next_y , z_val, 0)  
            
    def walkable_paths(self, y_heights):
        for x in range(1, len(y_heights)):
            if y_heights[x] - y_heights[x-1] < 1: #if next larger than 2
                y_heights[x] = y_heights[x-1] + 1
            else: 
                y_heights[x] = y_heights[x-1] - 1
        return y_heights

    def build_road(self, end_x,end_y,end_z,dir=''):
        # list for items to remove
        wood_log = ['oak_log', 'spruce_log', 'birch_log', 'jungle_log', 'dark_oak_log', 'red_mushroom_block', 'mushroom_stem']
        tree_leaves = ['oak_leaves', 'spruce_leaves', 'birch_leaves', 'jungle_leaves','dark_oak_leaves']
        counter = 0 # for lights
        counter_2 = 0 # for lights
        #buffer for houses/roads
        buffer = 5
        # for alternating streetlights
        alternate = True
        #roads with turns
        turns = random.choice([3,6])
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        if turns == 3:
            x_len = int(self.x - end_x)
            z_len = int(self.z - end_z)

            if x_len < 0:
                #SE quad +x +z
                if z_len < 0:
                    random_x = random.randint(5,abs(x_len//2))
                    random_z = random.randint(3,abs(z_len//2))

                    #terraform first paths
                    first_path_height = mc.getHeights(self.x ,self.z, self.x + random_x, self.z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    terraformed_heights = self.walkable_paths(first_path_height)
                    #build road
                    for path_x in range(self.x,self.x+random_x): #start path going east (+x)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z)
                        prev_y = mc.getHeight(path_x - 1, self.z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z)
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z)
                        mc.setBlock(path_x,new_y, self.z, 4)

                    #terraform second paths
                    second_path_height = mc.getHeights(self.x + random_x ,self.z, self.x + random_x, self.z + random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_z in range(self.z,self.z+random_z): #branch out south (+z)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {second_path_min} {path_z - 1} {self.x + random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {second_path_min} {path_z - 1} {self.x + random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x + random_x, path_z)
                        prev_y = mc.getHeight(self.x + random_x, path_z - 1)
                        self.fill_beneath_path(self.x + random_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(self.x + random_x, path_z)
                        mc.setBlock(self.x + random_x,new_y, path_z, 4)
                            
                    #terraform third paths
                    third_path_height = mc.getHeights(self.x + random_x ,self.z + random_z, end_x, self.z + random_z)
                    third_path_min = min(first_path_height)
                    third_path_max = max(first_path_height) + 10 #for extra leaves       
                    for path_x in range(self.x+random_x,end_x): #moves to end x
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z + random_z - buffer} {path_x+1} {third_path_max} {self.z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z + random_z - buffer} {path_x+1} {third_path_max} {self.z + random_z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z + random_z )
                        prev_y = mc.getHeight(path_x - 1, self.z + random_z )
                        self.fill_beneath_path(path_x,y, prev_y, self.z + random_z ) 
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z + random_z )
                        mc.setBlock(path_x,new_y, self.z + random_z , 4)
                        
                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(end_x ,self.z + random_z, end_x,end_z)
                    fourth_path_min = min(second_path_height)
                    fourth_path_max = max(second_path_height) + 10  #for extra leaves    
                    for path_z in range(self.z+random_z,end_z-1): #moves to end z
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(end_x, path_z)
                        prev_y = mc.getHeight(end_x, path_z - 1)
                        self.fill_beneath_path(end_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(end_x, path_z)
                        mc.setBlock(end_x,new_y, path_z, 4)

                        counter_2 += 1
                        #streetlights
                        if (counter_2 % 6 == 0) and ((path_z < end_z - 5) or (path_z > self.z + random_z + 5)):
                            new_streetlight = Streetlights(self.x+random_x+3,new_y,path_z)
                            new_streetlight.build_streetlight()

                    #places house south
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    #new house height
                    house_y = mc.getHeight(end_x ,end_z) + 1
                    build_house = House(end_x-(length//2),house_y,end_z)
                    build_house.build_house(length,height,width)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # NE quad +x -z 
                else:
                    random_x = random.randint(3,abs(x_len//2))
                    random_z = random.randint(3,abs(z_len//2))
                    
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x ,self.z, self.x + random_x, self.z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    for path_x in range(self.x,self.x+random_x): #start path going east (+x)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z)
                        prev_y = mc.getHeight(path_x - 1, self.z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z)
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z)
                        mc.setBlock(path_x,new_y, self.z, 4)
                        
                    #terraform second paths
                    second_path_height = mc.getHeights(self.x + random_x ,self.z, self.x + random_x, self.z - random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves   
                    for path_z in range(self.z,self.z-random_z,-1): #branch out north (-z)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {second_path_min} {path_z - 1} {self.x + random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {second_path_min} {path_z - 1} {self.x + random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x + random_x, path_z)
                        prev_y = mc.getHeight(self.x + random_x, path_z + 1)
                        self.fill_beneath_path(self.x + random_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(self.x + random_x, path_z)
                        mc.setBlock(self.x + random_x,new_y, path_z, 4)
                        counter += 1
                        #streetlights
                        if counter == (self.z - random_z) // 2:
                            new_streetlight = Streetlights(self.x+random_x+3,new_y,path_z)
                            new_streetlight.build_streetlight()
                            
                    #terraform third paths
                    third_path_height = mc.getHeights(self.x + random_x ,self.z - random_z, end_x, self.z - random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10 #for extra leaves        
                    for path_x in range(self.x+random_x,end_x): #moves to end x
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z - random_z - buffer} {path_x+1} {third_path_max} {self.z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z - random_z - buffer} {path_x+1} {third_path_max} {self.z - random_z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z - random_z )
                        prev_y = mc.getHeight(path_x - 1, self.z - random_z )
                        self.fill_beneath_path(path_x,y, prev_y, self.z - random_z ) 
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z - random_z )
                        mc.setBlock(path_x,new_y, self.z - random_z , 4)
                        
                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(end_x ,self.z - random_z, end_x,end_z)
                    fourth_path_min = min(second_path_height)
                    fourth_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_z in range(self.z-random_z,end_z,-1): #moves to end z
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(end_x, path_z)
                        prev_y = mc.getHeight(end_x, path_z + 1)
                        self.fill_beneath_path(end_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(end_x, path_z)
                        mc.setBlock(end_x,new_y, path_z, 4)

                        counter_2 += 1
                        #streetlights
                        if (counter_2 % 6 == 0) and ((path_z < end_z - 5) or (path_z > self.z + random_z + 5)):
                            new_streetlight = Streetlights(self.x+random_x+3,new_y,path_z)
                            new_streetlight.build_streetlight()

                    #north facing road
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x - (length//2),y+1,end_z - width,'N') # start
                    build_house.build_house(length,height,width) # end
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if x_len > 0:        
                #SW quad -x +z
                if z_len < 0:
                    random_x = random.randint(3,abs(x_len//2))
                    random_z = random.randint(3,abs(z_len//2))
                    
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x ,self.z, self.x - random_x, self.z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    for path_x in range(self.x,self.x-random_x,-1): #start path going west (-x)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z+buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z+buffer} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z)
                        prev_y = mc.getHeight(path_x + 1, self.z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z)
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z)
                        mc.setBlock(path_x,new_y, self.z, 4)
                        
                        
                    #terraform second paths
                    second_path_height = mc.getHeights(self.x - random_x ,self.z, self.x - random_x, self.z + random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_z in range(self.z,self.z+random_z): #branch out south (+z)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x-random_x-buffer} {second_path_min} {path_z -1} {self.x-random_x+buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x-random_x-buffer} {second_path_min} {path_z -1} {self.x-random_x+buffer} {second_path_max} {path_z +1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x - random_x, path_z)
                        prev_y = mc.getHeight(self.x - random_x, path_z - 1)
                        self.fill_beneath_path(self.x - random_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(self.x - random_x, path_z)
                        mc.setBlock(self.x - random_x,new_y, path_z, 4)

                        counter += 1
                        #streetlights
                        if (counter % 6 == 0) and ((path_z < self.z + random_z - 5) or (path_z > self.z + 5)):
                            new_streetlight = Streetlights(self.x-random_x+3,new_y,path_z)
                            new_streetlight.build_streetlight()
                            
                    #terraform third paths
                    third_path_height = mc.getHeights(self.x - random_x ,self.z + random_z, end_x, self.z + random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10 #for extra leaves                           
                    for path_x in range(self.x-random_x,end_x,-1): #moves to end x
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z + random_z - buffer} {path_x+1} {third_path_max} {self.z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z + random_z - buffer} {path_x+1} {third_path_max} {self.z + random_z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z + random_z )
                        prev_y = mc.getHeight(path_x + 1, self.z + random_z )
                        self.fill_beneath_path(path_x,y, prev_y, self.z + random_z ) 
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z + random_z )
                        mc.setBlock(path_x,new_y, self.z + random_z , 4)
                        

                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(end_x ,self.z + random_z, end_x,end_z)
                    fourth_path_min = min(second_path_height)
                    fourth_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_z in range(self.z+random_z,end_z-1): #moves to end z
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(end_x, path_z)
                        prev_y = mc.getHeight(end_x, path_z - 1)
                        self.fill_beneath_path(end_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(end_x, path_z)
                        mc.setBlock(end_x,new_y, path_z, 4)

                        counter_2 += 1
                        #streetlights
                        if (counter_2 % 6 == 0) and ((path_z < end_z - 5) or (path_z > self.z + random_z + 5)):
                            new_streetlight = Streetlights(self.x+random_x+3,new_y,path_z)
                            new_streetlight.build_streetlight()
                    #places house south facing road
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x-(length//2),y+1,end_z)
                    build_house.build_house(length,height,width)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                #NW quad -x -z
                else:
                    random_x = random.randint(3,abs(x_len//2))
                    random_z = random.randint(3,abs(z_len//2))
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x ,self.z, self.x - random_x, self.z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    for path_x in range(self.x,self.x-random_x,-1): #start path going west(-x)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z+buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {first_path_min} {self.z - buffer} {path_x+1} {first_path_max} {self.z+buffer} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z)
                        prev_y = mc.getHeight(path_x + 1, self.z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z)
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z)
                        mc.setBlock(path_x,new_y, self.z, 4)
                        
                    #terraform second paths
                    second_path_height = mc.getHeights(self.x - random_x ,self.z, self.x - random_x, self.z - random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves   
                    for path_z in range(self.z,self.z-random_z,-1): #branch out north(-z)
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {second_path_min} {path_z - 1} {self.x - random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {second_path_min} {path_z - 1} {self.x - random_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x - random_x, path_z)
                        prev_y = mc.getHeight(self.x - random_x, path_z + 1)
                        self.fill_beneath_path(self.x - random_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(self.x - random_x, path_z)
                        mc.setBlock(self.x - random_x,new_y, path_z, 4)
                        counter += 1

                        #streetlights
                        if (counter % 6 == 0) and (counter < 18):
                            new_streetlight = Streetlights(self.x-random_x-2,new_y,path_z)
                            new_streetlight.build_streetlight()
                            
                    #terraform third paths
                    third_path_height = mc.getHeights(self.x - random_x ,self.z - random_z, end_x, self.z - random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10 #for extra leaves        
                    for path_x in range(self.x-random_x,end_x,-1): #moves to end x
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z - random_z - buffer} {path_x+1} {third_path_max} {self.z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {third_path_min} {self.z - random_z - buffer} {path_x+1} {third_path_max} {self.z - random_z + buffer} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z - random_z )
                        prev_y = mc.getHeight(path_x - 1, self.z - random_z )
                        self.fill_beneath_path(path_x,y, prev_y, self.z - random_z ) 
                        
                        #get new height
                        new_y = mc.getHeight(path_x, self.z - random_z )
                        mc.setBlock(path_x,new_y, self.z - random_z , 4)
                        
                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(end_x ,self.z - random_z, end_x,end_z)
                    fourth_path_min = min(second_path_height)
                    fourth_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_z in range(self.z-random_z,end_z,-1): #moves to end z
                        #replace trees
                        for x in wood_log:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {end_x - buffer} {second_path_min} {path_z - 1} {end_x + buffer} {second_path_max} {path_z + 1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(end_x, path_z)
                        prev_y = mc.getHeight(end_x, path_z + 1)
                        self.fill_beneath_path(end_x ,y, prev_y, path_z)
                        
                        #get new height
                        new_y = mc.getHeight(end_x, path_z)
                        mc.setBlock(end_x,new_y, path_z, 4)
                        counter_2 += 1
                        #streetlights
                        if (counter_2 % 6 == 0) and (counter_2 < 18):
                            new_streetlight = Streetlights(end_x-2,new_y,path_z)
                            new_streetlight.build_streetlight()

                    #north facing road
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x - (length//2),y+1,end_z - width,'N') # start
                    build_house.build_house(length,height,width) # end

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # #else turns = 6
        if turns == 6:
            x_len = int(self.x - end_x)
            z_len = int(self.z - end_z)

            if x_len < 0:

                #NE quad +x -z
                if z_len > 0:
                    temp_x = abs(x_len//3)
                    temp_z = abs(z_len//3)
                    random_z = random.randint(10,temp_z)
                    random_x = random.randint(7,temp_x)
                    
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x,self.z, self.x, self.z-random_z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves

                    for path_z in range(self.z, self.z-random_z,-1): #start path going north (-z)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x-buffer} {first_path_min} {path_z-1} {self.x+buffer} {first_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x-buffer} {first_path_min} {path_z-1} {self.x+buffer} {first_path_max} {path_z+1} minecraft:air replace {x}')

                        # simple terraforming    
                        y = mc.getHeight(self.x, path_z)
                        prev_y = mc.getHeight(self.x, path_z + 1)
                        self.fill_beneath_path(self.x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x, path_z)                     
                        mc.setBlock(self.x, new_y, path_z, 4)
                        
                        
                    #terraform second paths
                    second_path_height = mc.getHeights(self.x,self.z - random_z, self.x + random_x, self.z - random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_x in range(self.x, self.x+random_x): #branch out east (+x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z - random_z - buffer} {path_x+1} {second_path_max} {self.z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z - random_z - buffer} {path_x+1} {second_path_max} {self.z - random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z - random_z)
                        prev_y = mc.getHeight(path_x - 1, self.z - random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z-random_z)
                        
                        #set path blocks
                        new_y = mc.getHeight(path_x, self.z - random_z)
                        mc.setBlock(path_x, new_y, self.z-random_z, 4)
                        

                    # terraform third path
                    third_path_height = mc.getHeights(self.x + random_x ,self.z - random_z, self.x + random_x, self.z-random_z-random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10  #for extra leaves   
                    for path_z in range(self.z-random_z, self.z-random_z-random_z,-1): #continue north (-z)
                        # replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {third_path_min} {path_z-1} {self.x + random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {third_path_min} {path_z-1} {self.x + random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x+random_x, path_z)
                        prev_y = mc.getHeight(self.x+random_x, path_z + 1)
                        self.fill_beneath_path(self.x+random_x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x+random_x, path_z)                   
                        mc.setBlock(self.x+random_x, new_y, path_z, 4)
                        
                        counter += 1
                        #streetlights
                        if path_z == ((self.z - random_z) - (self.z-random_z-random_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight()
                            

                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(self.x + random_x, self.z - random_z - random_z, self.x + random_x + random_x, self.z - random_z - random_z)
                    fourth_path_min = min(fourth_path_height) 
                    fourth_path_max = max(fourth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x+random_x, self.x+random_x+random_x): #continue east (+x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z - random_z - random_z - buffer} {path_x+1} {fourth_path_max} {self.z - random_z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z - random_z - random_z - buffer} {path_x+1} {fourth_path_max} {self.z - random_z - random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z-random_z-random_z)
                        prev_y = mc.getHeight(path_x - 1, self.z-random_z-random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z-random_z-random_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, self.z-random_z-random_z)
                        mc.setBlock(path_x, new_y, self.z-random_z-random_z, 4)
                        
                        
                    # terraform fifth path
                    fifth_path_height = mc.getHeights(self.x + random_x + random_x ,self.z - random_z - random_z, self.x + random_x + random_x, end_z)
                    fifth_path_min = min(fifth_path_height)
                    fifth_path_max = max(fifth_path_height) + 10 #for extra leaves
                    for path_z in range(self.z-random_z-random_z, end_z,-1): #move to end z
                        #replace wood and leafs
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x+random_x+random_x - buffer} {fifth_path_min} {path_z-1} {self.x+random_x+random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x+random_x+random_x - buffer} {fifth_path_min} {path_z-1} {self.x+random_x+random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x+random_x+random_x, path_z)
                        prev_y = mc.getHeight(self.x+random_x+random_x, path_z+1)
                        self.fill_beneath_path(self.x+random_x+random_x, y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x+random_x+random_x, path_z)                    
                        mc.setBlock(self.x+random_x+random_x, new_y, path_z, 4)
                        
                        #streetlights
                        if path_z == ((self.z - random_z - random_z) - (end_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight() 
                            
                            
                    #terraform sixth path
                    sixth_path_height = mc.getHeights(self.x + random_x + random_x, end_z, end_x, end_z)
                    sixth_path_min = min(sixth_path_height) 
                    sixth_path_max = max(sixth_path_height) + 10  #for extra leaves           
                    for path_x in range(self.x+random_x+random_x, end_x): #move to end x
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1 } {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, end_z)
                        prev_y = mc.getHeight(path_x -1, end_z)
                        self.fill_beneath_path(path_x,y, prev_y, end_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, end_z)
                        mc.setBlock(path_x, new_y, end_z, 4)

                    #east
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x,y+1,end_z- (width//2),'E')
                    build_house.build_house(length,height,width)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #SE quad +x +z
                else:
                    temp_x = abs(x_len//3)
                    temp_z = abs(z_len//3)
                    random_z = random.randint(7,temp_x)
                    random_x = random.randint(7,temp_x)
                    
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x,self.z, self.x, self.z+random_z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    for path_z in range(self.z, self.z+random_z): #start path going south (+z)
                        # replace wood and leaf
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x - buffer} {first_path_min} {path_z-1} {self.x  + buffer} {first_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x  - buffer} {first_path_min} {path_z-1} {self.x  + buffer} {first_path_max} {path_z+1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x, path_z)
                        prev_y = mc.getHeight(self.x, path_z - 1)
                        self.fill_beneath_path(self.x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x, path_z)                     
                        mc.setBlock(self.x, new_y, path_z, 4)    
                        

                    #terraform second paths
                    second_path_height = mc.getHeights(self.x,self.z + random_z, self.x + random_x, self.z + random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_x in range(self.x, self.x+random_x): #branch out east (+x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z + random_z - buffer} {path_x+1} {second_path_max} {self.z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z + random_z - buffer} {path_x+1} {second_path_max} {self.z + random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z + random_z)
                        prev_y = mc.getHeight(path_x - 1, self.z + random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z+random_z)
                        
                        #set path blocks
                        new_y = mc.getHeight(path_x, self.z + random_z)
                        mc.setBlock(path_x, new_y, self.z+random_z, 4)
                        
                        
                    # terraform third path
                    third_path_height = mc.getHeights(self.x + random_x ,self.z + random_z, self.x + random_x, self.z+random_z+random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10  #for extra leaves
                    for path_z in range(self.z+random_z, self.z+random_z+random_z): #continue south (+z)
                        # replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {third_path_min} {path_z-1} {self.x + random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x + random_x - buffer} {third_path_min} {path_z-1} {self.x + random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(self.x+random_x, path_z)
                        prev_y = mc.getHeight(self.x+random_x, path_z - 1)
                        self.fill_beneath_path(self.x+random_x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x+random_x, path_z)                   
                        mc.setBlock(self.x+random_x, new_y, path_z, 4)
                        
                        counter += 1
                        #streetlights
                        if counter == ((self.z + random_z + random_z) - (self.z+random_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z+random_z-2)
                            new_streetlight.build_streetlight()
                            
                            
                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(self.x + random_x, self.z + random_z + random_z, self.x + random_x + random_x, self.z + random_z + random_z)
                    fourth_path_min = min(fourth_path_height) 
                    fourth_path_max = max(fourth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x+random_x, self.x+random_x+random_x): #continue east (+x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z + random_z + random_z - buffer} {path_x+1} {fourth_path_max} {self.z + random_z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z + random_z + random_z - buffer} {path_x+1} {fourth_path_max} {self.z + random_z + random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z+random_z+random_z)
                        prev_y = mc.getHeight(path_x - 1, self.z+random_z+random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z+random_z+random_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, self.z+random_z+random_z)
                        mc.setBlock(path_x, new_y, self.z+random_z+random_z, 4)
                        
                        
                    # terraform fifth path
                    fifth_path_height = mc.getHeights(self.x + random_x + random_x ,self.z + random_z + random_z, self.x + random_x + random_x, end_z)
                    fifth_path_min = min(fifth_path_height)
                    fifth_path_max = max(fifth_path_height) + 10 #for extra leaves
                    counter = 0
                    for path_z in range(self.z+random_z+random_z, end_z): #move to end z
                        #replace wood and leafs
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x+random_x+random_x - buffer} {fifth_path_min} {path_z-1} {self.x+random_x+random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x+random_x+random_x - buffer} {fifth_path_min} {path_z-1} {self.x+random_x+random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x+random_x+random_x, path_z)
                        prev_y = mc.getHeight(self.x+random_x+random_x, path_z-1)
                        self.fill_beneath_path(self.x+random_x+random_x, y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x+random_x+random_x, path_z)                    
                        mc.setBlock(self.x+random_x+random_x, new_y, path_z, 4)
                        
                        #streetlights
                        counter += 1
                        if counter == ((self.z + random_z + random_z) + (end_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight()
                            
                            
                    #terraform sixth path
                    sixth_path_height = mc.getHeights(self.x + random_x + random_x, end_z, end_x, end_z)
                    sixth_path_min = min(sixth_path_height) 
                    sixth_path_max = max(sixth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x+random_x+random_x, end_x): #move to end x
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1 } {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, end_z)
                        prev_y = mc.getHeight(path_x -1, end_z)
                        self.fill_beneath_path(path_x,y, prev_y, end_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, end_z)
                        mc.setBlock(path_x, new_y, end_z, 4)
                        
                    #east house
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x,y+1,end_z- (width//2),'E')
                    build_house.build_house(length,height,width)
                    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            if x_len > 0:
                #SW quad -x, +z
                if z_len < 0:
                    temp_x = abs(x_len//3)
                    temp_z = abs(z_len//3)
                    random_z = random.randint(7,temp_x)
                    random_x = random.randint(7,temp_x)
                    
                    
                    #terraform first paths
                    first_path_height = mc.getHeights(self.x,self.z, self.x, self.z+random_z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    
                    for path_z in range(self.z, self.z+random_z): #start path going south (+z)
                        # replace wood and leaf
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x - buffer} {first_path_min} {path_z-1} {self.x  + buffer} {first_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x  - buffer} {first_path_min} {path_z-1} {self.x  + buffer} {first_path_max} {path_z+1} minecraft:air replace {x}')

                        #simple terraforming    
                        y = mc.getHeight(self.x, path_z)
                        prev_y = mc.getHeight(self.x, path_z - 1)
                        self.fill_beneath_path(self.x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x, path_z)                     
                        mc.setBlock(self.x, new_y, path_z, 4)
                        
                    #terraform second paths
                    second_path_height = mc.getHeights(self.x,self.z + random_z, self.x - random_x, self.z + random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves    
                    for path_x in range(self.x, self.x-random_x,-1): #branch out west (-x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z + random_z - buffer} {path_x+1} {second_path_max} {self.z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z + random_z - buffer} {path_x+1} {second_path_max} {self.z + random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z + random_z)
                        prev_y = mc.getHeight(path_x + 1, self.z + random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z+random_z)
                        
                        #set path blocks
                        new_y = mc.getHeight(path_x, self.z + random_z)
                        mc.setBlock(path_x, new_y, self.z+random_z, 4)

                    # terraform third path
                    third_path_height = mc.getHeights(self.x - random_x ,self.z + random_z, self.x - random_x, self.z+random_z+random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10  #for extra leaves
                    counter = 0
                    for path_z in range(self.z+random_z, self.z+random_z+random_z): #continue south (+z)
                        # replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {third_path_min} {path_z-1} {self.x - random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {third_path_min} {path_z-1} {self.x - random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace {x}')
                        #simple terraforming    
                        y = mc.getHeight(self.x-random_x, path_z)
                        prev_y = mc.getHeight(self.x-random_x, path_z - 1)
                        self.fill_beneath_path(self.x-random_x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x-random_x, path_z)                   
                        mc.setBlock(self.x-random_x, new_y, path_z, 4)
                        
                        counter += 1
                        #streetlights
                        if counter == ((self.z + random_z + random_z) - (self.z+random_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z+random_z-2)
                            new_streetlight.build_streetlight()

                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(self.x - random_x, self.z + random_z + random_z, self.x - random_x - random_x, self.z + random_z + random_z)
                    fourth_path_min = min(fourth_path_height) 
                    fourth_path_max = max(fourth_path_height) + 10  #for extra leaves            
                    for path_x in range(self.x-random_x, self.x-random_x-random_x,-1): #continue west (-x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z + random_z + random_z - buffer} {path_x+1} {fourth_path_max} {self.z + random_z + random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z + random_z + random_z - buffer} {path_x+1} {fourth_path_max} {self.z + random_z + random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z+random_z+random_z)
                        prev_y = mc.getHeight(path_x + 1, self.z+random_z+random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z+random_z+random_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, self.z+random_z+random_z)
                        mc.setBlock(path_x, new_y, self.z+random_z+random_z, 4)

                    # terraform fifth path
                    fifth_path_height = mc.getHeights(self.x - random_x - random_x ,self.z + random_z + random_z, self.x - random_x - random_x, end_z)
                    fifth_path_min = min(fifth_path_height)
                    fifth_path_max = max(fifth_path_height) + 10 #for extra leaves
                    counter = 0
                    for path_z in range(self.z+random_z+random_z, end_z): #move to end z
                        #replace wood and leafs
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x-random_x-random_x - buffer} {fifth_path_min} {path_z-1} {self.x-random_x-random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x-random_x-random_x - buffer} {fifth_path_min} {path_z-1} {self.x-random_x-random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x-random_x-random_x, path_z)
                        prev_y = mc.getHeight(self.x-random_x-random_x, path_z-1)
                        self.fill_beneath_path(self.x-random_x-random_x, y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x-random_x-random_x, path_z)                    
                        mc.setBlock(self.x-random_x-random_x, new_y, path_z, 4)
                        
                        #streetlights
                        counter += 1
                        if counter == ( (end_z) - (self.z + random_z + random_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight()
                            
                    #terraform sixth path
                    sixth_path_height = mc.getHeights(self.x - random_x - random_x, end_z, end_x, end_z)
                    sixth_path_min = min(sixth_path_height) 
                    sixth_path_max = max(sixth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x-random_x-random_x, end_x,-1): #move to end x
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1 } {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, end_z)
                        prev_y = mc.getHeight(path_x + 1, end_z)
                        self.fill_beneath_path(path_x,y, prev_y, end_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, end_z)
                        mc.setBlock(path_x, new_y, end_z, 4)
                        
                    #west road
                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x-length,y+1,end_z - (width//2),'W')
                    build_house.build_house(length,height,width)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                #NW quad -x -z
                else:
                    temp_x = abs(x_len//3)
                    temp_z = abs(z_len//3)
                    random_z = random.randint(7,temp_x)
                    random_x = random.randint(7,temp_x)

                    #terraform first paths
                    first_path_height = mc.getHeights(self.x,self.z, self.x, self.z-random_z)
                    first_path_min = min(first_path_height)
                    first_path_max = max(first_path_height) + 10 #for extra leaves
                    for path_z in range(self.z, self.z-random_z,-1): #start path going north (-z)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x-buffer} {first_path_min} {path_z-1} {self.x+buffer} {first_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x-buffer} {first_path_min} {path_z-1} {self.x+buffer} {first_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x, path_z)
                        prev_y = mc.getHeight(self.x, path_z + 1)
                        self.fill_beneath_path(self.x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x, path_z)                     
                        mc.setBlock(self.x, new_y, path_z, 4)

                    #terraform second paths
                    second_path_height = mc.getHeights(self.x,self.z - random_z, self.x - random_x, self.z - random_z)
                    second_path_min = min(second_path_height)
                    second_path_max = max(second_path_height) + 10  #for extra leaves
                    for path_x in range(self.x, self.x-random_x,-1): #branch out west (-x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z - random_z - buffer} {path_x+1} {second_path_max} {self.z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {second_path_min} {self.z - random_z - buffer} {path_x+1} {second_path_max} {self.z - random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z - random_z)
                        prev_y = mc.getHeight(path_x + 1, self.z - random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z - random_z)
                        
                        #set path blocks
                        new_y = mc.getHeight(path_x, self.z - random_z)
                        mc.setBlock(path_x, new_y, self.z-random_z, 4)
                        
                    # terraform third path
                    third_path_height = mc.getHeights(self.x - random_x ,self.z - random_z, self.x - random_x, self.z-random_z-random_z)
                    third_path_min = min(third_path_height)
                    third_path_max = max(third_path_height) + 10  #for extra leaves
                    for path_z in range(self.z-random_z, self.z-random_z-random_z,-1): #continue north (-z)
                        # replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {third_path_min} {path_z-1} {self.x - random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x - random_x - buffer} {third_path_min} {path_z-1} {self.x - random_x + buffer} {third_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x-random_x, path_z)
                        prev_y = mc.getHeight(self.x-random_x, path_z + 1)
                        self.fill_beneath_path(self.x-random_x,y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x-random_x, path_z)                   
                        mc.setBlock(self.x-random_x, new_y, path_z, 4)
                        
                        counter += 1
                        #streetlights
                        if path_z == ((self.z - random_z) - (self.z-random_z-random_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight()

                        
                    #terraform fourth paths
                    fourth_path_height = mc.getHeights(self.x - random_x, self.z - random_z - random_z, self.x - random_x - random_x, self.z - random_z - random_z)
                    fourth_path_min = min(fourth_path_height) 
                    fourth_path_max = max(fourth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x-random_x, self.x-random_x-random_x,-1): #continue west (-x)
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z - random_z - random_z - buffer} {path_x+1} {fourth_path_max} {self.z - random_z - random_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1} {fourth_path_min} {self.z - random_z - random_z - buffer} {path_x+1} {fourth_path_max} {self.z - random_z - random_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, self.z-random_z-random_z)
                        prev_y = mc.getHeight(path_x + 1, self.z-random_z-random_z)
                        self.fill_beneath_path(path_x,y, prev_y, self.z-random_z-random_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, self.z-random_z-random_z)
                        mc.setBlock(path_x, new_y, self.z-random_z-random_z, 4)
                        
                        
                    # terraform fifth path
                    fifth_path_height = mc.getHeights(self.x - random_x - random_x ,self.z - random_z - random_z, self.x - random_x - random_x, end_z)
                    fifth_path_min = min(fifth_path_height)
                    fifth_path_max = max(fifth_path_height) + 10 #for extra leaves
                    for path_z in range(self.z-random_z-random_z, end_z,-1): #move to end z
                        #replace wood and leafs
                        for x in wood_log:
                            mc.doCommand(f'fill {self.x-random_x-random_x - buffer} {fifth_path_min} {path_z-1} {self.x-random_x-random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {self.x-random_x-random_x - buffer} {fifth_path_min} {path_z-1} {self.x-random_x-random_x + buffer} {fifth_path_max} {path_z+1} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(self.x-random_x-random_x, path_z)
                        prev_y = mc.getHeight(self.x-random_x-random_x, path_z+1)
                        self.fill_beneath_path(self.x-random_x-random_x, y, prev_y, path_z)
                        
                        # set path blocks  
                        new_y = mc.getHeight(self.x-random_x-random_x, path_z)                    
                        mc.setBlock(self.x-random_x-random_x, new_y, path_z, 4)
                        
                        #streetlights
                        if path_z == ((self.z - random_z - random_z) - (end_z) // 2):
                            new_streetlight = Streetlights(path_x,y,self.z-random_z-2)
                            new_streetlight.build_streetlight() 

                    #terraform sixth path
                    sixth_path_height = mc.getHeights(self.x - random_x - random_x, end_z, end_x, end_z)
                    sixth_path_min = min(sixth_path_height) 
                    sixth_path_max = max(sixth_path_height) + 10  #for extra leaves
                    for path_x in range(self.x-random_x-random_x, end_x,-1): #move to end x
                        #replace leaf and wood
                        for x in wood_log:
                            mc.doCommand(f'fill {path_x-1} {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace minecraft:{x}')
                        for x in tree_leaves:
                            mc.doCommand(f'fill {path_x-1 } {sixth_path_min} {end_z - buffer} {path_x+1} {sixth_path_max} {end_z + buffer} minecraft:air replace {x}')
                            
                        #simple terraforming    
                        y = mc.getHeight(path_x, end_z)
                        prev_y = mc.getHeight(path_x+1, end_z)
                        self.fill_beneath_path(path_x,y, prev_y, end_z)
                        
                        #set path blocks    
                        new_y = mc.getHeight(path_x, end_z)
                        mc.setBlock(path_x, new_y, end_z, 4)

                    length = random.randrange(20,28, 2) #x-axis
                    width = random.randrange(16,32, 2) #z-axis
                    height = random.randrange(6,11, 2) #y-axis
                    build_house = House(end_x-length,y+1,end_z - (width//2),'W')
                    build_house.build_house(length,height,width)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if dir == 'N':
            # generate values for paths and houses
            loc5_z = (random.randrange(-50,-40)) - buffer
            z_len = loc5_z + self.z
            length = random.randrange(20,28, 2) #x-axis
            width = random.randrange(16,32, 2) #z-axis
            height = random.randrange(6,11, 2) #y-axis
            north_path_height = mc.getHeights(self.x,self.z, self.x, z_len - 1)
            north_min = min(north_path_height)
            north_max = max(north_path_height) + 10 #for extra leaves
            # loop thru path length
            for path_z in range(self.z, z_len,-1):
                #replace trees
                for x in wood_log:
                    mc.doCommand(f'fill {self.x-buffer} {north_min} {path_z-1} {self.x + buffer} {north_max} {path_z} minecraft:air replace minecraft:{x}')
                for x in tree_leaves:
                    mc.doCommand(f'fill {self.x-buffer} {north_min} {path_z-1} {self.x + buffer} {north_max} {path_z} minecraft:air replace {x}')     
                # simple terraforming    
                y = mc.getHeight(self.x, path_z) 
                prev_y = mc.getHeight(self.x, path_z+1) 
                self.fill_beneath_path(self.x, y, prev_y, path_z)

                #place block for path
                new_y = mc.getHeight(self.x, path_z)
                mc.setBlock(self.x, new_y, path_z, 4)
                #streetlights
                counter += 1
                if (counter % 8 == 0) and (counter < z_len - 10): 
                    if alternate:
                        new_streetlight = Streetlights(self.x+3,new_y,path_z-1)
                        new_streetlight.build_streetlight()
                        alternate = False
                    else:
                        new_streetlight = Streetlights(self.x-3,new_y,path_z-1)
                        new_streetlight.build_streetlight()
                        alternate = True
                    
            #get house height at the end
            house_y = mc.getHeight(self.x , z_len) +1
            build_house = House(self.x - (length//2),house_y,self.z + loc5_z-width,'N') # start
            build_house.build_house(length,height,width) # end
            #mc.setBlocks(self.x+(length/2), self.y+2, self.z, self.x+(length/2), self.y+2, self.z+0, door_id,9)#door
            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if dir == 'S':
            # generate values for path and houses
            loc5_z = (random.randrange(40,50)) + buffer
            z_len = loc5_z + self.z
            length = random.randrange(20,28, 2) #x-axis
            width = random.randrange(16,32, 2) #z-axis
            height = random.randrange(6,11, 2) #y-axis
            #terraform straight paths
            south_path_height = mc.getHeights(self.x,self.z, self.x, z_len - 1)
            south_path_min = min(south_path_height)
            south_path_max = max(south_path_height) + 10 # for extra leaves
            
            # loop through path length
            for path_z in range(self.z, z_len-1):
                #replace trees
                for x in wood_log:
                    mc.doCommand(f'fill {self.x-buffer} {south_path_min} {path_z-1} {self.x + buffer} {south_path_max} {path_z} minecraft:air replace minecraft:{x}')
                for x in tree_leaves:
                    mc.doCommand(f'fill {self.x-buffer} {south_path_min} {path_z-1} {self.x + buffer} {south_path_max} {path_z} minecraft:air replace {x}')
                    
                # simple terraforming    
                y = mc.getHeight(self.x, path_z) 
                prev_y = mc.getHeight(self.x, path_z-1)  
                self.fill_beneath_path(self.x, y, prev_y, path_z)
                
                #set blocks
                new_y = mc.getHeight(self.x, path_z)
                mc.setBlock(self.x, new_y, path_z, 4)
                
                #streetlights
                counter += 1
                if (counter % 8 == 0) and (counter < z_len - 10): 
                    if alternate:
                        new_streetlight = Streetlights(self.x+3,new_y,path_z-1)
                        
                        new_streetlight.build_streetlight()
                        alternate = False
                    else:
                        new_streetlight = Streetlights(self.x-3,new_y,path_z-1)
                        new_streetlight.build_streetlight()
                        alternate = True

            #get house height at the end
            house_y = mc.getHeight(self.x, self.z+loc5_z) + 1
            build_house = House(self.x - (length//2),house_y,self.z+loc5_z)
            build_house.build_house(length,height,width
                                    )
       

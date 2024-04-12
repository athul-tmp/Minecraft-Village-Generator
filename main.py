from mcpi.minecraft import Minecraft
from House import House
import random
from road import NewPath
from Fountain import Fountain
from Trees import Trees
from Terraform import Terraform

mc = Minecraft.create()
mc.doCommand(f'/gamerule sendCommandFeedback false')
mc.doCommand(f'time set day')
mc.doCommand(f'gamerule doDaylightCycle false')
x, y, z = mc.player.getPos()

start_x = int(x)
start_y = int(y)
start_z = int(z)

fountain = Fountain(start_x,start_y,start_z)

buffer  = 30
x_pos = [5,10,5,10,-5,-10,-5,-10]
z_pos = [-5,-10,5,10,5,10,-5,-10]

#places house       
loc5_direction = random.choice(['N','S'])
loc5 = NewPath(start_x,start_y,start_z)
loc5.build_road(start_x,start_y-1,start_z,loc5_direction)
for paths in range(0,len(x_pos),2): # generate road to 1 random point in each quadrant
    if x_pos[paths] < 0:
        rand_x = random.randrange(x_pos[paths],x_pos[paths+1],-1) - buffer
    else:
        rand_x = random.randrange(x_pos[paths],x_pos[paths+1]) + buffer
    if z_pos[paths] < 0:
        rand_z = random.randrange(z_pos[paths],z_pos[paths+1],-1) - buffer
    else:
        rand_z = random.randrange(z_pos[paths],z_pos[paths+1]) + buffer
    build_path = NewPath(start_x,start_y,start_z)
    build_path.build_road(start_x+rand_x, start_y-1, start_z+rand_z)
    

fountain.random_fountain()




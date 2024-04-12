from mcpi.minecraft import Minecraft
import random
from Terraform import Terraform
mc = Minecraft.create()

class Backyard:
    def __init__(self, x, y, z, length, height, width, choice,dir =''):
        self.x = x
        self.y = y
        self.z = z
        self.choice = choice
        self.dir = dir

        def pool_garden_spawner(choice, dir):
            #spawning random animals in backyard
            random_animal_word = ['donkey','pig, sheep', 'mule', 'cow', 'llama', 'rabbit', 'chicken']

            if dir == 'N' or dir == 'E' or dir == 'W':
                #build pool
                if choice == 'pool':
                    mc.setBlocks(self.x+length-1, self.y, self.z+15-width-3, self.x+length-14, self.y, self.z+15-width-10, 251)
                    mc.setBlocks(self.x+length-1, self.y-1, self.z+15-width-3, self.x+length-14, self.y-1, self.z+15-width-10, 251)
                    mc.setBlocks(self.x+length-2, self.y, self.z+15-width-4, self.x+length-13, self.y, self.z+15-width-9, 0)
                    mc.setBlocks(self.x+length-2, self.y, self.z+15-width-4, self.x+length-13, self.y, self.z+15-width-9, 9)
                    mc.setBlocks(self.x+length-2, self.y-1, self.z+15-width-4, self.x+length-13, self.y-1, self.z+15-width-9, 9)
                    mc.setBlocks(self.x+length-2, self.y-2, self.z+15-width-4, self.x+length-13, self.y-2, self.z+15-width-9, 251)
                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-4, self.x+length-18, self.y, self.z+15-width-4, 53, 1)

                    #right umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-5, self.x+length-18, self.y, self.z+15-width-5, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+15-width-5, self.x+length-18, self.y+1, self.z+15-width-5, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-5, self.x+length-18, self.y+2, self.z+15-width-5, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-6, self.x+length-18, self.y+2, self.z+15-width-6, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-4, self.x+length-18, self.y+2, self.z+15-width-4, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+2, self.z+15-width-5, self.x+length-17, self.y+2, self.z+15-width-5, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+2, self.z+15-width-5, self.x+length-19, self.y+2, self.z+15-width-5, 44,2)

                    #middle umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-8, self.x+length-18, self.y, self.z+15-width-8, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+15-width-8, self.x+length-18, self.y+1, self.z+15-width-8, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-8, self.x+length-18, self.y+2, self.z+15-width-8, 85)
                    mc.setBlocks(self.x+length-18, self.y+3, self.z+15-width-8, self.x+length-18, self.y+3, self.z+15-width-8, 44,2)

                    mc.setBlocks(self.x+length-18, self.y+3, self.z+15-width-9, self.x+length-18, self.y+3, self.z+15-width-9, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+3, self.z+15-width-7, self.x+length-18, self.y+3, self.z+15-width-7, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+3, self.z+15-width-8, self.x+length-17, self.y+3, self.z+15-width-8, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+3, self.z+15-width-8, self.x+length-19, self.y+3, self.z+15-width-8, 44,2)


                    #left umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-11, self.x+length-18, self.y, self.z+15-width-11, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+15-width-11, self.x+length-18, self.y+1, self.z+15-width-11, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-11, self.x+length-18, self.y+2, self.z+15-width-11, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-12, self.x+length-18, self.y+2, self.z+15-width-12, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+15-width-10, self.x+length-18, self.y+2, self.z+15-width-10, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+2, self.z+15-width-11, self.x+length-17, self.y+2, self.z+15-width-11, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+2, self.z+15-width-11, self.x+length-19, self.y+2, self.z+15-width-11, 44,2)


                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-7, self.x+length-18, self.y, self.z+15-width-7, 53, 1)
                    mc.setBlocks(self.x+length-18, self.y, self.z+15-width-10, self.x+length-18, self.y, self.z+15-width-10, 53, 1)

                    mc.setBlocks(self.x+length-17, self.y, self.z+15-width-4, self.x+length-17, self.y, self.z+15-width-4, 171)
                    mc.setBlocks(self.x+length-17, self.y, self.z+15-width-7, self.x+length-17, self.y, self.z+15-width-7, 171)
                    mc.setBlocks(self.x+length-17, self.y, self.z+15-width-10, self.x+length-17, self.y, self.z+15-width-10, 171)

                  
                elif choice == 'garden':
                    mc.setBlocks(self.x+21, self.y, self.z+15-width-2, self.x+5, self.y, self.z+15-width-2, 53, 3) #back
                    mc.setBlocks(self.x+21, self.y, self.z+15-width-2, self.x+21, self.y, self.z+15-width-7, 53, 1) #left
                    mc.setBlocks(self.x+5, self.y, self.z+15-width-2, self.x+5, self.y, self.z+15-width-6, 53, 0) #right
                    mc.setBlocks(self.x+20, self.y, self.z+15-width-7, self.x+5, self.y, self.z+15-width-7, 53, 2) #front

                    rand_flower = [0,1,2,3,4,5,6,7,8]
                    random_flower_choice = random.choice(rand_flower)

                    mc.setBlocks(self.x+20, self.y, self.z+15-width-3, self.x+6, self.y, self.z+15-width-6, 2) #grass
                    mc.setBlocks(self.x+20, self.y+1, self.z+15-width-3, self.x+6, self.y+1, self.z+15-width-6, 38, random_flower_choice) #flowers
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-2, self.x+2, self.y, self.z+15-width-2, 5) #wooden plank
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-3, self.x+2, self.y, self.z+15-width-3, 44, 10) #wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-4, self.x+2, self.y, self.z+15-width-4, 44, 10) #wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-5, self.x+2, self.y, self.z+15-width-5, 5) #wooden plank
                    mc.setBlocks(self.x+2, self.y+1, self.z+15-width-3, self.x+2, self.y+1, self.z+15-width-3, 140) #flower pot
                    mc.setBlocks(self.x+2, self.y+1, self.z+15-width-4, self.x+2, self.y+1, self.z+15-width-4, 140) #flower pot
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-8, self.x+2, self.y, self.z+15-width-8, 5) #second wooden plank
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-9, self.x+2, self.y, self.z+15-width-9, 44, 10) #second wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-10, self.x+2, self.y, self.z+15-width-10, 44, 10) #second wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+15-width-11, self.x+2, self.y, self.z+15-width-11, 5) #second wooden plank
                    mc.setBlocks(self.x+2, self.y+1, self.z+15-width-9, self.x+2, self.y+1, self.z+15-width-9, 140) #second flower pot
                    mc.setBlocks(self.x+2, self.y+1, self.z+15-width-10, self.x+2, self.y+1, self.z+15-width-10, 140) #second flower pot

                    def build_well(x_shift_num):
                        mc.setBlocks(self.x+10+x_shift_num, self.y, self.z+15-width-10, self.x+10+x_shift_num, self.y, self.z+15-width-10, 4) #left cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+15-width-11, self.x+9+x_shift_num, self.y, self.z+15-width-11, 4) #front cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+15-width-9, self.x+9+x_shift_num, self.y, self.z+15-width-9, 4) #back cobblestone piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y, self.z+15-width-10, self.x+8+x_shift_num, self.y, self.z+15-width-10, 4) #right cobblestone piece
                        mc.setBlocks(self.x+10+x_shift_num, self.y+1, self.z+15-width-10, self.x+10+x_shift_num, self.y+2, self.z+15-width-10, 85) #left cobblestone piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y+1, self.z+15-width-10, self.x+8+x_shift_num, self.y+2, self.z+15-width-10, 85) #right cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+15-width-10, self.x+9+x_shift_num, self.y+3, self.z+15-width-10, 44,2) #middle slab piece
                        mc.setBlocks(self.x+10+x_shift_num, self.y+3, self.z+15-width-10, self.x+10+x_shift_num, self.y+3, self.z+15-width-10, 44,2) #left upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+15-width-11, self.x+9+x_shift_num, self.y+3, self.z+15-width-11, 44,2) #front upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+15-width-9, self.x+9+x_shift_num, self.y+3, self.z+15-width-9, 44,2) #back upperslab piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y+3, self.z+15-width-10, self.x+8+x_shift_num, self.y+3, self.z+15-width-10, 44,2) #right upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y-1, self.z+15-width-10, self.x+9+x_shift_num, self.y-1, self.z+15-width-10, 4) #cobblestone under water
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+15-width-10, self.x+9+x_shift_num, self.y, self.z+15-width-10, 9) #water for well
                    build_well(0)
                    build_well(7)
            elif dir == 'S':
                #South Backyard
                if choice == 'pool':
                    mc.setBlocks(self.x+length-1, self.y, self.z+width+3, self.x+length-14, self.y, self.z+width+10, 251)
                    mc.setBlocks(self.x+length-1, self.y-1, self.z+width+3, self.x+length-14, self.y-1, self.z+width+10, 251)
                    mc.setBlocks(self.x+length-2, self.y, self.z+width+4, self.x+length-13, self.y, self.z+width+9, 0)
                    mc.setBlocks(self.x+length-2, self.y, self.z+width+4, self.x+length-13, self.y, self.z+width+9, 9)
                    mc.setBlocks(self.x+length-2, self.y-1, self.z+width+4, self.x+length-13, self.y-1, self.z+width+9, 9)
                    mc.setBlocks(self.x+length-2, self.y-2, self.z+width+4, self.x+length-13, self.y-2, self.z+width+9, 251)
                    mc.setBlocks(self.x+length-18, self.y, self.z+width+4, self.x+length-18, self.y, self.z+width+4, 53, 1)

                    #right umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+width+5, self.x+length-18, self.y, self.z+width+5, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+width+5, self.x+length-18, self.y+1, self.z+width+5, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+5, self.x+length-18, self.y+2, self.z+width+5, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+6, self.x+length-18, self.y+2, self.z+width+6, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+4, self.x+length-18, self.y+2, self.z+width+4, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+2, self.z+width+5, self.x+length-17, self.y+2, self.z+width+5, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+2, self.z+width+5, self.x+length-19, self.y+2, self.z+width+5, 44,2)

                    #middle umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+width+8, self.x+length-18, self.y, self.z+width+8, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+width+8, self.x+length-18, self.y+1, self.z+width+8, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+8, self.x+length-18, self.y+2, self.z+width+8, 85)
                    mc.setBlocks(self.x+length-18, self.y+3, self.z+width+8, self.x+length-18, self.y+3, self.z+width+8, 44,2)

                    mc.setBlocks(self.x+length-18, self.y+3, self.z+width+9, self.x+length-18, self.y+3, self.z+width+9, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+3, self.z+width+7, self.x+length-18, self.y+3, self.z+width+7, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+3, self.z+width+8, self.x+length-17, self.y+3, self.z+width+8, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+3, self.z+width+8, self.x+length-19, self.y+3, self.z+width+8, 44,2)


                    #left umbrellas
                    mc.setBlocks(self.x+length-18, self.y, self.z+width+11, self.x+length-18, self.y, self.z+width+11, 85)
                    mc.setBlocks(self.x+length-18, self.y+1, self.z+width+11, self.x+length-18, self.y+1, self.z+width+11, 85)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+11, self.x+length-18, self.y+2, self.z+width+11, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+12, self.x+length-18, self.y+2, self.z+width+12, 44,2)
                    mc.setBlocks(self.x+length-18, self.y+2, self.z+width+10, self.x+length-18, self.y+2, self.z+width+10, 44,2)
                    mc.setBlocks(self.x+length-17, self.y+2, self.z+width+11, self.x+length-17, self.y+2, self.z+width+11, 44,2)
                    mc.setBlocks(self.x+length-19, self.y+2, self.z+width+11, self.x+length-19, self.y+2, self.z+width+11, 44,2)


                    mc.setBlocks(self.x+length-18, self.y, self.z+width+7, self.x+length-18, self.y, self.z+width+7, 53, 1)
                    mc.setBlocks(self.x+length-18, self.y, self.z+width+10, self.x+length-18, self.y, self.z+width+10, 53, 1)

                    mc.setBlocks(self.x+length-17, self.y, self.z+width+4, self.x+length-17, self.y, self.z+width+4, 171)
                    mc.setBlocks(self.x+length-17, self.y, self.z+width+7, self.x+length-17, self.y, self.z+width+7, 171)
                    mc.setBlocks(self.x+length-17, self.y, self.z+width+10, self.x+length-17, self.y, self.z+width+10, 171)

                elif choice == 'garden':
                    mc.setBlocks(self.x+21, self.y, self.z+width+2, self.x+5, self.y, self.z+width+2, 53, 2) #back
                    mc.setBlocks(self.x+21, self.y, self.z+width+2, self.x+21, self.y, self.z+width+7, 53, 1) #left
                    mc.setBlocks(self.x+5, self.y, self.z+width+2, self.x+5, self.y, self.z+width+7, 53, 0) #right
                    mc.setBlocks(self.x+20, self.y, self.z+width+7, self.x+5, self.y, self.z+width+7, 53, 3) #front

                    rand_flower = [0,1,2,3,4,5,6,7,8]
                    random_flower_choice = random.choice(rand_flower)

                    mc.setBlocks(self.x+20, self.y, self.z+width+3, self.x+6, self.y, self.z+width+6, 2) #grass
                    mc.setBlocks(self.x+20, self.y+1, self.z+width+3, self.x+6, self.y+1, self.z+width+6, 38, random_flower_choice) #flowers
                    mc.setBlocks(self.x+2, self.y, self.z+width+2, self.x+2, self.y, self.z+width+2, 5) #wooden plank
                    mc.setBlocks(self.x+2, self.y, self.z+width+3, self.x+2, self.y, self.z+width+3, 44, 10) #wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+width+4, self.x+2, self.y, self.z+width+4, 44, 10) #wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+width+5, self.x+2, self.y, self.z+width+5, 5) #wooden plank
                    mc.setBlocks(self.x+2, self.y+1, self.z+width+3, self.x+2, self.y+1, self.z+width+3, 140) #flower pot
                    mc.setBlocks(self.x+2, self.y+1, self.z+width+4, self.x+2, self.y+1, self.z+width+4, 140) #flower pot
                    mc.setBlocks(self.x+2, self.y, self.z+width+8, self.x+2, self.y, self.z+width+8, 5) #second wooden plank
                    mc.setBlocks(self.x+2, self.y, self.z+width+9, self.x+2, self.y, self.z+width+9, 44, 10) #second wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+width+10, self.x+2, self.y, self.z+width+10, 44, 10) #second wooden slab
                    mc.setBlocks(self.x+2, self.y, self.z+width+11, self.x+2, self.y, self.z+width+11, 5) #second wooden plank
                    mc.setBlocks(self.x+2, self.y+1, self.z+width+9, self.x+2, self.y+1, self.z+width+9, 140) #second flower pot
                    mc.setBlocks(self.x+2, self.y+1, self.z+width+10, self.x+2, self.y+1, self.z+width+10, 140) #second flower pot

                    def build_well(x_shift_num):
                        mc.setBlocks(self.x+10+x_shift_num, self.y, self.z+width+10, self.x+10+x_shift_num, self.y, self.z+width+10, 4) #left cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+width+11, self.x+9+x_shift_num, self.y, self.z+width+11, 4) #front cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+width+9, self.x+9+x_shift_num, self.y, self.z+width+9, 4) #back cobblestone piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y, self.z+width+10, self.x+8+x_shift_num, self.y, self.z+width+10, 4) #right cobblestone piece
                        mc.setBlocks(self.x+10+x_shift_num, self.y+1, self.z+width+10, self.x+10+x_shift_num, self.y+2, self.z+width+10, 85) #left cobblestone piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y+1, self.z+width+10, self.x+8+x_shift_num, self.y+2, self.z+width+10, 85) #right cobblestone piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+width+10, self.x+9+x_shift_num, self.y+3, self.z+width+10, 44,2) #middle slab piece
                        mc.setBlocks(self.x+10+x_shift_num, self.y+3, self.z+width+10, self.x+10+x_shift_num, self.y+3, self.z+width+10, 44,2) #left upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+width+11, self.x+9+x_shift_num, self.y+3, self.z+width+11, 44,2) #front upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y+3, self.z+width+9, self.x+9+x_shift_num, self.y+3, self.z+width+9, 44,2) #back upperslab piece
                        mc.setBlocks(self.x+8+x_shift_num, self.y+3, self.z+width+10, self.x+8+x_shift_num, self.y+3, self.z+width+10, 44,2) #right upperslab piece
                        mc.setBlocks(self.x+9+x_shift_num, self.y-1, self.z+width+10, self.x+9+x_shift_num, self.y-1, self.z+width+10, 4) #cobblestone under water
                        mc.setBlocks(self.x+9+x_shift_num, self.y, self.z+width+10, self.x+9+x_shift_num, self.y, self.z+width+10, 9) #water for well
                    build_well(0)
                    build_well(7)


        if self.dir == 'S':
            #terraforming house plot
            terraform = Terraform(self.x-5, self.y, self.z-6, self.x+length+5, self.z+width+16)
            terraform.terraform_land()

            #fencing around house
            fence_ids = [85, 113, 188, 189, 190, 191, 192]
            random_fence = random.choice(fence_ids)
            mc.setBlocks(self.x+length+2, self.y, self.z-3, self.x-2, self.y, self.z-3, random_fence)
            mc.setBlocks(self.x-2, self.y, self.z-2, self.x-2, self.y, self.z+width+13, random_fence)
            mc.setBlocks(self.x+length+2, self.y, self.z-2, self.x+length+2, self.y, self.z+width+13, random_fence)
            mc.setBlocks(self.x+length+2, self.y, self.z+width+13, self.x-2, self.y, self.z+width+13, random_fence)
            #fence opening
            mc.setBlocks(self.x+(length/2)-1, self.y, self.z-3, self.x+(length/2)+1, self.y, self.z-3,0)
            #setting blocks around fencing to make them connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-3-1, self.x-2-1, self.y, self.z-3-1, 1)
            mc.setBlocks(self.x-2-1, self.y, self.z-2-1, self.x-2-1, self.y, self.z+width+13+1, 1)
            mc.setBlocks(self.x+length+2+1, self.y, self.z-2-1, self.x+length+2+1, self.y, self.z+width+13+1, 1)
            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+13+1, self.x-2-1, self.y, self.z+width+13+1, 1)
            #removed the blocks after fences connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-3-1, self.x-2-1, self.y, self.z-3-1, 0)
            mc.setBlocks(self.x-2-1, self.y, self.z-2-1, self.x-2-1, self.y, self.z+width+13+1, 0)
            mc.setBlocks(self.x+length+2+1, self.y, self.z-2-1, self.x+length+2+1, self.y, self.z+width+13+1, 0)
            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+13+1, self.x-2-1, self.y, self.z+width+13+1, 0)
            #build pool or garden
            pool_garden_spawner(choice, 'S')

            

        elif self.dir == 'N':
            #terraforming house plot
            terraform = Terraform(self.x-5, self.y, self.z-width-3, self.x+length+8, self.z+width+8)
            terraform.terraform_land()

            #fencing around house
            fence_ids = [85, 113, 188, 189, 190, 191, 192]
            random_fence = random.choice(fence_ids)
            mc.setBlocks(self.x+length+2, self.y, self.z-width, self.x-2, self.y, self.z-width, random_fence) #back house

            mc.setBlocks(self.x-2, self.y, self.z+width+5, self.x-2, self.y, self.z-width, random_fence) #left house

            mc.setBlocks(self.x+length+2, self.y, self.z+width+5, self.x+length+2, self.y, self.z-width, random_fence) #right house

            mc.setBlocks(self.x+length+3, self.y, self.z+width+5, self.x-2, self.y, self.z+width+5, random_fence) #front house

            #fence opening
            mc.setBlocks(self.x+(length/2)-1, self.y, self.z+width+5, self.x+(length/2)+1, self.y, self.z+width+5,0)

            #setting blocks around fencing to make them connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-width-1, self.x-2-1, self.y, self.z-width-1, 1) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z-width-1, 1) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y, self.z-width-1, 1) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z+width+5+1, 1) #front house


            #removed the blocks after fences connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-width-1, self.x-2-1, self.y+10, self.z-width-1, 0) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z-width-1, 0) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y+10, self.z-width-1, 0) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z+width+5+1, 0) #front house

            #build pool or garden
            pool_garden_spawner(choice, 'N')

           
        elif self.dir == 'E':
            #terraforming house plot
            terraform = Terraform(self.x-5, self.y, self.z-width-3, self.x+length+8, self.z+width+8)
            terraform.terraform_land()
            #fencing around house
            fence_ids = [85, 113, 188, 189, 190, 191, 192]
            random_fence = random.choice(fence_ids)
            mc.setBlocks(self.x+length+3, self.y, self.z-width, self.x-2, self.y, self.z-width, random_fence) #back house

            mc.setBlocks(self.x-2, self.y, self.z+width+5, self.x-2, self.y, self.z-width, random_fence) #left house

            mc.setBlocks(self.x+length+2, self.y, self.z+width+5, self.x+length+2, self.y, self.z-width, random_fence) #right house

            mc.setBlocks(self.x+length+3, self.y, self.z+width+5, self.x-2, self.y, self.z+width+5, random_fence) #front house


            #setting blocks around fencing to make them connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-width-1, self.x-2-1, self.y, self.z-width-1, 1) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z-width-1, 1) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y, self.z-width-1, 1) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z+width+5+1, 1) #front house


            #removed the blocks after fences connect
            mc.setBlocks(self.x+length+2+1, self.y, self.z-width-1, self.x-2-1, self.y+10, self.z-width-1, 0) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z-width-1, 0) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y+10, self.z-width-1, 0) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z+width+5+1, 0) #front house

            #build pool or garden
            pool_garden_spawner(choice, 'E')

        elif self.dir == 'W':
            #terraforming house plot
            terraform = Terraform(self.x-5, self.y, self.z-width-4, self.x+length+8, self.z+width+8)
            terraform.terraform_land()
            #fencing around house
            fence_ids = [85, 113, 188, 189, 190, 191, 192]
            random_fence = random.choice(fence_ids)
            mc.setBlocks(self.x+length+2, self.y, self.z-width-1, self.x-2-1, self.y, self.z-width-1, random_fence) #back house

            mc.setBlocks(self.x-2, self.y, self.z+width+5, self.x-2, self.y, self.z-width, random_fence) #left house

            mc.setBlocks(self.x+length+2, self.y, self.z+width+5, self.x+length+2, self.y, self.z-width, random_fence) #right house

            mc.setBlocks(self.x+length+3, self.y, self.z+width+5, self.x-2, self.y, self.z+width+5, random_fence) #front house


            #setting blocks around fencing to make them connect
            mc.setBlocks(self.x+length+2, self.y, self.z-width-2, self.x-2-1, self.y, self.z-width-2, 1) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z-width-1, 1) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y, self.z-width-1, 1) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y, self.z+width+5+1, 1) #front house


            #removed the blocks after fences connect
            mc.setBlocks(self.x+length+2, self.y, self.z-width-2, self.x-2-1, self.y+10, self.z-width-2, 0) #back house

            mc.setBlocks(self.x-2-1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z-width-1, 0) #left house

            mc.setBlocks(self.x+length+2+1, self.y, self.z+width+5+1, self.x+length+2+1, self.y+10, self.z-width-1, 0) #right house

            mc.setBlocks(self.x+length+5+1, self.y, self.z+width+5+1, self.x-2-1, self.y+10, self.z+width+5+1, 0) #front house

            #build pool or garden
            pool_garden_spawner(choice, 'W')

            
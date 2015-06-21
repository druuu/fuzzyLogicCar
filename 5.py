import pygame, random, roboCar
import time
from pygame.locals import *
import math
import random

class Maze:
    def __init__(self, mazeLayer=0, solveLayer=0):
        self.mLayer = mazeLayer # surface
        self.sLayer = solveLayer# surface
        self.sLayer.fill((0, 0, 0, 0))
        self.walls = []
        self.totalCells = height*width # 80 * 60
        self.compass = [(-1,0),(0,1),(1,0),(0,-1),(0,0)]
        self.gridWalls(grid)
        self.drawMaze(self.walls,self.mLayer)

    def gridWalls(self, grid):
        xGrid = len(grid[0])
        yGrid = len(grid)
        for i in xrange(yGrid):
            for j in xrange(xGrid):
                if grid[i][j] == 1:
                    self.walls.append((xGrid * i) + j)
        #self.walls = [4,13,19,20,22,24,25,26,27,28,29,31,33,34,37,52,55,57,58,60,65,67,68,70,78,83,91,93,94,96,97,98,99,100,101,103,104,106,109,124,127,128,130,132,133,134,135,136,137,139,141,142,148,157]
        
        

    def update(self):
        pass

    def drawMaze(self,walls,mLayer):
        for wall in walls:
            dx = (wall%coord)*cell
            dy = (wall/coord)*cell
            pygame.draw.line(mLayer, (0,0,0,255),(dx,dy+1),(dx,dy+cell-1))
            pygame.draw.line(mLayer, (0,0,0,255),(dx+1,dy+cell),(dx+cell-1,dy+cell))
            pygame.draw.line(mLayer, (0,0,0,255),(dx+cell,dy+1),(dx+cell,dy+cell-1))
            pygame.draw.line(mLayer, (0,0,0,255),(dx+1,dy),(dx+cell-1,dy))


    def roboPos(self):
        listRoboCoord = []
        listRoboOrient = []
        #grid = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0]]
    	init = [0, 0]
    	goal = [len(grid)-1, len(grid[0])-1]
        #goal = [4,1 ]
    	steering_noise    = 0.1
    	distance_noise    = 0.03
    	measurement_noise = 0.3

    	#### ADJUST THESE PARAMETERS ######

    	weight_data       = 0.1
    	weight_smooth     = 0.2
    	p_gain            = 2.0
    	d_gain            = 6.0

    	result, listRoboPos = roboCar.main(grid, init, goal, steering_noise, distance_noise, measurement_noise,
                weight_data, weight_smooth, p_gain, d_gain)

        k = 0
        for i in listRoboPos:
            listRoboCoord.append(((i[0] * 40) + 20, (i[1] * 40) + 20 ))
            listRoboOrient.append(i[2])
            k += 1
            
        return listRoboCoord, listRoboOrient


    def solve(self) :
        return self.roboPos()



    def draw(self, screen):
        screen.blit(self.sLayer, (0,0))
        screen.blit(self.mLayer, (0,0))
    def resetSlayer(self):
        self.sLayer.fill((0, 0, 0, 0))

def main():  
    """Maze Main Function - Luke Arntson, Jan '09
        Written using - http://www.mazeworks.com/mazegen/mazetut/index.htm
    """
    pygame.init()
    screen = pygame.display.set_mode((240, 200))
    pygame.display.set_caption("druuu's game")
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    mazeLayer = pygame.Surface(screen.get_size())
    mazeLayer = mazeLayer.convert_alpha()
    mazeLayer.fill((0, 0, 0, 0))
    solveLayer = pygame.Surface(screen.get_size())
    solveLayer = solveLayer.convert_alpha()
    solveLayer.fill((0, 0, 0, 0))
    newMaze = Maze(mazeLayer,solveLayer)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    t = 0 

    def roboMov(roboPosCoord, roboPosOrient):
        roboPosOrientA = []
        for radian in roboPosOrient:
            roboPosOrientA.append(radian * 57.295)
        roboPosOrient = roboPosOrientA

        for index in xrange(len(roboPosCoord)):
            xCoord = roboPosCoord[index][0] - 5
            yCoord = roboPosCoord[index][1] - 5
            dot1 = pygame.image.load("car1.png").convert()
            solveLayer.fill((255,255,255))
            dot1.set_colorkey((255, 0, 0))
            time.sleep(0.1)
            rotateLayer = pygame.transform.rotate(dot1, roboPosOrient[index])
            solveLayer.blit(rotateLayer, Rect(xCoord, yCoord, 0, 0))
            solveLayer.blit(rotateLayer, Rect(xCoord, yCoord, 0, 0))
            newMaze.draw(screen)
            pygame.display.flip()

    while 1:
        clock.tick(5)
#         if sp == 50 :
#             t =2 
        t += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
        screen.blit(background, (0, 0))
        newMaze.draw(screen)
        pygame.display.flip()
        roboPosCoord, roboPosOrient = newMaze.solve()
        roboMov(roboPosCoord, roboPosOrient)
        #newMaze.resetSlayer()
if __name__ == '__main__': main()

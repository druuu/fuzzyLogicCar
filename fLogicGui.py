import pygame, random, time
import math
from pygame.locals import *
import fuzzyLogic

roadList = []
xCar = 30
yCar = 30
angle = 45
senseList = []
            
draw_on = False
last_pos = (0, 0)
color = (0, 0, 0)
radius = 5 
run = 1
p = q =  0
angleOld = 45

def eucDist(coord1, coord2):
    x1 = float(coord1[0])
    y1 = float(coord1[1])
    x2 = float(coord2[0])
    y2 = float(coord2[1])
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

def compDist(roadListLeft, roadListRight, center, angle):
    rL = 0
    rR = 0
    roadCenterList = []
    l1 = len(roadListLeft)
    l2 = len(roadListRight)
    n = 0
    n1 = 0
    index = 0
    index = 1
    if l1 < l2 and l1 > 0:
        nFact = int(l2 / l1)
        for rL in xrange(l1):
            n = 0
            while n < nFact:
                xM1, yM1 = roadListLeft[rL]
                index = (rL * nFact) + n
                xM2, yM2 = roadListRight[index]
                n += 1
                m1,m2 = ((xM1 + xM2) / 2 , (yM1 + yM2) / 2)
                m1 = math.ceil(m1)
                m2 = math.ceil(m2)
                roadCenterList.append((m1,m2))
    else:
        if l2 > 0:
            nFact = int(l1 / l2)
            for rR in xrange(l2):
                n1 = 0
                while n1 < nFact:
                    xM1, yM1 = roadListRight[rR]
                    index1 = (rR * nFact) + n1
                    xM2, yM2 = roadListLeft[index1]
                    n1 += 1
                    m1,m2 = ((xM1 + xM2) / 2 , (yM1 + yM2) / 2)
                    roadCenterList.append((m1,m2))
    global p,q
    global angleOld
    val = 0
    angle = (angle + 90) * 0.0174532925
    m = math.tan(angle)
    x1, y1 = center
    x1 = int(math.ceil(x1))
    y1 = int(math.ceil(y1))
    for x, y in roadCenterList:
        if int(x - x1) == int(m * (y - y1)):
            #print int(m * (x - x1)),"m is"
            senseList.append((x,y))

    #print senseList

    for coord in senseList:
        m1 = -m
        if (int(coord[0] - center[0]) - int(m1 * (coord[1] - center[1]))) < 0:
            val = -eucDist(coord, center)
        else:
            val = eucDist(coord, center)


    return val

def getCarCoord():
    global i, j
    i += 0.5
    j = i
    left = (63, 45.371679553) 
    right = (45.371679553, 63)
    x = left[0] + i, left[1] + j
    y = right[0] + i, right[1] + j

    return x, y
        
def carMove(rotateLayer, xCar, yCar):
    solveLayer.blit(rotateLayer, (xCar, yCar))
    #pygame.display.flip()


screen = pygame.display.set_mode((600,700))
screen.fill((255,255,255))
solveLayer = pygame.Surface(screen.get_size())
solveLayer = solveLayer.convert_alpha()
carLayer = pygame.Surface(screen.get_size())
carLayer = carLayer.convert_alpha()
solveLayer.fill((255,0,0))
carLayer.fill((255,255,255))

carImage = pygame.image.load("car.png").convert()
carImage.set_colorkey((255, 0, 0))
pos = 0
posDetermine = 0
roadListLeft = []
roadListRight = []
count = 0
center = (30.70710, 30.707106)
isNeg = 0
draw = 0
fullRoadList = []

while run == 1:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        run = 0
    if e.type == pygame.MOUSEBUTTONDOWN:
        draw_on = True
    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False
    if e.type == pygame.MOUSEMOTION:
        if draw_on:
            pygame.draw.circle(carLayer, color, e.pos, radius)
            roundline(carLayer, color, e.pos, last_pos,  radius)
            xCarEpos = math.ceil(xCar)
            yCarEpos = math.ceil(yCar)
            angleEpos = angle *  0.0174532925
            mSlope = math.tan(angleEpos)
            fullRoadList.append(e.pos)
            uptoPoint1 = math.ceil(xCarEpos + (50 * math.sin(mSlope)))
            uptoPoint2 = math.ceil(yCarEpos + (50 * math.cos(mSlope)))
            uptoPoint = (uptoPoint1, uptoPoint2)
            #print uptoPoint

            #print mSlope, yCarEpos, xCarEpos, xEpos, yEpos, posDetermine
            #time.sleep(0.3)
            #print posDetermine,"pd"
            for xEpos, yEpos in fullRoadList:
                posDetermine = (xEpos - xCarEpos) - (mSlope * (yEpos - yCarEpos))
                lenDetermine = (xEpos - uptoPoint[0]) - ((-mSlope) * (yEpos - uptoPoint[1]))
                #print lenDetermine
                if posDetermine < 0:
                    if lenDetermine > 0:
                        roadListRight.append(e.pos)
                        
                else:
                    if lenDetermine > 0:
                        roadListLeft.append(e.pos)
        last_pos = e.pos

    solveLayer.blit(carLayer, (0,0))
        
    rotateLayer = pygame.transform.rotate(carImage, angle)
    carMove(rotateLayer, xCar, yCar)
    if count >= 200:
        angleRad = angle * 0.0174532925
        yCar = yCar + math.cos(angleRad)
        xCar = xCar + math.sin(angleRad)
        center = (xCar, yCar)
    count += 1
    val = compDist(roadListLeft, roadListRight, center, angle)
    senseList = []
    val = int(val/3)
    #if val > 160:
        #val = 159
    if val < 0:
        isNeg = 1
        val = -val
    else:
        isNeg = 0
    fuzzyLogic.fl.fuzzy(val)
    if not val == 0:
        if isNeg == 1:
            #print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            angle = angleOld - fuzzyLogic.fl.deFuzzy()
            #print angle
            #time.sleep(3)
        else:
            angle = angleOld + fuzzyLogic.fl.deFuzzy()
            #print angle 
            #time.sleep(3)

        angleOld = angle
    else:
        angle = angleOld
        #if not angle == 45:
            #print '^^^^^^^^^^^^^^^^^^^^',angle
    isNeg = 0
    #print val, angleOld, '((((((((((((((((((('
    #print "val:", val, "angle:", angle
    if val > 0:
        time.sleep(0.5)
    screen.blit(solveLayer, (0, 0))
    pygame.display.flip()

pygame.quit()

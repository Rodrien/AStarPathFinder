import pygame as py
import math

W_SIZE = 600
CANTIDAD = 30 
WIDTH = int(W_SIZE/CANTIDAD)

#-------------------- colors --------------------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,45,0)
BLUE = (0,120,255)
GREEN = (108,255,0)
PURPLE = (89,0,255)
#------------------------------------------------

class node:
    def __init__(self,a,b):
        self.position = (a,b)
        self.x = a * WIDTH
        self.y = b * WIDTH
        self.color = WHITE
        self.gcost = 0
        self.hcost = 0 #distance from end node
        self.fcost = 0 #g+h
        self.father = None 

    def draw(self,screen):
        nodeRect = py.Rect(self.x,self.y,WIDTH,WIDTH)
        py.draw.rect(screen,self.color,nodeRect)
    
    def clicked(self,position):
        (a,b) = position
        if self.x <= a and a < self.x + WIDTH:
             if self.y <= b and b < self.y + WIDTH:
                 return True
        return False

def drawLines(screen):
    for i in range(CANTIDAD+1):
        py.draw.line(screen,BLACK,(i*WIDTH,0),(i*WIDTH,W_SIZE))
    for j in range(CANTIDAD+1):
        py.draw.line(screen,BLACK,(0,j*WIDTH),(W_SIZE,j*WIDTH))

def startNodes():
    squares = [[node(x,y) for x in range(CANTIDAD)] for y in range(CANTIDAD)]
    for x in range(CANTIDAD):
        for y in range(CANTIDAD):
            if squares[x][y].position[0] == 0:
                squares[x][y].color = BLACK
            if squares[x][y].position[0] == CANTIDAD-1:
                squares[x][y].color = BLACK
            elif squares[x][y].position[1] == 0:
                squares[x][y].color = BLACK
            elif squares[x][y].position[1] == CANTIDAD-1:
                squares[x][y].color = BLACK
    return squares 

def restart():
    squares = startNodes()
    return squares

def drawNodes(screen,list,lines):
    for x in range(CANTIDAD):
        for y in range(CANTIDAD):
            list[x][y].draw(screen)
    if lines:
        drawLines(screen)

def changeNodes(list,position,key,screen): #key = 1 or 2 and is used to set the starting and finishing nodes
    for x in range(CANTIDAD):
        for y in range(CANTIDAD):
            n = list[x][y]
            if n.clicked(position) and n.color == WHITE:
                if key == 1:
                    n.color = GREEN
                #key = key + 1
                elif key == 2:
                    n.color = BLUE
                #key = key + 1
                else: 
                    n.color = BLACK
            n.draw(screen)

#A* specific functions

def paint(list,path):
    for c in path:
        list[c[0]][c[1]].color = PURPLE

#if A B have same coordinates return true
def equals(self,B):
    x=self.position[0]
    y=self.position[1]
    x2=B.position[0]
    y2=B.position[1]
    return x == x2 and y == y2

def closer(self,B):
    return self.fcost < B.fcost

def fCost(self):
    return self.gcost + self.hcost

def distance(self,B):
    x=self.position[0]
    y=self.position[1]
    x2=B.position[0]
    y2=B.position[1]
    return abs((x-x2))+abs((y-y2))
        
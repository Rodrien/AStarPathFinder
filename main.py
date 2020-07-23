import pygame as py
import Nodes as N
from Nodes import *

def solve(squares):
    open_nodes = []
    closed_nodes = []

    grid = [[0 for x in range(CANTIDAD)] for y in range(CANTIDAD)] 

    for x in range(CANTIDAD):
        for y in range(CANTIDAD):   
            s = squares[x][y]
            if s.color == GREEN: #open starting node
                grid[x][y] = 'A'
                start = N.node(x,y)
                open_nodes.append(start) #open start
            elif s.color == BLUE: #set end node
                grid[x][y] = 'B'
                finish = N.node(x,y)
            elif s.color == BLACK:
                grid[x][y] = 'X'

    path = finder(grid,open_nodes,closed_nodes,start,finish)
    return path

def finder(grid,open_nodes,closed_nodes,start,finish):
    while(open_nodes != []):
        sorted(open_nodes) #sort nodes so first is the closest one
        
        current = open_nodes.pop(0)        
        closed_nodes.append(current)
        (x,y) = current.position
        
        if(equals(current,finish)):    
            path = []
            while current != start:
                path.append(current.position)
                current = current.father
            path.append(start.position)
            return path[::-1] #path reversed
        else: #current != finish
            (x,y) = current.position
            neighbors = [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]#,(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
            for i in neighbors:
                (a,b) = i #neighbors coordinates
                if grid[a][b] == 'X': 
                    continue
                son = N.node(a,b)
                son.father = current
                door = True
                for c in closed_nodes:
                    if equals(son,c):
                        door = False
                if door:
                    son.hcost = distance(son,finish)
                    son.gcost = distance(son,start)
                    son.fcost = son.hcost + son.gcost
                    if(addToOpen(open_nodes,son)):
                        for f in open_nodes:
                            if equals(f,son):
                                open_nodes.remove(f)
                        open_nodes.append(son)
    return []

def addToOpen(open_nodes, son):
    for node in open_nodes:
        if (equals(son,node) and son.fcost == node.fcost):
            return False
    return True

#remove current from open_nodes
def remove(current,open_nodes):
    for x in open_nodes:
        if(equals(x,current)):
            open_nodes.remove(x)

def sorted(open_nodes): #returns open nodes sorted with sorted value
    low = open_nodes[0]
    for i in open_nodes:
        if (i.fcost < low.fcost):
            low = i
        elif (i.fcost == low.fcost): #if fcost equal keep the one with the lowest gcost
            if (i.gcost < low.gcost):
                low = i

    open_nodes.remove(low)
    open_nodes.insert(0,low)

#load logo and set window name and background
#logo = py.image.load("./Icons/snake64.png")
#py.display.set_icon(logo)
py.display.set_caption("Nodes")
screen = py.display.set_mode((W_SIZE+1,W_SIZE+1))

#start nodes
squares = startNodes()

#shortest path
path = []

key = 1
click = False
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:
                path = solve(squares)
                paint(squares,path)
            if event.key == py.K_BACKSPACE: #fix
                restart(squares)
                print("in")
        if event.type == py.MOUSEBUTTONDOWN:
            #get mouse location 
            click = True
            while click: #works but must re think, bugs with key
                position = py.mouse.get_pos()
                changeNodes(squares,position,key,screen)
                #drawLines(screen)
                py.display.update()
                for event2 in py.event.get():
                    if event2.type == py.MOUSEBUTTONUP:
                        click = False
            key = key + 1

    drawNodes(screen,squares)
    #drawLines(screen)
    py.display.update()


from Nodes import *
import Nodes as n

lenY = 50
lenX = 50

def main():
    grid = [[n.node(x,y) for x in range(lenX)] for y in range(lenY)] 
    
    start = n.node(1,1)
    grid[1][1].type = 'A' 

    finish = n.node(7,8)
    grid[7][8].type = 'B' 
    
    grid[5][5].type ='X' #placed a wall #place walls all around the grid 
    grid[6][5].type ='X' #placed a wall 
    grid[5][5].type ='X'
    grid[5][4].type ='X'
    grid[5][3].type ='X'
    grid[5][2].type ='X'

    for i in {0,lenX-1}:
        for j in range(lenX):
            grid[i][j].type = 'X'
    for i in [0,lenX-1]:
        for j in range(lenX):
            grid[j][i].type = 'X'

    open_nodes = []
    closed_nodes = []
    open_nodes.append(start) #open starting node

    path = finder(grid,open_nodes,closed_nodes,start,finish) #shortest path will be stored here

    showPath(grid,path)
    drawGrid(grid)

    

def finder(grid,open_nodes,closed_nodes,start,finish):
    while(open_nodes != []):
        lowest(open_nodes) #sort nodes so first is the closest one
        
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
            neighbors = [(x-1, y,10), (x+1, y,10), (x, y-1,10), (x, y+1,10),(x+1,y+1,14),(x-1,y-1,14),(x+1,y-1,14),(x-1,y+1,14)] #(x+1,y+1,14),(x-1,y-1,14),(x+1,y-1,14),(x-1,y+1,14)
            for i in neighbors:
                (a,b,z) = i #neighbors coordinates
                if grid[a][b].type == 'X': 
                    continue
                son = n.node(a,b)
                son.father = current
                door = True
                for c in closed_nodes:
                    if equals(son,c):
                        door = False
                if door:
                    son.hcost = distance(son,finish)
                    son.gcost = distance(son,start) #+ float(z)
                    print(float(z))
                    son.fcost = son.hcost + son.gcost
                    if(addToOpen(open_nodes,son)):
                        for f in open_nodes:
                            if equals(f,son):
                                open_nodes.remove(f)
                        open_nodes.append(son)
    return []

def showPath(grid,path):
    for p in path:
        print(p)
        x = p[0]
        y = p[1]
        if (grid[x][y].type != 'A' and grid[x][y].type != 'B'):
            grid[x][y].type = '*'

def addToOpen(open_nodes, son):
    for node in open_nodes:
        if (equals(son,node) and son.fcost >= node.fcost):
            return False
    return True

#remove current from open_nodes
def remove(current,open_nodes):
    for x in open_nodes:
        if(equals(x,current)):
            open_nodes.remove(x)

def lowest(open_nodes): #returns open nodes sorted with lowest value
    low = open_nodes[0]
    for i in open_nodes:
        if (i.fcost < low.fcost):
            low = i
    open_nodes.remove(low)
    open_nodes.insert(0,low)
    
def drawGrid(grid):
    for x in range(lenX):
        for y in range(lenY):
            print(grid[y][x].type,end = "")
        print("")

main()
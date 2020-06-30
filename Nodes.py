import math

class node:
    def __init__(self,x,y):
        self.position = (x,y)
        self.type = 0 #type A,B,X if wall or Z if part of path
        self.gcost = 0
        self.hcost = 0 #distance from end node
        self.fcost = 0 #g+h
        self.father = None 

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
        
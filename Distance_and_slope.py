# Python program to accept coordinates as a pair of tuples and return the slope and distance of the line.

import math

class Line():
    def __init__(self,coor1,coor2):
        self.coor11=coor1[0]
        self.coor12=coor1[1]
        self.coor21=coor2[0]
        self.coor22=coor2[1]
        
    def distance(self):
        return math.sqrt(((self.coor21 - self.coor11)**2) + ((self.coor22 - self.coor12)**2))
        
    def slope(self):
        return ((self.coor22 - self.coor12)/(self.coor21 - self.coor11))

coordinate1 =(3,2)
coordinate2 =(8,10)
li=Line(coordinate1,coordinate2)

li.distance()  # 9.433981132056603

li.slope()  # 1.6

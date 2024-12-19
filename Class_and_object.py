# Python program to find area and circumference of a cirlce using class and objects

class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    def get_circumference(self):
        return 2*Circle.pi*self.radius

m=Circle(3)

m.area  # 28.26

m.get_circumference()  # 18.84

m.pi  # 3.14

m.radius # 3

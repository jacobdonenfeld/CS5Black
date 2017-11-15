# CS5 Black, hw10pr2
# Filename: shapes.py
# File Writer: RLH January 26, 2010
# Problem description: Shape class and friends

import math
import turtle

from Matrix import *
from Vector import *

class Shape(object):
    def __init__(self):
        self.points = []
        
    def render(self):
        """Use turtle graphics to render shape"""
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        for vector in self.points[1:]:
            turtle.setposition(vector.x, vector.y)
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.end_fill()

    def erase(self):
        """Draw shape in white to effectively erase it from screen"""
        temp = self.color
        self.color = "white"
        self.render()
        self.color = temp
    
    def rotate(self, theta, rotateAbout = Vector(0,0)):
        """Rotate shape by theta degrees """
        theta = math.radians(theta)  # THIS IS CORRECT!
        # Python's trig functions expect input in radians
        # so this function converts from degrees into radians.
        cent = self.center
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] - rotateAbout)
        self.center = self.center - rotateAbout
        self.points = newpoints
        NewPoints = []
        for vector in self.points:
            newvector = RotationMatrix * vector
            NewPoints.append(newvector)
        self.center = RotationMatrix * self.center
        self.points = NewPoints
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] + rotateAbout)
        self.center = self.center + rotateAbout
        self.points = newpoints

    def scale(self, x):
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] - self.center)
        self.points = newpoints
        newpoints = []
        for z in self.points:
            newvector = Vector(z.x *x, z.y *x)
            print(newvector)
            newpoints.append(newvector)
        print(newpoints)
        self.points = newpoints
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] + self.center)
        self.points = newpoints


    def flip(self, v1, v2):
        angle = math.atan((v2.y - v1.y) / (v2.x - v1.x))
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] - v1)
        self.points = newpoints
        self.rotate(angle)
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] - Vector(-2 * self.points[x].x), 0)
        self.points = newpoints
        newpoints = []
        for x in range(len(self.points)):
            newpoints.append(self.points[x] + v1)
        self.points = newpoints






class Rectangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "black"):
        self.center = center
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color

class Square(Rectangle):
    def __init__(self, width, center=Vector(0, 0), color = "black"):
        Rectangle.__init__(self, width, width, center, color)


        
class Circle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
        self.center = center
        self.radius = radius
        self.color = color

    def rotate(self, theta, rotateAbout=Vector(0, 0)):
        self.points = self.center
        self.rotate(self, theta, rotateAbout)



    def render(self):
        turtle.penup()
        turtle.setposition(self.center.x, self.center.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.center)
        turtle.end_fill()

    def rotate(self, theta):
        """ theta is in degrees """
        theta = math.radians(theta)
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
        self.center = RotationMatrix * self.center

class triangle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
        """Center is middle of equalateral triangle"""
        self.center = center
        self.radius = radius
        self.color = color
        self.points = [center + Vector(radius,0), center + Vector(- radius,0), center + Vector(0, radius)]

class LineSegment(Shape):
    def __init__(self, v1, v2):
        self.points = [v1,v2]

    def render(self):
        """Use turtle graphics to render shape"""
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.pencolor(self.color)
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.setposition(self.points[1].x, self.points[1].y)
        turtle.setposition(self.points[0].x + self.points[1].x /2, self.points[0].y + self.points[1].y /2)



        
        

"""My own Implementation of the famous kids tool LOGO.
basic functions are:
t = Turtle() - initiate an instance
t.moveForward(x) - moves the turtle x steps forward
t.rotateTurtle(a) - rotates the turtle a degrees in anticlockwise direction.
t.hide() - hides the turtle(movement still creates a line)
t.show() - show the hidden turtle
t.penUp() - the turtle will move without a trail.(no line will be drawn)
t.penDown() - the turtle will move with a trail.
"""
from Tkinter import *
from math import *
import re
c = Canvas(width = 700,height = 700)
c.pack()

class Turtle():
	def __init__(self):
		self.oangle = 0
		self.Canvas = c
		self.x = 350
		self.y = 350
		self.angle = 0
		self.hidden = 0
		self.a = c.create_polygon(362,350,350,345,350,355)	
		self.stop = 0

	def rotateTurtle(self,angle=0):
		self.angle = self.angle + angle
		c.delete(self.a)
		x1 = self.x+(12*cos((self.angle)*pi/180))
		y1 = self.y-(12*sin((self.angle)*pi/180))
		x2 = self.x+(5*cos((self.angle + 90)*pi/180))
		y2 = self.y-(5*sin((self.angle + 90)*pi/180))
		x3 = self.x+(5*cos((self.angle + 270)*pi/180))
		y3 = self.y-(5*sin((self.angle + 270)*pi/180))
		if not self.hidden:
			self.a = c.create_polygon(x1,y1,x2,y2,x3,y3)

	def moveForward(self,steps):
		x1 = self.x + steps*cos((self.angle)*pi/180)
		y1 = self.y - steps*sin((self.angle)*pi/180)
		if self.stop == 0:
			self.Canvas.create_line(self.x,self.y,x1,y1)
		self.x = x1
		self.y = y1
		c.move(self.a, +steps*cos((self.angle)*pi/180), -steps*sin((self.angle)*pi/180))

	def createCanvas(self):
		c = Canvas(width = 700, height = 700)
		c.pack()
	
	def show(self):
		self.hidden = 0
		c.delete(self.a)
		self.a = c.create_polygon(self.x+(12*cos((self.angle)*pi/180)),self.y-(12*sin((self.angle)*pi/180)),self.x+(5*cos((self.angle + 90)*pi/180)),self.y-(5*sin((self.angle + 90)*pi/180)),self.x+(5*cos((self.angle + 270)*pi/180)),self.y-(5*sin((self.angle + 270)*pi/180)))
		return self.hidden

	def hide(self):
		self.hidden = 1
		c.delete(self.a)
		return self.hidden

	def penDown(self):
		self.stop = 0
		return self.stop

	def penUp(self):
		self.stop = 1
		return self.stop


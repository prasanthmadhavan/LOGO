"""
My Own implementation of the koch snowflake and some other such recursive curves using LOGO.
"""
from logo import *

t = Turtle()

def snowFlake(times,length=200.00):
	t.penUp()
        t.rotateTurtle(180)
        t.moveForward(300)
	t.rotateTurtle(-90)
	t.moveForward(170)
        t.rotateTurtle(-90)
        t.penDown()
	pattern = "MRMRM"
	for i in range(times):
    		pattern = pattern.replace("M","MLMRMLM")
	for j in pattern:
    		if j=="M": t.moveForward(length / (3.00 ** (times - 1)))
    		elif j=="L": t.rotateTurtle(60)
    		elif j=="R": t.rotateTurtle(-120)
	t.rotateTurtle(-120)

def quadraticType1(times,length=100.00):
	t.penUp()
        t.rotateTurtle(180)
        t.moveForward(150)
	t.rotateTurtle(-90)
	t.moveForward(150)
        t.rotateTurtle(180)
        t.rotateTurtle(90)
	t.penDown()
	pattern = "MRMRMRM"
	for i in range(times):
    		pattern = pattern.replace("M","MLMRMRMLM")
	for j in pattern:
    		if j=="M": t.moveForward(length / (3.00 ** (times - 1)))
    		elif j=="L": t.rotateTurtle(90)
    		elif j=="R": t.rotateTurtle(-90)
	t.rotateTurtle(-90)


def kochIsland(times,length=100.00):
	t.penUp()
        t.rotateTurtle(180)
        t.moveForward(150)
	t.rotateTurtle(-90)
	t.moveForward(150)
        t.rotateTurtle(180)
        t.rotateTurtle(90)
	t.penDown()
	pattern = "MRMRMRM"
	for i in range(times):
    		pattern = pattern.replace("M","MLMRMRMMLMLMRM")
	for j in pattern:
    		if j=="M": t.moveForward(length / (3.00 ** (times - 1)))
    		elif j=="L": t.rotateTurtle(90)
    		elif j=="R": t.rotateTurtle(-90)
	t.rotateTurtle(-90)


def levyCurve(times,length=200.00):
	pattern = "LMRRM"
	for i in range(times):
    		pattern = pattern.replace("M","LMRRML")
	for j in pattern:
    		if j=="M": t.moveForward(length / (2.00 ** (times - 1)))
    		elif j=="L": t.rotateTurtle(45)
    		elif j=="R": t.rotateTurtle(-45)
	t.rotateTurtle(-120)



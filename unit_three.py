# James Bankole Unit 3 9/26/16
# This program prompts the user for a side length, center color, and petal color, then draws a flower using what the
# user inputed.

import turtle


def getSideLength():
    """ This function gets the size of each hexagon"""
    side = float(input("How long do you want the side length?"))
    return side


def getCenterColor():
    """This function gets the color of the center petal"""
    return input("What color do you want the center color to be?")


def getPetalColor():
    """This function gets the color for each petal"""
    return input("What color do you want the petals to be?")


def drawPetal(size, petalColor):
    """This function defines the turtle used for drawing the petals"""
    turtle.color(petalColor)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()


def drawHexagon(size, centerColor, petalColor):
    """This function defines the turtle that draws the entire flower"""
    turtle.color(centerColor)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)  # Turned left 120 so that the turtle faces the correct direction
    drawPetal(size, petalColor)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)
    drawPetal(size, centerColor)

    turtle.end_fill()


def main():
    turtle.speed(2)
    sideLength = getSideLength()
    centerColor = getCenterColor()
    petalColor = getPetalColor()
    drawHexagon(sideLength, centerColor, petalColor)

    turtle.done()

main()

from graphics import *
import random
import math


inputLayerN=int(input("How many neurons in are in the input layer: "))
noHiddenLayers=int(input("How many hidden layers: "))
outputLayerN=int(input("How many neurons in output layer: "))
window=GraphWin("VisualizeNN", 500, 500)

#Build neurons in first layer and line them up


newrow=100
for i in range(inputLayerN):
  # make the circle in the center
  circle = Circle(Point(100, newrow), 20)

  # set the circle to a random colors
  color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
  circle.setFill(color)
  # draw it
  circle.draw(window)
  newrow+=70

while True:
  pass
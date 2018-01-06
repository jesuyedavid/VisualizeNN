from graphics import *
import random
import math


window=GraphWin("VisualizeNNFullyConnected", 700, 500)
window.setBackground("white")
prom=Text(Point(200, 470), "How many neurons in first layer")
prom.draw(window)
texE=Entry(Point(200, 490), 20)
texE.draw(window)
netMat=[[]]

#click the mouse to signal done entering text
window.getMouse()

inputLayerN=int(texE.getText())
firLayerC=100
newrow=100
for i in range(inputLayerN):
  # make the circle in the center
  circle = Circle(Point(firLayerC, newrow), 20)
  netMat[0].append((firLayerC, newrow))
  # set the circle to a random colors
  color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
  circle.setFill(color)
  circle.draw(window)
  newrow+=70


prom.setText("How many hidden layers")
texE.setText("")
window.getMouse()
numhidL=int(texE.getText())
secLayerC=firLayerC+100
for i in range(0, numhidL):
  prom.setText("Neurons in "+str(i+2)+" layer")
  texE.setText("")
  window.getMouse()
  secLayerN=int(texE.getText())
  newrow=100
  laylist=[]
  for j in range(secLayerN):
    circle = Circle(Point(secLayerC, newrow), 20)
    laylist.append((secLayerC, newrow))
    # set the circle to a random colors
    color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
    circle.setFill(color)
    circle.draw(window)
    newrow+=70
  netMat.append(laylist)
  secLayerC+=100

print("newrow", netMat)
preColumn=netMat[-1][1][0]+100

prom.setText("How many neurons in output layer")
texE.setText("")
window.getMouse()
numoutL=int(texE.getText())
newrow=100
for i in range(numoutL):
      # make the circle in the center
  circle = Circle(Point(preColumn, newrow), 20)
  netMat[0].append((firLayerC, newrow))
  # set the circle to a random colors
  color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
  circle.setFill(color)
  circle.draw(window)
  newrow+=70

window.getMouse()
window.close()
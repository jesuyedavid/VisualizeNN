from graphics import *
import random
import math


window=GraphWin("VisualizeNNFullyConnected", 700, 500)
window.setBackground("white")
prom=Text(Point(200, 470), "How many neurons in first layer")
prom.draw(window)
texE=Entry(Point(200, 490), 20)
texE.draw(window)

#click the mouse to signal done entering text
window.getMouse()

inputLayerN=int(texE.getText())

firLayerC=100
newrow=100
for i in range(inputLayerN):
  # make the circle in the center
  circle = Circle(Point(firLayerC, newrow), 20)

  # set the circle to a random colors
  color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
  circle.setFill(color)
  # draw it
  circle.draw(window)
  newrow+=70

print(newrow)
prom.setText("Neurons in second layer")
texE.setText("")
window.getMouse()
secLayerN=int(texE.getText())
newrow=100
secLayerC=firLayerC+100
for i in range(secLayerN):
  circle = Circle(Point(secLayerC, newrow), 20)

  # set the circle to a random colors
  color = color_rgb(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
  circle.setFill(color)
  circle.draw(window)
  newrow+=70


window.getMouse()
window.close()
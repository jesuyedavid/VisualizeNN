import graphics
import random

# create the window
window = graphics.GraphWin("Snow!", 400, 400)

# set the background to a nice sky blue
window.setBackground("skyblue")

# make a list of 500 random points
flakes = []
for i in range(500):
    # random  location
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    p = graphics.Point(x, y)
    # color
    p.setFill("white")
    p.draw(window)
    # add to list
    flakes.append(p)

# keep looping forever
while True:
  # for each flake
  for f in flakes:
    # move it down 2 pixels
    f.move(0, 2)
    # if it's out of bounds, move it back to 0
    if f.getY( ) > 399:
      f.move(0, -400)


# close the window
window.close( )
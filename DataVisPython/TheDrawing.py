from graphics import *
import random
import time

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
data = datafile.readlines()

# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)


listOfBoxes = []
# GUIDE
# Processing version looks like this... 
# for(int i=0; i<datafile.length ;i=i+2) {

# SQUARES DATA VISUALIZATION (greyscale)
# using two data values for more unique position and sizes
while True:
    for i in range(0,len(data),2):
        firstnumber = int(float(data[i].strip())) * 3        
        secondnumber = int(float(data[i+1].strip())) * 3
        print(str(firstnumber) + " and " + str(secondnumber))
        box = Rectangle(Point(firstnumber,firstnumber),Point(secondnumber,secondnumber))
      #  box.setOutline(color_rgb(255,0,0))
      #  box.setFill(color_rgb(0,0,0))
        i = random.randint(0,255)
        box.setFill(color_rgb(i,i,i))
        box.draw(window)
        listOfBoxes.append(box)
        time.sleep(1./3)
    #for box in listOfBoxes:
        
        
# OTHER POSSIBLE SHAPES
# Change Values by replacing the points with firstnumber and secondnumber
#real time data instead of drawing on top
# ball = Circle(Point(100,100), 30)
# ball.setFill(color_rgb(255,255,0))
# ball.draw(window)


# line = Line(Point(200,200),Point(250,280))
# line.setWidth(4)
# line.draw(window)

# text = Text(Point(50,200),"Hello")
# text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()

# GCode Plotter
# Program written by Leo Rauschenberger
# Source: https://github.com/LeoRauschenberger/2DGcodePlotter

import turtle
import math

# user settings
f = 10                    # size increase factor
p = 3                     # size of pen tip
debugmode = 'y'           # y/n will display coordinates of G0 (goto) commands in window
drawcolor = (211,211,211) # RGB code or name e.g. "blue" of color you want to draw with 


# ------------------------------

def centers(x1, y1, x2, y2, r):
    q = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    xx = (r ** 2 - (q / 2) ** 2) ** 0.5 * (y1 - y2) / q
    yy = (r ** 2 - (q / 2) ** 2) ** 0.5 * (x2 - x1) / q
    return ((x3 + xx, y3 + yy), (x3 - xx, y3 - yy))


# ------------------------------
t=turtle
t.clear() #clear drawing window
# screen layout (can mess up aspect ratio if chose too big!)
#turtle.setworldcoordinates(-50, -50, 400, 300)
t.setworldcoordinates(0, 0, 600, 300)
t.title("Python 2D GCode Plotter and Debugger")
t.colormode(255)


t.ht() #render drawing-arrow invisible
t.pensize(p)

t.goto(0,0) # default start is 0,0
t.up()
t.write("X0 Y0" , move=True,align='left',font=('Arial',7))
t.up()
t.color(drawcolor)


#Draw Gcode
#file1 = open("cyrillic/ltr_Д.txt", "r")
file1 = open("cyrillic/helloworld.txt", "r")
Lines = file1.readlines()
count = 0
lList = []
# Strips the newline character
for line in Lines:
    count += 1
    # save previous List before overwriting
    prevlList=lList
    #strip newline character and split at spaces
    lList = line.strip().split(' ')
    print("{}: {}".format(count, lList)) # prints out line number and contents
    #draw
    
    if lList[0] == 'G0':
        if 'X' in lList[1]:
            x = float(lList[1].strip('X'))
            y = float(lList[2].strip('Y'))
            t.up()
            t.goto(x*f,y*f)
            # now write position if desired
            if debugmode == "y":
                t.color("black")
                t.dot(p*2)
                t.write("X"+str(round(x, 2))+" \nY"+str(round(y, 2)) , move=True,align='right',font=('Arial',8))
                t.color(drawcolor)
                t.up()
                t.goto(x*f,y*f)
        else:
            print("------------------------------------------------------")
            pass
    elif lList[0] == 'G1':
        x = float(lList[1].strip('X'))
        y = float(lList[2].strip('Y'))
        t.down()
        t.goto(x*f,y*f)
    elif lList[0] == 'G3':
        # retrieve starting point of arc from previous line:
        x1 = float(prevlList[1].strip('X'))
        y1 = float(prevlList[2].strip('Y'))
        # retrieve end point and radius of arc form current line:
        x2 = float(lList[1].strip('X'))
        y2 = float(lList[2].strip('Y'))
        r = float(lList[3].strip('R')) # can be negative!
        # calculate straight line distance between points
        dLength = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        # calculate opening angle in degrees
        openingAngle = math.acos(1- 0.5*(dLength/r)**2)*180/math.pi
        # https://lydxlx1.github.io/blog/2020/05/16/circle-passing-2-pts-with-fixed-r/
        nl=centers(x1, y1, x2, y2, r)
        xc = nl[0][0]
        yc = nl[0][1]
        print(xc, yc)
        startheading = math.atan((x1-xc)/(y1-yc))*180/math.pi+90
        # go to starting point and draw
        t.goto(x1*f,y1*f)
        t.down()
        t.setheading(startheading)
        t.circle(abs(r)*f,openingAngle)
    elif lList[0] == 'G2':
        t.circle(abs(r)*f,-openingAngle)
    else:
        pass

file1.close()

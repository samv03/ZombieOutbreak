# Quick project modeling a zombie outbreak game for a math modeling course.

from Tkinter import *
from random import *

polyflag = [0]*101
poly = [0]*101
zombieflag = [0]*101
rect = 0
humans = 49
totalhumans = humans
zombies = 1
totalzombies = zombies
day = 0
nextbuttonflag = 0
testiterations = 1

game = Tk()
can = Canvas(game, width=800, height=800)

x0=40
x1=68
x2=88
x3=68
x4=40
x5=20

y0=20
y1=20
y2=50
y3=80
y4=80
y5=50


cnt = 0
offset = 0

for x in range(0, 10):
    for y in range(0, 10):
        if x % 2 == 1:
            offset = 30
        else:
            offset = 0
        poly[cnt] = can.create_polygon(x0 + (x*48), y0 + (y*60) + offset, x1 + (x*48), y1 + (y*60) + offset, x2 + (x*48), y2 + (y*60) + offset, x3 + (x*48), y3 + (y*60) + offset, x4 + (x*48), y4 + (y*60) + offset, x5 + (x*48), y5 + (y*60) + offset, fill="white", outline="black", width=2)
        cnt += 1

nextrect = can.create_rectangle(550, 600, 650, 650, outline="black", fill='gray')
daytext = can.create_text(600, 75, font=("Times", 15), text='Day: ' + str(day))
humancounttext = can.create_text(600, 100, font=("Times", 15), text='Humans: ' + str(humans))
zombiecounttext = can.create_text(600, 128, font=("Times", 15), text='Zombies: ' + str(zombies))
simulatetext = can.create_text(600, 200, font=("Times", 15), text='Simulation:')
iterationtext = can.create_text(610, 228, font=("Times", 15), text='Iterations: ' + str(testiterations))
simstart = can.create_text(600, 300, font=("Times", 15), text='Start Sim')

def onObjectClick(event):
    global humans
    global nextbuttonflag
    item = event.widget.find_closest(event.x, event.y)
    
    if  polyflag[item[0]] == 0 and humans != 0:
        can.itemconfig(poly[item[0]-1], fill='green')
        polyflag[item[0]] = 1
        humans -= 1
        can.itemconfig(humancounttext, text='Humans: ' + str(humans))
    elif polyflag[item[0]] == 1:
        can.itemconfig(poly[item[0]-1], fill='white')
        polyflag[item[0]] = 0
        humans += 1
        can.itemconfig(humancounttext, text='Humans: ' + str(humans))

    if humans == 0:
        can.itemconfig(nextrect, fill='green')
        nextbuttonflag=1
    else:
        can.itemconfig(nextrect, fill='gray')
        nextbuttonflag=0

    print item[0]

def onNextButton(event):
    global nexbuttonflag
    if nextbuttonflag:
        print "next is green"
        zombies = totalzombies

        while zombies != 0:
            randindex = getRand()
            if zombieflag[randindex] == 0:
                zombieflag[randindex] = 1
                zombies -= 1
                print randindex            
        
    else:
        print "next is gray"

def simStartButton(event):
    print "Sim Start"

    iterationcount = testiterations
    while iterationcount != 0:
        roundhumans = totalhumans
        roundzombies = totalzombies
        daycount = 0
        
        while roundhumans > 0 and roundzombies > 0:
            sethumans = roundhumans
            setzombies = roundzombies
            print "Day: " + str(daycount)
            print "Humans: " + str(sethumans)
            print "Zombies: " + str(setzombies)

            while sethumans != 0:
                rand = getRand()
                if polyflag[rand] == 0:
                    polyflag[rand] = 1
                    sethumans = sethumans - 1                    

            while setzombies != 0:
                rand = getRand()
                if zombieflag[rand] == 0:
                    zombieflag[rand] = 1
                    setzombies = setzombies -1

            for x in range(1, 101):
                if zombieflag[x] == 1:
                    numhumans = humancheck(x)
                    
                    if numhumans > 4:
                        roundzombies = roundzombies - 1
                    elif numhumans < 4:
                        roundzombies = roundzombies + numhumans
                        roundhumans = roundhumans - numhumans  
            for y in range(1, 101):
                polyflag[y] = 0
                zombieflag[y] = 0
            daycount += 1

        print "Day: " + str(daycount)
        print "Humans: " + str(roundhumans)
        print "Zombies: " + str(roundzombies)

        daycount = 0 
        iterationcount = iterationcount - 1
            

def getRand():
    return randint(0, 100)

def humancheck(spot):
    columncheck = spot
    columnnumber = 0
    while columncheck > 10:
        columncheck = columncheck - 10
        columnnumber += 1
    
    if columnnumber % 2:
        columnnumber = 1
    else:
        columnnumber = 0

    numberofhumans = 0
    checks = [0]*7
    checks[0] = origincheck(spot)
    checks[1] = lowerleftcheck(spot, columnnumber)
    checks[2] = upperleftcheck(spot, columnnumber)
    checks[3] = upcheck(spot)
    checks[4] = upperrightcheck(spot, columnnumber)
    checks[5] = lowerrightcheck(spot, columnnumber)
    checks[6] = downcheck(spot)


    for i in range(0, 7):
        if checks[i]:
            numberofhumans += 1
    if numberofhumans < 4:
        for j in range(0, 7):
            polyflag[checks[j]] = 0

    return numberofhumans

def origincheck(spot):
    if polyflag[spot]:
        return spot
    else:
        return 0

def lowerleftcheck(spot, columnnumber):
    if spot >= 1 and spot <= 10:
        return 0
    elif spot % 20 == 0:
        return 0
    else:
        if polyflag[spot - 10 + columnnumber]:
            return spot - 10 + columnnumber
        else:
            return 0

def upperleftcheck(spot, columnnumber):

    if spot >= 1 and spot <= 10:
        return 0
    elif (spot - 1) % 20 == 0:
        return 0
    else:
        if polyflag[spot - 11 + columnnumber]:
            return spot - 11 + columnnumber
        else:
            return 0

def upcheck(spot):

    if (spot - 1) % 10 == 0:
        return 0
    else:
        if polyflag[spot - 1]:
            return spot - 1
        else:
            return 0

def upperrightcheck(spot, columnnumber):

    if spot >= 91 and spot <= 100:
        return 0
    elif (spot - 1) % 20 == 0:
        return 0
    else:
        if polyflag[spot + 9 + columnnumber]:
            return spot + 9 + columnnumber
        else:
            return 0

def lowerrightcheck(spot, columnnumber):

    if spot >= 91 and spot <= 100:
        return 0
    elif spot % 20 == 0:
        return 0
    else:
        if polyflag[spot + 10 + columnnumber]:
            return spot + 10 + columnnumber
        else:
            return 0

def downcheck(spot):
    if spot % 10 == 0:
        return 0
    else:
        if polyflag[spot + 1]:
            return spot + 1
        else:
            return 0
    

for j in range(0,100):
    can.tag_bind(poly[j], '<ButtonPress-1>', onObjectClick)
can.tag_bind(nextrect, '<ButtonPress-1>', onNextButton)
can.tag_bind(simstart, '<ButtonPress-1>', simStartButton)
can.pack()


game.mainloop()

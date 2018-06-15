import pyautogui as pyag
import time
#edge of screen to beginning of emulator screen
xpad = 65
ypad = 60
def getCoords():
    print (pyag.position())

screenWidth, screenHeight = pyag.size()
def leftClick(pos):
    #pos is list with [x,y]
    pyag.moveTo(pos[0],pos[1])
    pyag.click()
def leftClickHoldFor(pos, seconds):
    pyag.moveTo(pos[0],pos[1])
    pyag.mouseDown()
    time.sleep(seconds)
    pyag.mouseUp()
    

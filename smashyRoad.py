import core_controls as cc
import neural_core as nc
import pyautogui as pyag
import SimpleCV
from PIL import Image
import time
import tensorflow as tf

turnRightPixel = [469, 194]
turnLeftPixel = [130, 191]

def playAgain():
    # play button to try again
    cc.leftClick([291, 287])
    time.sleep(3)

def startGame():
    # cancel google play games popup  (322, 221)
    cc.leftClick([322, 221])
    time.sleep(5)
    # exit smashyroad2ad (434, 106)
    cc.leftClick([434, 106])
    time.sleep(3)
    # tap left or right to start driving
    cc.leftClick(turnLeftPixel)

#def checkPixelColor(pixel):
#    im =  pyag.screenshot(pixel)
#    return im.getpixel(pixel)
     
def getBinarizedScreen():
    im =  pyag.screenshot(region=(65, 60, 458, 260))#left, top, width, and height
    ##this is a PIL image
    im = im.convert('1')
    #im = im.resize((50, 25))
    im.save("test.png")
    return im

def executeCommand(command):
    if command is 0:#left 0.5
	print "left 0.5"
	cc.leftClickHoldFor(turnLeftPixel, 0.5)
    elif command is 1:#right 0.5
	print "right 0.5"
	cc.leftClickHoldFor(turnRightPixel, 0.5)
    elif command is 2:#straight 0.5
	print "straight 0.5"
	time.sleep(0.5)
    elif command is 3:#left 1
	print "left 1"
	cc.leftClickHoldFor(turnLeftPixel, 1)
    elif command is 4:#right 1
	print "right 1"
	cc.leftClickHoldFor(turnRightPixel, 1)
    elif command is 5:#straight 1
	print "straight 1"
	time.sleep(1)

def maneuver():
    fitness = 0
    while True:
        command = getCommand()
        executeCommand(command)
        time.sleep(0.01)
        #if pixel at (329, 173) is white (means arrested), exit
        if pyag.pixelMatchesColor(329,173, (255, 248, 221)):
            print "arrested"
            return fitness
        screen = getBinarizedScreen()
        #print list(screen.getdata())
        #print len(list(screen.getdata()))
        fitness += 1
        

########################################################### Evolution

########################################################### End Evolution
########################################################### Neural Network Definition
pixelInputs = len(getBinarizedScreen().getdata())
print pixelInputs, "inputs"
input_layer = tf.placeholder(tf.float32, shape=[None, pixelInputs])
#units is number of neurons
dense = tf.layers.dense(inputs=input_layer, units=50, activation=tf.nn.relu)
dense2 = tf.layers.dense(inputs=dense, units=50, activation=tf.nn.relu)
    
logits = tf.layers.dense(inputs=dense2, units=6)#l,r,straight, reverse...potentially more for [right for 5 cycles] or [left for 10 cycles]
    
predictions = {
  # Generate commands
  "classes": tf.argmax(input=logits, axis=1),
}
############################################################### End Neural Network Definition

#im = Image.open("test.png")
#data = list(im.getdata())
#print logits.eval(feed_dict={input_layer:[data]})
#print predictions["classes"].eval(feed_dict={input_layer:[data]})

cc.getCoords()
#startGame()
with tf.Session() as sess:

    sess.run(tf.global_variables_initializer()) 
    def getCommand():
        data = list(getBinarizedScreen().getdata())
        return int(predictions["classes"].eval(feed_dict={input_layer:[data]}, session=sess)[0])

    while True:
	fitness = maneuver()
        print "fitness was", fitness
	string = raw_input("push enter start another trial")
	playAgain()

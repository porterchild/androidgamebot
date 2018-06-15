import pyscreenshot as ImageGrab
import os
import time

def screenGrab():
    box = (65,60,515,320)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()

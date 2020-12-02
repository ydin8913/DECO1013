from microbit import *
import neopixel
from random import randint
import music
import Toys


def neopi(light):
    for pi in range(0,len(np)):
            np[pi] = light
            np.show()

# Setup the Neopixel strip on pin2 with a length of 30 pixels
np = neopixel.NeoPixel(pin2, 30)

# using toys's class Gesture
gesture=Toys.Gesture()
while True:
    str_gesture=gesture.read()
    if str_gesture=='left':
		#Added sound effects
        tune = ["A2:4", "A2:4"]
        music.play(tune)
        neopi((0,0,0))
    if str_gesture=='right':
        tune = ["A2:4", "A2:4"]
        music.play(tune)
        neopi((255,255,255))
    if str_gesture=='backward':
        neopi((0,0,255))
    if str_gesture=='forward':
        neopi((255,0,0))


'''
    if button_a.is_pressed():
        neopi((255,255,255))
    if button_b.is_pressed():
        neopi((255,0,255))
'''


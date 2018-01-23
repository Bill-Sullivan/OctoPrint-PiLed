import sys
import time
import math
from neopixel import *
count = int(sys.argv[1])
percent = int(sys.argv[2])
# LED strip configuration:
LED_COUNT      = count   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2811_STRIP_GRB	
#LED_STRIP      = ws.SK6812W_STRIP
lightUp = math.floor(percent/count)
# Intialize the library (must be called once before other functions).
def setPixel(strip):
	for i in range(count):
		if(i<lightUp):
			strip.setPixelColor(i, Color(0, 255, 0))
			strip.show()
		else:
			strip.setPixelColor(i, Color(255, 0, 0))
			strip.show()
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)		
	strip.begin()
	setPixel(strip)

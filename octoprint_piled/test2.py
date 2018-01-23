import time
import os
while(1):
	for i in range(0, 110, 10):
		os.system('sudo python /home/pi/OctoPrint-PiLed/octoprint_piled/strip.py 10 '+str(i))
		time.sleep(.5)

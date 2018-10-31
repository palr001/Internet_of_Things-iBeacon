import RPi.GPIO as GPIO
import time
import subprocess
import os

beacon = 1

try:
	while True:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		if beacon == 1 and True:
			input_state = GPIO.input(18)
			subprocess.call(['iBeacon/iBeacon.sh'])
			print("Beacon 1")
			time.sleep(0.5)
			if input_state == False:
				beacon = 2
				os.system("hciconfig hci0 reset")
				print("Next beacon")
			
		if beacon == 2 and True:
			input_state = GPIO.input(18)
			subprocess.call(['iBeacon/iBeacon2.sh'])
			print("Beacon 2")
			time.sleep(0.5)
			if input_state == False:
				beacon = 3
				os.system("hciconfig hci0 reset")
				print("Next beacon")
		
		if beacon == 3 and True:
			input_state = GPIO.input(18)
			subprocess.call(['iBeacon/iBeacon3.sh'])
			print("Beacon 3")
			time.sleep(0.5)
			if input_state == False:
				beacon = 1
				os.system("hciconfig hci0 reset")
				print("Next beacon")
				
		else:
			GPIO.cleanup()
			
except KeyboardInterrupt:
	print("Keyboard interrupt")
	
finally:
	print("The program has ended")
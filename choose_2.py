# at this to crontab -> @reboot python3 /home/pi/choose_2.py -> etc/rc.local -> crontab 

#print("0")
import main_test as main
import evasion_test as evasion
import RPi.GPIO as GPIO
from time import sleep

def set_gpios_():
    GPIO.setmode(GPIO.BCM)    
    #Input pins
    GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#print("1")
set_gpios_()
#print("2")

if GPIO.input(17) == 1:
    #print("main")
    main.run()
   # print("main")
if GPIO.input(4) == 1:
    #print("evasion")
    evasion.run()


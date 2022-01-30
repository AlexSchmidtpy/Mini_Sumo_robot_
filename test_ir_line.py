
import RPi.GPIO as GPIO
from time import sleep
import pickle
def set_gpios():
    GPIO.setmode(GPIO.BCM)
    #line sensor output pins -> pi input pins
    GPIO.setup(26, GPIO.IN) #
    GPIO.setup(19, GPIO.IN) #
    GPIO.setup(13, GPIO.IN) #
    #GPIO.setup(6, GPIO.IN) #

#set all gpios
set_gpios()
 
def check_pin(gpio=26): # line is / isn´t dedected 
    if GPIO.input(gpio) == 1:  
        return [gpio,1]
    elif GPIO.input(gpio) == 0: 
        return [gpio,0]  
def check_all_gpios(): # creat list of all line sensors for main program (main_test.py)
    set_gpios()
    all_gpios=[26,19,13]
    all_gpios_high_or_low=[[26,0,"front"],[19,0,"right"],[13,0,"left"]] #[6,0,"back"] doesnt work

    for i in all_gpios:
        check_pin_= check_pin(i)
        for j in all_gpios_high_or_low:
            if check_pin_[0] == j[0]  and 0 == check_pin_[1]:
                all_gpios_high_or_low[all_gpios_high_or_low.index(j)][1] = 0
            elif j[0] == check_pin_[0] and 1 == check_pin_[1]:

                all_gpios_high_or_low[all_gpios_high_or_low.index(j)][1] = 1            
    return all_gpios_high_or_low
if __name__ == "__main__":  #only run when the file is direktly excecuted -> testing sensors
    for i in range(0,5):
        a=check_all_gpios()
        print(a)
        sleep(1)
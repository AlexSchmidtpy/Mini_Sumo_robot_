# dc gear motors and l293D ic chip
import RPi.GPIO as GPIO
from time import sleep



def set_gpios():
    GPIO.setmode(GPIO.BCM)    
    #motor pins
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)


def calculate_time(speed=50, basic_time=0.001 ): # basic_time ..... still time for ir sensors to detect while driving (not by time e.g 1 sec)
    devision = 100/speed # e.g speed 50 -> 2
    time_off = (basic_time * devision) - basic_time # e.g (0.001*2)-0.001 = 0.001 -> on 0.001 seconds then off 0.001 seconds
    return [basic_time, time_off]

def calculate_for_loop_for_rotation(degrees = 180,basic_time=0.001): 
    value = 1/(360/ degrees) # e.g 180 -> 1/(360/180) -> 1/2 -> 0.5
    loop_range = (0.4 * value)/basic_time # 0.4 == 360 degree -> e.g 0.4 * 0.5 = 0.2 (0.2 == 180) -> (0.4 * 0.5)/ 0.001 = 200 -> for i in range (1,200+1)
    return int(loop_range)


def calculate_for_loop(basic_time=0.001, cm=1):
    value = 0.01 * cm # 0.01==1cm e.g 0.01 * 10cm = 1
    loop_range = value / basic_time # 1/0.001 = 1000 -> for i in range (1,1000+1) -> motors on(basic_time long) off(time_off)
    return int (loop_range)
def clean_up():
    GPIO.output(25,0)
    GPIO.output(16,0)
    GPIO.output(21,0)
    GPIO.output(20,0)
    GPIO.output(12,0)
    GPIO.output(13,0)
    GPIO.cleanup()

def hinten(speed=50, cm = 1): # moves the robot backwards
    set_gpios()
    times = calculate_time(speed)
    loop_range = calculate_for_loop(times[0], cm=cm)
    for i in range(1,loop_range + 1):
        GPIO.output(20,0)
        GPIO.output(21,1)
        GPIO.output(16,1)
        GPIO.output(25,0)
        sleep(times[0])
        GPIO.output(20,0)
        GPIO.output(21,0)
        GPIO.output(16,0)
        GPIO.output(25,0)
        sleep(times[1])
    

def vorne(speed=50,cm=1): # moves the robot forwards

    set_gpios()
    times = calculate_time(speed) # return [basic_time, time_off]
    loop_range = calculate_for_loop(times[0], cm=cm) # times[0] -> basic_time

    for i in range(1, loop_range+1):
        GPIO.output(20,1)
        GPIO.output(21,0)
        GPIO.output(16,0)
        GPIO.output(25,1)
        sleep(times[0])
        GPIO.output(20,0)
        GPIO.output(21,0)
        GPIO.output(16,0)
        GPIO.output(25,0)
        sleep(times[1])


def drehen(clock_wise=False,speed=50, degrees = 180): # rotate = in german "drehen" 
    set_gpios()
    basic_time_=0.001
    times = calculate_time(speed, basic_time=basic_time_)
    for_loop = calculate_for_loop_for_rotation(degrees=degrees, basic_time=basic_time_)
    if clock_wise == True:
        for i in range(1,for_loop +1):
            GPIO.output(20,1)
            GPIO.output(21,0)
            GPIO.output(16,1)
            GPIO.output(25,0)
            sleep(times[0])
            GPIO.output(20,0)
            GPIO.output(21,0)
            GPIO.output(16,0)
            GPIO.output(25,0)
            sleep(times[1])

    else:
        for i in range(1, for_loop +1):
            GPIO.output(20,0)
            GPIO.output(21,1)
            GPIO.output(16,0)
            GPIO.output(25,1)
            sleep(times[0])
            GPIO.output(20,0)
            GPIO.output(21,0)
            GPIO.output(16,0)
            GPIO.output(25,0)
            sleep(times[1])



set_gpios()



if __name__ == "__main__":
    vorne()
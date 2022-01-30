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
    devision = 100/speed 
    time_off = (basic_time * devision) - basic_time
    return [basic_time, time_off]

def calculate_for_loop(degrees = 180, speed = 40, basic_time=0.001): # 24000 == 360 degree  -> 24000 = speed * loop_range (for 360 degrees)
    degrees_to_360= (1/(360/degrees)) # degrees = 180 => num is 0.5 of 360
    speed_times_looprange_for_degrees_num = (24000* degrees_to_360) # 24000 * 0.5 = 1200
    loop_range = (speed_times_looprange_for_degrees_num/speed)*(1/basic_time)
    return int(loop_range)

def clean_up():
    GPIO.output(25,0)
    GPIO.output(16,0)
    GPIO.output(21,0)
    GPIO.output(20,0)
    GPIO.output(12,0)
    GPIO.output(13,0)
    GPIO.cleanup()

def hinten(speed=50, loop_range = 100): # moves the robot backwards
    set_gpios()
    times = calculate_time(speed)
    
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
    

def vorne(speed=50,loop_range = 10): # moves the robot forwards

    set_gpios()
    times = calculate_time(speed)

    for i in range(1,loop_range+1):
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
    basic_time_=1
    times = calculate_time(speed, basic_time=basic_time_)
    for_loop = calculate_for_loop(degrees=degrees, speed= speed,  basic_time=basic_time_)
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
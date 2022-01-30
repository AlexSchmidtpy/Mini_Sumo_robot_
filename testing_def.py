def calculate_time(speed=50):
    basic_time = 0.01 #still time for ir sensors to detect while driving (not by time e.g 1 sec)
    devision = 100/speed 
    time_off = (basic_time * devision) - basic_time
    return [basic_time, time_off]

time_= calculate_time(1)
print(time_)
def calculate_degrees(degrees = 180, speed = 40):# 24000 == 360 degree  -> 24000 = speed * loop_range (for 360 degrees)
    degrees_to_360= (1/(360/degrees)) # degrees = 180 => num is 0.5 of 360
    speed_times_looprange_for_degrees_num = (24000* degrees_to_360) # 24000 * 0.5 = 1200
    loop_range = speed_times_looprange_for_degrees_num/speed # 300 => for in range (1, 300+1) to get 180 turn by speed 40 
    return loop_range
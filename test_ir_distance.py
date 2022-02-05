###!/usr/bin/python
from time import sleep 
import spidev 
import test_platine
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
def readChannel(channel): #read channel
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data
def dist(channel=0,pause_on=True,position="front",pause=0.1,): # get the distance from a choosen ir sensor in cm
     v=(readChannel(channel)/1023.0)*4.99 # 4.99 V
     dist = (16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439)  /3 # /3 is making it better for Mini Sumo distances (5-60cm)but can work without it 
     if pause_on==True:
         sleep(pause)
     return dist
sharp_positions={"1":[3,"back"], 
      "2":[1,"front"],
      "3":[0,"left"],
      "4":[2,"right"]  # shrapsensor nummber : channel nummber of the ic chip , position of sensor

}

def get_all_dists(pause_on_=False,pause_=0): # getting all data/distances from each sensor
    list_of_dists=[]
    for i in sharp_positions.values(): # e.g [3,"back"]
        distance=dist(channel= i[0],pause_on= False ,position=i[1]) #get all  
        list_of_dists.append([i[1],distance])  # e.g ["back", 30] ->(30cm)
    return list_of_dists

def identify(): # making decision based on ir sensors data / distances -> moving the robot in new position when he dedects  a opponent 
    distances=get_all_dists()
    for i in distances:
        if i[1]<15:  
            if i[0]=="front":
                test_platine.vorne(speed=100,cm=25) #attack the enemy robot
                return
            elif i[0]=="back":
                test_platine.drehen(clock_wise=False, speed = 100, degrees=180) #rotate to enemy
                test_platine.vorne(speed=100,cm=25) #attack the enemy robot
                return
            elif i[0]=="left":
                test_platine.drehen(clock_wise=False, speed = 100, degrees=90) #rotate to enemy
                test_platine.vorne(speed=100,cm=25) #attack the enemy robot
                return
            elif i[0]=="right":
                test_platine.drehen(clock_wise=True, speed = 100, degrees=90) #rotate to enemy
                test_platine.vorne(speed=100,cm=25) #attack the enemy robot
                return
            return
if __name__ == "__main__":    # only run when the file is direktly excecuted -> testing sensors
    for i in range(100):
        distances=get_all_dists()
        print(distances)
        sleep(1)
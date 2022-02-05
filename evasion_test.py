from time import sleep 
import test_platine as platine
import test_ir_distance as ir_distance
def distance():
    distances=ir_distance.get_all_dists()
    for i in distances:
        if i[1]<30 and i[0]=="front":  
            platine.drehen(degrees=180, speed=50)
            platine.vorne(speed=50,cm=10)
            return
        elif i[1]<5 and i[0]=="back":
            platine.vorne(speed=50,cm=10)
            return

        elif i[1]<10 and i[0]=="right":
            platine.drehen(degrees=90, speed=50)
            platine.vorne(speed=50,cm=10)
            return
        elif i[1]<10 and i[0]=="left":
            platine.drehen(clock_wise=True,degrees=90, speed=50 )
            platine.vorne(speed=50,cm=10)
            return

def run():
    
    try:
        while True:
            platine.vorne(speed=50,cm=1)
            do=distance()                
    except KeyboardInterrupt:
        platine.clean_up()
        return
if __name__=="__main__":
    a=run()
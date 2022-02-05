from time import sleep 
import test_platine 
import test_ir_distance 
import test_ir_line 
 
def run():
    Inputs_ir_line = [[26,1,""],[19,1,""],[13,1,""]] #,[6,1] defect
    for i in range(0,200): # for fight use while loop and for testing for loop
        try:
            if i>0:
                Inputs_ir_line = test_ir_line.check_all_gpios()
            while Inputs_ir_line[0][1]==1 and  Inputs_ir_line[1][1]==1 and  Inputs_ir_line[2][1]==1 : # as long as no line is dedected 
                test_platine.vorne(speed = 40,cm=1) # slowly driving to have enough time to react to sensor data
                Inputs_ir_line = test_ir_line.check_all_gpios()
                #print("while", Inputs_ir_line)
                test_ir_distance.identify() # if enemy is dedected -> rotate to him -> full speed driving/attack                 
            for i in Inputs_ir_line:
                if i[1]==0:

                    if i[2]=="front":
                        test_platine.drehen(clock_wise=False, speed = 60, degrees=180) # roate in the opposite direction of the line
                        test_platine.vorne(speed = 40, cm=10) # 10cm to get away from the line/border
                        break
                    elif i[2]=="left":
                        test_platine.drehen(clock_wise=True, speed = 40,degrees=120)# roate in the opposite direction of the line
                        test_platine.vorne(speed = 40, cm=10) # 10cm to get away from the line/border
                        break
                    elif i[2] =="back" :
                        test_platine.vorne(speed = 40, cm=10) # 10cm to get away from the line/border
                        break
                    elif i[2] == "right":
                        test_platine.drehen(speed = 40,clock_wise=False,degrees=120) # roate in the opposite direction of the line
                        test_platine.vorne(speed = 40, cm=10) # 10cm to get away from the line/border
                        break
        except KeyboardInterrupt:
            test_platine.clean_up()# cleaning motor pins and more 
            return
if __name__=="__main__":
    a=run()
    #platine.forne(1)
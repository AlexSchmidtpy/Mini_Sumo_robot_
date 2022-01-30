from time import sleep 
import test_platine 
import test_ir_distance 
import test_ir_line 
 
def run():
    Inputs_ir_line = [[26,1,""],[19,1,""],[13,1,""]] #,[6,1]
    for i in range(0,200):
        try:
            if i>0:
                Inputs_ir_line = test_ir_line.check_all_gpios()
            while Inputs_ir_line[0][1]==1 and  Inputs_ir_line[1][1]==1 and  Inputs_ir_line[2][1]==1 : # as long as no line is dedected 
                test_platine.vorne(speed = 40,loop_range=10) #speed=50
                Inputs_ir_line = test_ir_line.check_all_gpios()
                #print("while", Inputs_ir_line)
                test_ir_distance.identify()                
            for i in Inputs_ir_line:
                if i[1]==0:
                    if i[2]=="front":
                        test_platine.drehen(clock_wise=False, speed = 60, degrees=180)
                        test_platine.vorne(speed = 40, loop_range=200) 
                        break
                    elif i[2]=="left":
                        test_platine.drehen(clock_wise=True, speed = 40,degrees=90)
                        test_platine.vorne(speed = 40, loop_range=200) #0.02
                        break
                    elif i[2] =="back" :
                        test_platine.vorne(speed = 40, loop_range=200) 
                        break
                    elif i[2] == "right":
                        test_platine.drehen(speed = 40,clock_wise=False,degrees=90)
                        test_platine.vorne(speed = 40, loop_range=200) 
                        break
        except KeyboardInterrupt:
            test_platine.clean_up()
            return
if __name__=="__main__":
    a=run()
    #platine.forne(1)
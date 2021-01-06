# Credit: https://github.com/DhairyaShah-Programmer

import time



# Time Logic
def timeMainOpt():
    topic = str(input("What will you do today: "))
    timeM = int(input('How much time you will spend for ' + topic + ": "))
    if timeM > 480:
        print("Not Valid Time, Select time below 480 minutes ")
    else:
        print('You have taken ' + str(timeM) + ' mins to focus for ' + topic)
        for i in range(timeM-1, -1, -1):
            time.sleep(60)
            if i == 0:           
                print("You are done! Good Job!")
                
            else:
                print(str(timeM-i)+ " minute elapsed of " + str(timeM) + " mins")
            
        




timeMainOpt()
    

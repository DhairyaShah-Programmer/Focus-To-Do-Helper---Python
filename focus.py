# Credit: https://github.com/DhairyaShah-Programmer

import time



# Time Logic
def timeMainOpt():
    timeM = int(input('Enter time in Minutes: '))
    if timeM > 480:
        print("Not Valid Time, Select time below 480 minutes ")
    else:
        print('You have taken ' + str(timeM) + ' mins to focus')
        for i in range(timeM, -1, -1):
            time.sleep(3)
            if i == 0:           
                print("You are done! Good Job!")
                
            else:
                print(str(timeM-i)+ " minute elapsed of " + str(timeM) + " mins")
            
        




timeMainOpt()

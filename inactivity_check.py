from time import sleep
import schedule
from ctypes import Structure, windll, c_uint, sizeof, byref

#gobal variables
inactivie = False
activie = True



class LASTINPUTINFO(Structure):
    _fields_ = [("cbSize", c_uint), ("dwTime", c_uint)]

def get_idle_duration():
    lii = LASTINPUTINFO()
    lii.cbSize = sizeof(LASTINPUTINFO)
    windll.user32.GetLastInputInfo(byref(lii))
    millis = windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0


def check_inactivity():
    global inactivie 
    global activie 
    idle_time = get_idle_duration()
    if idle_time >= 5:
        inactivie = True
        activie = False
        print("inactive")
    else:
        inactivie = False
        activie = True
        print("active")


flag =True
    
def inactiviity_checker():
    global activie, inactivie
    global flag 
    while True :
        if flag :
            schedule.every(1).seconds.do(check_inactivity)
            flag = False

        while activie :
            schedule.run_pending()
            sleep(1)
            flag = False
            if inactivie :
                flag = True
                break
        
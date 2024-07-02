import random
import subprocess
import threading
import keyboard
import schedule
from ctypes import Structure, windll, c_uint, sizeof, byref
import pyautogui as gui
from time import sleep
from words_list import words
import open_edge

class LASTINPUTINFO(Structure):
    _fields_ = [("cbSize", c_uint), ("dwTime", c_uint)]

def get_idle_duration():
    lii = LASTINPUTINFO()
    lii.cbSize = sizeof(LASTINPUTINFO)
    windll.user32.GetLastInputInfo(byref(lii))
    millis = windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0

inactivie = False
activie = True

#checks for inactivity
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

terminate = False

#for pause the task
def check_esc_press(): 
    global terminate, inactivie

    print("Press 'Esc' to exit")
    while True:
        # sleep(0.5)
        # print("waiitng for esc")
        flag = keyboard.is_pressed('esc')

        while inactivie :
            if flag:
                print("The 'Esc' key is pressed.")
                terminate =True
                inactivie =False
                flag = False
                break

freq=0
complete = False

def task():
    global freq ,inactivie, terminate, flag, complete
    n=30
    while True:
        

        while inactivie:
                
                if terminate :
                    flag =  True
                    break

                if freq == n+1 :
                    freq = 0
                    open_edge.close_edge_browser()
                    complete =True
                    break

                gui.hotkey('win', 'd')
                sleep(1)
                open_edge.open_edge_browser()
                
                
                
                sleep(1)
                gui.typewrite("bing search history")
                sleep(1)
                gui.press("enter")

                sleep(2)
                
                while (freq<=n):
                    if terminate :
                        flag = True
                        break

                    gui.moveTo(x=642, y=147)
                    gui.click()
                    sleep(1)
                    gui.hotkey('ctrl', 'a')
                    sleep(1)
                    gui.press('backspace')
                    sleep(1)
                    if terminate :
                        flag = True
                        break
                    random_word = random.choice(words)      
                    gui.write(random_word)
                    sleep(1)
                    gui.press('enter')
                    if terminate :
                        flag = True
                        break
                    sleep(3)
                    freq=freq+1
                    print(freq)
  
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
        





if __name__ == "__main__":
    
    inactivity_thread = threading.Thread(target=inactiviity_checker, daemon= True)
    task_thread = threading.Thread(target=task, daemon= True)
    #exit_thread = threading.Thread(target=check_esc_press, daemon= True)

    

    inactivity_thread.start()
    task_thread.start()
    #exit_thread.start()

    while True:
        if complete :
            print(f" searches completed")
            exit()
           
    
    
        
        

        
                
            

        
        
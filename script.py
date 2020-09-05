import os             
import pyautogui
import time
from time import sleep
from datetime import datetime


try:
    # open MS Teams application
    os.startfile("C:/Users/username/AppData/Local/Microsoft/Teams/current/Teams.exe") 
    sleep(2)
    # settings
    settings = pyautogui.locateCenterOnScreen("settings.PNG") 
    pyautogui.moveTo(settings)
    pyautogui.click()
    time.sleep(2)
    # manageteams.PNG
    manageteams = pyautogui.locateCenterOnScreen("manageteams.PNG") 
    pyautogui.moveTo(manageteams)
    pyautogui.click()
    time.sleep(2)
except Exception as e:
    print(e)

while True:
    #DemoMeetOne
    now = datetime.now().strftime("%H:%M")
    if now < '11:00':
        DemoMeetOne = pyautogui.locateCenterOnScreen("DemoMeetOne.PNG") 
        pyautogui.moveTo(DemoMeetOne)
        pyautogui.click()
        time.sleep(2)
        join = pyautogui.locateCenterOnScreen("join.PNG") 
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(2)
        audiooff = pyautogui.locateCenterOnScreen("audiooff.PNG") 
        pyautogui.moveTo(audiooff)
        pyautogui.click()
        time.sleep(2)
        
    elif now <'10:00':
      	#DemoMeetTwo
        DemoMeetTwo = pyautogui.locateCenterOnScreen("DemoMeetTwo.PNG") 
        pyautogui.moveTo(DemoMeetTwo)
        pyautogui.click()
        time.sleep(2)
        join = pyautogui.locateCenterOnScreen("join.PNG") 
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(2)
        audiooff = pyautogui.locateCenterOnScreen("audiooff.PNG") 
        pyautogui.moveTo(audiooff)
        pyautogui.click()
        time.sleep(2)

import time
import pyautogui


def mouse_click(x,y):
    time.sleep(1)
    pyautogui.click(x,y)
def key_press(char):
     time.sleep(1)
     pyautogui.press(char)

cordinate = open("click_coordinatess.txt",'r')
read = cordinate.readlines()



for line in read :
    
    striped_string = line.strip()
    
    if striped_string.isalpha():
            key_press(striped_string)
    
    else :
        position =line.strip().split(",")
        for values in position :
            x = int(position[0])
            y = int(position[1])
            
    mouse_click(x,y)
cordinate.close()
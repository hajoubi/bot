import pyautogui
import time
def mouse_click(x,y):
    time.sleep(3)
    
    pyautogui.click(x,y)
def key_press(char):
     time.sleep(3)
     pyautogui.press(char)

cordinate = open("click_coordinates.txt",'r')
read = cordinate.readlines()
count = 0
cordinate.close()

for line in read :
    striped_string = line.strip()
    if striped_string.isalpha():
            key_press(striped_string)
    
    else :
        cordination =line.strip().split(",")
        for values in cordination :
             x = cordination[0]
             y = cordination[1]
        mouse_click(x,y)
             

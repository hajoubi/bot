import pynput
from pynput.mouse import Listener
from pynput import keyboard
import time


time.sleep(2)

def on_press(key):
    try:
        with open("click_coordinates.txt", "a") as f:
            f.write((f"{key.char}\n"))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))



def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
        

def on_click(x, y, button, pressed):
   if pressed:
       with open("click_coordinates.txt", "a") as f:
            f.write(f"{x},{y}\n")
       
   

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

with Listener(on_click=on_click) as listener:
   listener.join()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:

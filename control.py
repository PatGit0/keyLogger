import pynput


def controlMouse():
    mouse = pynput.mouse.Controller
    mouse.position = (100,200) 

controlMouse()      
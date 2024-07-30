from pynput.mouse import Controller


def controlMouse():
    mouse = Controller()
    print("posicion actual:",mouse.position)
    mouse.position = (100,200) 
    print("posicion después del cambio",mouse.position)

controlMouse()      
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    print("posicion actual:",mouse.position)
    mouse.position = (100,200) 
    print("posicion después del cambio",mouse.position)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("esto esta bien guapo!!!")

controlKeyboard()      
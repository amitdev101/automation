import pyautogui
import pyperclip
import subprocess
import psutil
import time
import sys
import os
import random
from playsound import playsound

############ GLOBAL VARIABLES ##########################
CMD_NUM = 1

##################### PYINSTALLER SETTINGS ############################

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller 
        PyInstaller creates a temp folder and stores path in _MEIPASS
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
SOUND_DIR = resource_path("sound")
STATIC = resource_path('static')
'''
# now use all path relative to this path sound
# now sound and static folder must be there 
file structure :
    .... main.py
    .... static (dir)
    .... sound (dir)
            . song.mp3 (audio file )

How to use :
    suppose i have a song in sound folder
    so i will use my song path relative to above defined sound folder
    song_file = sound_dir + '\song.mp3'

'''
######################################################################


################# NOTES FOR BUILDING STAND ALONE EXE WITH PYINSTALLER #####################
'''
1. pyi-makespec --onefile main.py
2. now open main.spec file and add your directories (for example i have set all mypath wrt sound directories for sound files)
    ex my_data = [("sound","sound"),
                    ]
3. now set a.data = my_data
4. now run command pyinstaller --onefile main.spec
5. now you have your exe build
'''
#############################################################################################




def play_music_on_windows():
    music_file_path =  SOUND_DIR+"\devil_inside_me.mp3"
    playsound(music_file_path)


def show_desktop():
    pyautogui.hotkey('winleft','d')

def get_all_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid','name'])]
    return processes

def print_all_process():
    processes = [p.info for p in psutil.process_iter(attrs=['pid','name'])]
    for process in processes:
        print(process)

def close_process(process_name):
    print('closing application %s' %(process_name))
    processes = get_all_processes()
    terminate_processes = [p for p in processes if process_name in p.info['name']]
    pid_to_kill = list()
    for process in terminate_processes:
        pid_to_kill.append(process['pid'])
    print(pid_to_kill)
    ########################
    for p in pid_to_kill:
        process = psutil.process(p)
        print(process)
        process.terminate()

def open_app(app_path):
    # if windows replace '\' with '\\'
    print('Starting app ',app_path)
    cmd = 'start ' + app_path
    subprocess.call(cmd,shell=True)
    print(app_path,' is opened')

def focus_on_app(window_title,maximize=True,activate=True):
    winlist = pyautogui.getAllWindows()
    for item in winlist:
        if window_title in item.title:
            if maximize:
                if (not item.maximize()):
                    item.maximize()
            if activate:
                if (not item.isActive):
                    item.activate()

def is_focused(window_title):
    winlist = pyautogui.getAllWindows()
    for win in winlist:
        if window_title in win.title:
            if win.isActive:
                return True
            else:
                return False
def window_exist(window_title):
    winlist = pyautogui.getAllWindows()
    for win in winlist:
        if window_title in win.title:
            return True
    return False

def minimize_window(window_title):
    winlist = pyautogui.getAllWindows()
    for item in winlist:
        if window_title in item.title:
            if (not item.minimize()):
                item.minimize()

def print_all_windows():
    winlist = pyautogui.getAllWindows()
    for win in winlist:
        print(win.title)

def locate(image_list):
    for image in image_list:
        print("searching for ",image)
        for i in pyautogui.locateAllOnScreen(image):
            pyautogui.moveTo(i.left + i.width/2,i.top + i.height/2)
            if len(i)!=0:
                print("found",image)
                x,y = pyautogui.position()
                print('mouse position is ',x,' ',y)
                return 

def locate_until_found(image_list):
    while(True):
        for image in image_list:
            print("searching for ",image)
            for i in pyautogui.locateAllOnScreen(image):
                pyautogui.moveTo(i.left + i.width/2,i.top + i.height/2)
                if len(i)!=0:
                    print("found",image)
                    x,y = pyautogui.position()
                    print('mouse position is ',x,' ',y)
                    return
            

def print_list(mylist):
    for i in range(len(mylist)):
        # print('%s. %s' %(i,mylist[i]))
        print(i,'. ',mylist[i])

def print_mouse_position():
    while True:
        time.sleep(5)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)


def execute_cmd(cmd):
    ''' This function runs a command in shell/Terminal
    input: cmd , type : str
    return type : None

    '''
    global CMD_NUM
    print(CMD_NUM,' ' ,time.ctime(),' Executing cmd ',cmd)
    subprocess.call(cmd,shell=True)
    CMD_NUM+=1


def close_window(win_name):
    '''
    inputs : win_name , type : str 
    output : None 
    This function closes the given app_name window
    '''
    print('Closing window ',win_name)
    winlist = pyautogui.getAllWindows()
    for window in winlist:
        if window.title == win_name:
            window.close()
            print("window closed ")


def move_mouse_random():
    xmin,ymin,xmax,ymax = 10,10,900,900
    from pyautogui import ( easeInQuad,
        easeOutQuad,
        easeInOutQuad,
        easeInCubic,
        easeOutCubic,
        easeInOutCubic,
        easeInQuart,
        easeOutQuart,
        easeInOutQuart,
        easeInQuint,
        easeOutQuint,
        easeInOutQuint,
        easeInSine,
        easeOutSine,
        easeInOutSine,
        easeInExpo,
        easeOutExpo,
        easeInOutExpo,
        easeInCirc,
        easeOutCirc,
        easeInOutCirc,
        easeInElastic,
        easeOutElastic,
        easeInOutElastic,
        easeInBack,
        easeOutBack,
        easeInOutBack,
        easeInBounce,
        easeOutBounce,
        easeInOutBounce,
        )
    tween_list = [ easeInQuad,
        easeOutQuad,
        easeInOutQuad,
        easeInCubic,
        easeOutCubic,
        easeInOutCubic,
        easeInQuart,
        easeOutQuart,
        easeInOutQuart,
        easeInQuint,
        easeOutQuint,
        easeInOutQuint,
        easeInSine,
        easeOutSine,
        easeInOutSine,
        easeInExpo,
        easeOutExpo,
        easeInOutExpo,
        easeInCirc,
        easeOutCirc,
        easeInOutCirc,
        easeInElastic,
        easeOutElastic,
        easeInOutElastic,
        easeInBack,
        easeOutBack,
        easeInOutBack,
        easeInBounce,
        easeOutBounce,
        easeInOutBounce,]
    while(True):
        rand_x = random.randint(xmin,xmax)
        rand_y = random.randint(ymin,ymax)
        duration = random.randint(2,6)
        random_tween_func = tween_list[random.randint(0,len(tween_list)-1)]
        pyautogui.moveTo(rand_x,rand_y,duration=duration,tween=random_tween_func)
        time.sleep(10)
        time.sleep(duration)
        # print(rand_x,rand_y)
        x,y = pyautogui.position()
        print(x,y)

def main():
    print('Inside main ')

if __name__ == "__main__":
    main()
    
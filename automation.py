import pyautogui
import pyperclip
import subprocess
import psutil
import time

def show_desktop():
    pyautogui.hotkey('winleft','d')

def get_all_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid','name'])]
    return processes

def print_all_process():
    processes = [p.info for p in psutil.process_iter(attrs=['pid','name'])]
    for process in processes:
        print(process)

def close_app(name):
    print('closing application %s' %(name))
    processes = get_all_processes()
    terminate_processes = [p for p in processes if name in p.info['name']]
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

def focus_on_app(window_title):
    winlist = pyautogui.getAllWindows()
    for item in winlist:
        if window_title in item.title:
            if not item.maximize():
                item.maximize()
            if not item.isActive:
                item.activate()

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


def main():
    pass


if __name__ == "__main__":
    main()
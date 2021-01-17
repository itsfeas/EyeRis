import numpy as np
import cv2
import pynput
from pynput.keyboard import Key, Controller
from pynput import keyboard
from time import sleep

settings= open('settings.txt','r')
sens = settings.readline().replace('\n',"")
webc = settings.readline().replace('\n',"")
rmode =settings.readline().replace('\n',"")


def realtime(cam_no, show_feed):
    feed = cv2.VideoCapture(cam_no)
    keyboard = Controller()
    input_stopped = 50
    calm = 30
    affirmation = [0,0,0]

    for x in range(100):
        ret, frame = feed.read()
        reference_frame = frame
        reference_frame = resize_frame(frame)
        pause_frame = frame

    busy = 0
    frame_no=0

    while(True):
        ret, frame = feed.read()
        output_frame = frame

        width = feed.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = feed.get(cv2.CAP_PROP_FRAME_HEIGHT)

        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame[2,1]=[0,0,255]
        frame = resize_frame(frame)
        #reference_frame = frame

        scan_yes, input_stopped, affirmation, calm = trigger_track(reference_frame, frame, pause_frame, input_stopped, affirmation, calm, keyboard)

        if scan_yes==0 and frame_no%5==0:
            reference_frame = frame

        if scan_yes==0 and frame_no%70==0:
            pause_frame = frame
            #print("pause_frame updated")
        frame_no+=1

        if input_stopped>1:
            input_stopped-=1
        if input_stopped==1:
            input_stopped-=1
            print("cooldown complete")

        if show_feed==1:
            cv2.namedWindow('EyeRis',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('EyeRis', (int(width),int(height)))
            cv2.imshow('EyeRis',output_frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    feed.release()
    cv2.destroyAllWindows()
"""
def burn_in(reference_frame, frame):
    ave = [0]*3
    for x in range(50):
        for y in range(50):
            for channel in range(3):
                ave[channel] = int((frame[y,x][channel]+reference_frame[y,x][channel])/2)
                reference_frame[y,x][channel] = ave[channel]
    return(reference_frame)
"""

def resize_frame(frame):
    return(cv2.resize(frame, (50,50), interpolation = cv2.INTER_AREA))


def trigger_track(reference_frame, frame, pause_frame, input_stopped, affirmation, calm, keyboard):
    l1, r1 = average_of_color(reference_frame)
    l2, r2 = average_of_color(frame)
    #print(abs(l1 - l2))
    returned_val = 0
    #print(calm, input_stopped, affirmation)

    if input_stopped==0:
        
        if sens == 'low':
            abs_full = 70
            abs_l = 20
            abs_r = 20
        elif sens == 'medium':
            abs_full = 60
            abs_l = 15
            abs_r = 15
        elif sens == 'high':
            abs_full = 50
            abs_l =10
            abs_r = 10        

        if abs(full_average(frame) - full_average(pause_frame))>abs_full:
            affirmation[2]+=1
            calm=0
        elif (abs(l1 - l2))>abs_l:
            affirmation[0]+=1
            calm=0

        elif (abs(r1-r2))>abs_r:
            affirmation[1]+=1
            calm=0
        elif calm>=30:
            affirmation=[0]*3
        else:
            calm+=1


        if affirmation[2]>=3 and rmode == 'media':
            returned_val, input_stopped, calm = ("pause", 150, 0)
            print("paused")
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)
            affirmation = [0]*3
        elif affirmation[1]>=4:
            returned_val, input_stopped, calm = ("R", 71, 0)
            
            if rmode == 'media':
                keyboard.press(Key.media_previous)
                keyboard.release(Key.media_previous)
                print("reverse")
            elif rmode == 'read':
                keyboard.press(Key.page_down)
                keyboard.release(Key.page_down)
                print("page down")

            affirmation = [0]*3
        elif affirmation[0]>=4:
            returned_val, input_stopped, calm = ("L", 71, 0)
            #print("activated left")

            if rmode == 'media':
                keyboard.press(Key.media_next)
                keyboard.release(Key.media_next)
                print("skip")
            elif rmode == 'read':
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
                print("page up")
            affirmation = [0]*3

    return(returned_val, input_stopped, affirmation, calm)

def full_average(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows = np.average(frame, axis=0)
    ave = np.average(rows, axis=0)
    color = int(ave)
    return(color)

def average_of_color(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ave_left = 0
    ave_right = 0

    for x in range(5):
        for y in range(10,50):
            ave_left += (frame[y,x])
            #print(type(frame[y,x]))
    ave_left = int(ave_left/((5)*(50-10)))
    
    #print(ave_left)

    for x in range(44,49):
        for y in range(10,50):
            ave_right += frame[y,x]
    ave_right = int(ave_right/((5)*(50-10)))
    return(ave_left, ave_right)

if __name__ == '__main__':
    realtime(int(webc), 1)
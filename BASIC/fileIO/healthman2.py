import pygame
from pygame import mixer 
from datetime import datetime
from time import time

def musiconloop(file,stopper):#file having music stopper: when we wanna stop
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__=="__main__":
    musiconloop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=5
    eyessecs=20
    exsecs=10

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm. ")
            musiconloop('water.mp3','drank')
            init_water=time()
            log_now("Drank water at")

        if time() - init_eyes > eyessecs:
            print("Water Drinking time. Enter 'done' to stop the alarm. ")
            musiconloop('eyes.mp3','done')
            init_eyes=time()
            log_now("Eyes relaxed at")
        
        if time() - init_exercise > exsecs:
            print("Exercise time. Enter 'done' to stop the alarm. ")
            musiconloop('physical.mp3','done')
            init_exercise=time()
            log_now("Done exercise at")
import pygame
from pygame import mixer 

def musicloop(file,stopper):#file having music stopper: when we wanna stop
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

if __name__=="__main__":
    musiconloop=("water.mp3","stop")


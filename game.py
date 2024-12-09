import pgzrun
import random
from time import time

HEIGHT=600
WIDTH=800

TITLE="Satelites"

satelites=[]
lines=[]
next_satelite=0

total_time=0
end_time=0
start_time=0

number_of_satellites=8

def create_satellites():
    global start_time
    for i in range(number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=random.randint(40,760),random.randint(40,560)
        satellites.append(satellite)
    start_time=time(
        
    )


                                                        
        

        



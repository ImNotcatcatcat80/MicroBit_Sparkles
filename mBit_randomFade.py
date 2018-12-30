from microbit import *
import random
import os

go_gen = True

while True:
    temp_factor = int(temperature() - 20)
    if temp_factor <= -9:
        temp_factor = 0
    if go_gen == True:
        pxx = random.randint(0, 4)
        pxy = random.randint(0, 4)
        display.set_pixel(pxx, pxy, 9)
    for lx in range(0, 5):
        for ly in range(0, 5):
            sleep(10 + temp_factor)
            bri = display.get_pixel(lx, ly)
            if bri > 0:
                bri -= 1
            display.set_pixel(lx, ly, bri)
    if button_a.was_pressed():
        go_gen = not go_gen
    if button_b.was_pressed():
        if button_a.is_pressed():
            display.scroll("t = " + str(temperature()))
        for sx in range(0, 5):
            for sy in range(0, 5):
                display.set_pixel(sx, sy, 9)
        sleep(100)
        
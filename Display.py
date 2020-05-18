import subprocess
import time
from time import sleep


white_path = '/home/pi/Pictures/White.jpeg'
black_path = '/home/pi/Pictures/Black.jpeg'
blue_path = '/home/pi/Pictures/Blue.png'
green_path = '/home/pi/Pictures/Green.png'


def LCD_REG():
    path = white_path

    command = ['display', white_path]
    process = subprocess.Popen(command)


def LCD_COLOURS(bincolor):

    if bincolor == 'Black':
        path = black_path

        command = ['display', black_path]
        process = subprocess.Popen(command)

        time.sleep(2.5)
        process.kill()

    elif bincolor == 'Blue':
        path = black_path

        command = ['display', blue_path]
        process = subprocess.Popen(command)

        time.sleep(2.5)
        process.kill()

    elif bincolor == 'Green':
        path = green_path

        command = ['display', green_path]
        process = subprocess.Popen(command)

        time.sleep(2.5)
        process.kill()
        

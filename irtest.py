import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
    if(GPIO.input(4) == 1):
        print("input is 1 lol xD")
    if(GPIO.input(4) == 0):
        print("input is 0 xdxd")
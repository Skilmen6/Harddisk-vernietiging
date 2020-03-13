import platform
from tkinter import *
from time import sleep
import RPi.GPIO as GPIO
import pifacerelayplus
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

testIR = FALSE
testRelay = FALSE


def test_comp(c):
    if c == 'IR':
        global testIR
        testIR = not testIR
    if c == 'Relay':
        global testRelay
        testRelay = not testRelay


root = Tk()

inputShow = Text(root)

btnIR = Button(
    text="Infrarood test",
    command=test_comp('IR')
)

btnRelay = Button(
    text="Infrarood test",
    command=test_comp('Relay')
)

btnIR.pack(side=LEFT)
btnRelay.pack(side=LEFT)
inputShow.pack(side=RIGHT)
while True:
    while testIR == 1:
        if GPIO.input(4) == 1:
            print('input is 1')
        if GPIO.input(4) == 0:
            print('input is 0')

    while testRelay == 1:
        pfr.relays[0].toggle()
        sleep(2)

    root.update()

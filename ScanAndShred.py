import tkinter as tk
from picamera import PiCamera
from time import sleep


def onkeypress(e):
    if e.keysym == 'Return':
        global HardDiskID
        HardDiskID = inputShow['text']
        take_photo()
        inputShow['text'] = ''

    else:
        inputShow['text'] += e.char


def take_photo():
    global HardDiskID
    camera.start_preview()
    sleep(2)
    camera.capture('hard_disk_drive_storage/%s.png' % HardDiskID)
    camera.stop_preview()


HardDiskID = 'blank'

root = tk.Tk()
camera = PiCamera()
root.attributes('-fullscreen', True)
inputShow = tk.Label(root, height=3, width=50)
inputShow.pack(side=tk.RIGHT)
root.bind('<KeyPress>', onkeypress)

root.mainloop()

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
    sleep(3)
    camera.capture('hard_disk_drive_storage/%s.png' % HardDiskID)
    camera.stop_preview()


HardDiskID = 'blank'

root = tk.Tk()
camera = PiCamera()
root.attributes('-fullscreen', True)
inputShow = tk.Label(root, height=3, width=50)

btnQuit = tk.Button(root,
                    text='QUIT',
                    height=1,
                    width=8,
                    fg='red',
                    font=('Helvetica', '20'),
                    command=quit)

btnCameraTest = tk.Button(root,
                          text='Maak foto',
                          height=1,
                          width=8,
                          fg='blue',
                          font=('Helvetica', '20'),
                          command=take_photo)
inputShow.pack(side=tk.RIGHT)
btnQuit.pack()
btnCameraTest.pack(side=tk.LEFT)
btnQuit.place(relx=1.0, rely=0.0, anchor='ne')
root.bind('<KeyPress>', onkeypress)

root.mainloop()

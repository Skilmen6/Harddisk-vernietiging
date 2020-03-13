import platform
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
import datetime

if platform.system() == 'Linux':
    from picamera import PiCamera
    camera = PiCamera()
else:
    camera = 'undefined'


def onkeypress(e):
    if e.keysym == 'Return':
        global HardDiskID
        HardDiskID = inputShow['text']
        take_photo()
        inputShow['text'] = ''

    else:
        inputShow['text'] += e.char


def take_photo():
    if camera != 'undefined':
        try:
            global HardDiskID
            camera.start_preview()
            sleep(2)
            camera.capture('hard_disk_drive_storage/%s.png' % HardDiskID)
            camera.stop_preview()
        except picamera.exc.PICameraError:
            tkinter.messagebox.showwarning('Geen camera aangesloten', 'je moet de camera aansluiten', icon='warning')
    else:
        tkinter.messagebox.showinfo('foto', 'foto genomen')


def close_window():
    root.destroy()


HardDiskID = '%s: blank' % datetime.datetime.now()

root = Tk()
root.attributes('-fullscreen', True)
imgFrame = Frame(root)
buttonFrame = Frame(root, bg="grey")

img = Image.open("blank.png")
img = img.resize((675, 405), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
inputShow = Label(root, height=3, width=50)

imgPhoto = Label(
    imgFrame,
    image=photoImg
)

btnYes = Button(
    buttonFrame,
    text="Ja",
    width=20,
    height=4,
    bg="green",  # bg = background
    fg="white"  # fg = foreground(text)
)

btnQuit = Button(
    buttonFrame,
    text="Quit",
    fg="red",
    command=close_window
)

btnNo = Button(
    buttonFrame,
    text="Nee",
    width=20,
    height=4,
    bg="red",
    fg="white"
)

imgFrame.pack()
buttonFrame.pack(side=BOTTOM, fill="x")

imgPhoto.pack()
btnYes.pack(side=LEFT, anchor="w")
btnQuit.place(relx=0.5, rely=0.5, anchor="c")
btnNo.pack(side=RIGHT, anchor="e")

inputShow.pack(side=RIGHT)
root.bind('<KeyPress>', onkeypress)

root.mainloop()

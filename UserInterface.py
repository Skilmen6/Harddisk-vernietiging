from tkinter import *
from PIL import Image, ImageTk
from time import sleep
import tkinter.messagebox
#import pifacerelayplus #werkt alleen op Raspberry Pi
root = Tk()

#for testing on Raspberry Pi touch screen
#root.attributes('-fullscreen', True)

#for testing on other screens
root.geometry("800x480")

imgFrame = Frame(root)
buttonFrame = Frame(root)

img = Image.open("blank.png")
img = img.resize((675, 405), Image.ANTIALIAS) 
photoImg = ImageTk.PhotoImage(img)
#pinRelay = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

def close_window():
    MsgBox = tkinter.messagebox.askquestion ('Afsluiten','Weet je zeker dat je het programma wil sluiten?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

#def move_pin():
#    pinRelay.relays[0].toggle() #pin naar beneden
#    sleep(3.0)
#    pinRelay.relays[0].toggle() #pin naar boven


imgPhoto = Label(
    imgFrame, 
    image=photoImg
)

btnYes = Button(
    buttonFrame, 
    text="Ja", 
    width=20, 
    height=4,
    bg="green", #bg = background
    fg="white", #fg = foreground(text)
    #command=move_pin
)

btnQuit = Button(
    buttonFrame,
    text="Quit",
    fg="red",
    width=10, 
    height=2,
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
btnQuit.place(relx=0.5, rely=1, anchor="s")
btnNo.pack(side=RIGHT, anchor="e")

root.mainloop()

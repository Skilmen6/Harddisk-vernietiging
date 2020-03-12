from tkinter import *
from PIL import Image, ImageTk
root = Tk()

#for testing on Raspberry Pi
root.attributes('-fullscreen', True)

#for testing on Windows
#root.geometry("800x480")

imgFrame = Frame(root)
buttonFrame = Frame(root, bg="grey")

img = Image.open("blank.png")
img = img.resize((675, 405), Image.ANTIALIAS) 
photoImg = ImageTk.PhotoImage(img) 

def close_window(): 
    root.destroy()


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
    fg="white" #fg = foreground(text)
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

root.mainloop()

from tkinter import *
root = Tk()
root.geometry("800x480")

imgFrame = Frame(root)
buttonFrame = Frame(root, bg="grey")

photoImg = PhotoImage( file="forest.png") #jpg is not supported
photoImg = photoImg.subsample(3, 3)

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
    fg="red"
)

btnNo = Button(
    buttonFrame, 
    text="Nee", 
    width=20, 
    height=4,
    bg="red",
    fg="white"
)

imgFrame.pack(padx=20, pady=20)
buttonFrame.pack(side=BOTTOM, fill="x")

imgPhoto.pack()
btnYes.pack(side=LEFT, anchor="w")
btnQuit.place(relx=0.5)
btnNo.pack(side=RIGHT, anchor="e")

root.mainloop()

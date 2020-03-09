import tkinter as tk

def write_slogan():
    print("Tkinter tests")

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, )) 

root = tk.Tk()
root.attributes('-fullscreen' , True)
text = tk.Text(root)

button = tk.Button(root, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
text.pack(side=tk.RIGHT)
button.pack(side=tk.LEFT)
slogan = tk.Button(root,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)
root.bind('<KeyPress>', onKeyPress)

root.mainloop()
import tkinter as tk


def onkeypress(e):
    if e.keysym == 'Return':
        inputShow['text'] = ''
    else:
        inputShow['text'] += e.char


root = tk.Tk()
root.attributes('-fullscreen', True)
inputShow = tk.Label(root, height=3, width=50)

btnQuit = tk.Button(root,
                    text='QUIT',
                    height=1,
                    width=8,
                    fg='red',
                    font=('Helvetica', '20'),
                    command=quit)
inputShow.pack(side=tk.RIGHT)
btnQuit.pack()
btnQuit.place(relx=1.0, rely=0.0, anchor='ne')
root.bind('<KeyPress>', onkeypress)

root.mainloop()

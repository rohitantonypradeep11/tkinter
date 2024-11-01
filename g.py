from tkinter import *
window = Tk()
window.geometry("1000x1000")
for i in range(3):
    for j in range(3):
        frame = Frame(master = window,relief = RAISED,borderwidth = 1)
        frame.grid(row = i,column = j,padx = 10,pady = 10)
        label = Label(master = frame,text = f"row {i}\ncolum {j}",height = 10,width = 10)
        label.pack()
window.mainloop()
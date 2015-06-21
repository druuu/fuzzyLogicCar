from Tkinter import *

root = Tk()

def next_image(event):
    canvas1.move(item, 10, 0) # <--- Use Canvas.move method.

image1 = r"car.gif"
photo1 = PhotoImage(file=image1)
width1 = 500
height1 = 400
canvas1 = Canvas(width=width1, height=height1)
canvas1.pack(expand=1, fill=BOTH) # <--- Make your canvas expandable.
x = (width1)/2.0
y = (height1)/2.0
item = canvas1.create_image(x, y, image=photo1) # <--- Save the return value of the create_* method.
canvas1.bind('<Button-1>', next_image)
gg = 'aaaaaa'
root.mainloop()

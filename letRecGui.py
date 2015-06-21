from Tkinter import *
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT
import subprocess

from PIL import Image, ImageDraw, ImageTk

b1 = "up"
xold, yold = None, None
white = (255, 255, 255)
black = (0, 0, 0)
width = 400
height = 400
center = height/2

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Layout Test")
        self.config(bg = '#F0F0F0')
        self.grid()

        self.canvas1 = Canvas(self, relief = FLAT, background = "#33B5E0",
                                            width = 400, height = 600)
        self.canvas1.grid(row = 2, column = 2)

        self.canvas1.bind("<Motion>", self.motion)
        self.canvas1.bind("<ButtonPress-1>", self.b1down)
        self.canvas1.bind("<ButtonRelease-1>", self.b1up)


        self.imagePil = Image.open('car.gif')
        self.imagePil = self.imagePil.rotate(45).show()
        self.photo1 = ImageTk.PhotoImage(self.imagePil)
        self.width1 = 500
        self.height1 = 400
        self.x = (self.width1)/2.0
        self.y = (self.height1)/2.0
        self.item = self.canvas1.create_image(self.x, self.y, image=self.photo1)
        self.canvas1.move(self.item, 100, 0)
        #self.submit = Button(self, text = "Submit", command = self.submitImg)
        #self.submit.configure(activebackground = "#33B5E5", relief = FLAT)
        #self.submit.grid()

        #self.clearCanvas = Button(self, text = "Clear", command =
        #        self.clearCanvasFun)
        #self.clearCanvas.configure(activebackground = "#33B5E0", relief = FLAT)
        #self.clearCanvas.grid()

        #self.drawL = Label(self.canvas1, text='Draw a capital letter',
        #        fg='white', bg='black')
        #self.drawL.configure(activebackground = "#33B5E5", relief = FLAT)
        #labelWindow = self.canvas1.create_window(10, 10, anchor=NW,
        #        window=self.drawL)
        #self.drawL.grid()
        #self.canvas1.create_window(10, 10, anchor = NW, window=self.drawL)

        #add quit button
        #button1 = Button(self, text = "Quit", command = self.quit, anchor = W)
        #button1.configure(width = 10, activebackground = "#33B5E5", relief =
        #        FLAT)
        #button1_window = self.canvas1.create_window(10, 10, anchor=NW,
        #        window=button1)
        #button1.grid()

        self.image1 = Image.new("RGB", (400, 400), black)
        self.draw = ImageDraw.Draw(self.image1)
        self.filename = "my_drawing.jpg"


    def b1up(self, event):
        global b1, xold, yold
        b1 = "up"
        xold = None           
        yold = None

    def b1down(self, event):
        global b1
        b1 = "down"

    def motion(self, event):
        if b1 == "down":
            global xold, yold
            if xold is not None and yold is not None:
                event.widget.create_line(xold ,yold ,event.x ,event.y,
                         width = 4, fill = 'white')
                self.draw.line([xold,yold,event.x,event.y], white, width = 4)
            xold = event.x
            yold = event.y

        self.canvas1.update()
        self.image1.save(self.filename)

    def clearCanvasFun(self):
        self.canvas1.delete('all')

    def submitImg(self):
        subprocess.call('./letRec.sh')
        alphaList = []
        alphaFile = open('result.txt', 'r')
        for line in alphaFile:
            line = line.replace('\n', '')
            alphaList.append(line)

        letters = '8ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        predAlpha = letters[int(alphaList[3])]
        self.drawL = Label(self, width = 20, height = 2, text= 'Predicted letter is: ' + predAlpha, fg='white', bg='black')
        self.drawL.configure(activebackground = "#33B5E5", relief = FLAT)
        self.drawL.grid()




def main():
    root = Tk()
    root.geometry('600x600')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()

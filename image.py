from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

""" imagen = Image.open('cascada.jpg')
imagen.show() """

img = ImageTk.PhotoImage(Image.open('cascada.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()
from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('400x400')

l = Label(root, text='Hola mundo')
def click():
    l.pack()

btn = Button(root, text="clickeame", command=click, fg='#ffff00', bg='blue')
btn.pack()

root.mainloop()
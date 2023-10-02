from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('300x100')

exit = Button(root, text='Salir', command=root.quit)
exit.pack()

root.mainloop()
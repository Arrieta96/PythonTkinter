from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')
root.geometry('300x100')


""" def click():
    messagebox.showwarning('Popup', 'Hola mundo') """
""" def click():
    messagebox.showinfo('Popup', 'Hola mundo') """
""" def click():
    messagebox.showerror('Popup', 'Hola mundo')   """
""" def click():
    respuesta = messagebox.askquestion('Popup', 'Hola mundo')     
    if respuesta == 'yes':
        messagebox.showinfo('Respuesta', 'la respuesta fuer: ' + respuesta)
    else:
        messagebox.showinfo('Respuesta', 'la respuesta fuer: ' + respuesta) """
""" def click():
    respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar accion?')
    if respuesta:
        messagebox.showinfo('Respuesta', 'la respuesta fue OK')
    else:
        messagebox.showinfo('Respuesta', 'la respuesta fue cancelar') """
def click():
    respuesta = messagebox.askyesno('Hola mundo', 'Desea realizar accion?')
    if respuesta:
        messagebox.showinfo('Respuesta', 'la respuesta fue Yes')
    else:
        messagebox.showinfo('Respuesta', 'la respuesta fue No')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
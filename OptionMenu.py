from tkinter import *

root = Tk()
root.title('Hola mundo: Option Menu')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Chanchito feliz', 
    'Chanchito triste', 
    'Chanchito emocionado'
]

value = StringVar()
value.set(lista[1])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
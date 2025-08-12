from tkinter import *
import wikipedia

root = Tk()
root.title('aaa')
root.geometry('300x250')

label = Label(wikipedia.summary())  # создаем текстовую метку
label.pack()  # размещаем метку в окне)

root.mainloop()
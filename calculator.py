from tkinter import *

class App:
    def __init__(self, master):
        window.title("Calculator")      #jak se bude nase okno jmenovat
        window.configure(background = "lightgrey")      #nastaveni pozadi okna
        

window = Tk()
app = App(window)
window.mainloop()       #mainloop znaci, ze okno se bude zobrazovat, dokud se nezavre
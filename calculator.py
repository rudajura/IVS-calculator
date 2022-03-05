from tkinter import *

class App:
    def __init__(self, master):
        window.title("Calculator")      #jak se bude nase okno jmenovat
        window.geometry("400x400")
        window.configure(background = "lightgrey")      #nastaveni pozadi okna

        Button(window, text = "9", fg = "black", width = 2, height = 2) .grid(row = 0, column = 2, sticky = W)
        Button(window, text = "8", fg = "black", width = 2, height = 2) .grid(row = 0, column = 1, sticky = W)
        Button(window, text = "7", fg = "black", width = 2, height = 2) .grid(row = 0, column = 0, sticky = W)
        Button(window, text = "6", fg = "black", width = 2, height = 2) .grid(row = 1, column = 2, sticky = W)
        Button(window, text = "5", fg = "black", width = 2, height = 2) .grid(row = 1, column = 1, sticky = W)
        Button(window, text = "4", fg = "black", width = 2, height = 2) .grid(row = 1, column = 0, sticky = W)
        Button(window, text = "3", fg = "black", width = 2, height = 2) .grid(row = 2, column = 2, sticky = W)
        Button(window, text = "2", fg = "black", width = 2, height = 2) .grid(row = 2, column = 1, sticky = W)
        Button(window, text = "1", fg = "black", width = 2, height = 2) .grid(row = 2, column = 0, sticky = W)
        Button(window, text = "0", fg = "black", width = 2, height = 2) .grid(row = 3, column = 0, sticky = W)
        Button(window, text = ",", fg = "black", width = 2, height = 2) .grid(row = 3, column = 1, sticky = W)
        Button(window, text = "%", fg = "black", width = 2, height = 2) .grid(row = 3, column = 2, sticky = W)



window = Tk()
app = App(window)
window.mainloop()       #mainloop znaci, ze okno se bude zobrazovat, dokud se nezavre
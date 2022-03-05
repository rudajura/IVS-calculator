from tkinter import *


character = ""      #prazdny retezec, budou se do nej dosazovat cislice a s nimi pak pocitat
class App:
    def __init__(self, master):
        window.title("Calculator")      #jak se bude nase okno jmenovat
        window.geometry("400x400")
        window.resizable(0, 0)
        window.configure(background = "lightgrey")      #nastaveni pozadi okna

        number = StringVar()
        
        #prvni kolonka pro vkladani cisel
        vcmd = (master.register(self.valid))
        entry = Entry(window, width = 20, font = ('none 24'), bg = "white", textvar = number, validatecommand = (vcmd, '%P'), insertontime = 0)
        entry.pack()
        entry.focus_set()

        #funkce na nacitani a zobrazovani vstupu kliknutim na tlacitko s cislem
        def load_input(input_num):
            global character
            character = character + str(input_num)
            number.set(character)
            position = entry.index(INSERT)
            entry.icursor(position + 1)

        #druha kolonka pro vypisovani vysledku, nelze do ni zapisovat
        result = Text(window, width = 25, height = 1, font = ('none 19'), bg = "white")
        result.configure(state = "disabled")
        result.pack()

        #jednotliva tlacitka
        but_9 = Button(window, text = "9", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(9)) .place(x = 90, y = 82)
        but_8 = Button(window, text = "8", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(8)) .place(x = 45, y = 82)
        but_7 = Button(window, text = "7", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(7)) .place(x = 0, y = 82)
        but_6 = Button(window, text = "6", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(6)) .place(x = 90, y = 131)
        but_5 = Button(window, text = "5", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(5)) .place(x = 45, y = 131)
        but_4 = Button(window, text = "4", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(4)) .place(x = 0, y = 131)
        but_3 = Button(window, text = "3", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(3)) .place(x = 90, y = 180)
        but_2 = Button(window, text = "2", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(2)) .place(x = 45, y = 180)
        but_1 = Button(window, text = "1", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(1)) .place(x = 0, y = 180)
        but_0 = Button(window, text = "0", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(0)) .place(x = 0, y = 229)
        but_dot = Button(window, text = ",", fg = "black", width = 2, height = 2, command = lambda:load_input(',')) .place(x = 45, y = 229)
        but_fact = Button(window, text = "!", fg = "black", width = 2, height = 2) .place(x = 90, y = 229)
        but_div = Button(window, text = "/", fg = "black", width = 2, height = 2, command = lambda:load_input('/')) .place(x = 135, y = 82)
        but_mul = Button(window, text = "*", fg = "black", width = 2, height = 2, command = lambda:load_input('*')) .place(x = 135, y = 131)
        but_minus = Button(window, text = "-", fg = "black", width = 2, height = 2, command = lambda:load_input('-')) .place(x = 135, y = 180)
        but_plus = Button(window, text = "+", fg = "black", width = 2, height = 2, command = lambda:load_input('+')) .place(x = 135, y = 229)
        but_random = Button(window, text = "", fg = "black", width = 2, height = 2) .place(x = 180, y = 82)
        but_backsp = Button(window, text = "<-", fg = "black", width = 2, height = 2) .place(x = 225, y = 82)
        but_lbrack = Button(window, text = "(", fg = "black", width = 2, height = 2) .place(x = 180, y = 131)
        but_rbrack = Button(window, text = ")", fg = "black", width = 2, height = 2) .place(x = 225, y = 131)
        but_pow = Button(window, text = "", fg = "black", width = 2, height = 2) .place(x = 180, y = 180)
        but_sqrt = Button(window, text = "", fg = "black", width = 2, height = 2) .place(x = 225, y = 180)
        but_res = Button(window, text = "=", fg = "white", bg = "green", width = 7, height = 2) .place(x = 183, y = 229)

    #funkce pouze pro kontrolu, zda se vkladaji pouze cisla (jine znaky nevypise)
    def valid(self, P):
        if str.isdigit(P) or P == "" or P == "," or P == "*" or P == "/" or P == "-" or P == "!" or P == "+":
            return True
        else:
            return False


window = Tk()
app = App(window)
window.mainloop()       #mainloop znaci, ze okno se bude zobrazovat, dokud se nezavre
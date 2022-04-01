from tkinter import *       #naimportuje vsechno z knihovny tkinter

#TODO:
#nacitani vstupu z klavesnice
#funkce mocnina, odmocnina, faktorial

#prazdny retezec, budou se do nej dosazovat cislice a s nimi pak pocitat
character = ""

#funkce na nacitani cisel a operatoru , ukladaji se do promenne character
def load_input(input_num):
    global character
    character = character + str(input_num)
    number.set(character)
    position = entry.index(INSERT)
    entry.icursor(position + 1)

#funkce, ktera se zavola pri stisknuti tlacitka "="
#zobrazi vysledek prikladu, a nasledne zresetuje pole pro vkladani cisel
#vetev "try" se vykona, pokud v priklade neni zadna chyba (napriklad dvakrat minus, deleni nulou atd.)
#pokud je tam chyba, provede se vetev "except" a vypise se chybova hlaska
def result_foo():
    try:
        global character
        total = str(eval(character))
        number.set(total)
        character = ""
    except:
        number.set("chyba v zadani")
        character = ""

#stejna funkce jako result_foo, akorat se vola, kdyz je stisknuta klavesa enter
def result_enter(entry):
    global character
    total = str(eval(character))
    number.set(total)
    character = ""

#odstrani posledni znak z prikladu (cisla)
def backspace():
    global character
    character = character[:-1]
    number.set(character)
    position = entry.index(INSERT)
    entry.icursor(position + 1)

#odstrani cely priklad
def clear():
    global character
    character = ""
    number.set(character)


##################             MAINLOOP             ######################
#pocatecni inicializace kalkulacky spolu s vykreslenim gui, spusti se
#hned pri spusteni programu
if __name__ == "__main__":

    #window bude oznacovat okno, ve kterem se bude vsechno zobrazovat
    window = Tk()

    #nastaveni parametru, se kterymi se bude kalkulacka (okno) vykreslovat
    window.title("Calculator")
    window.geometry("400x400")
    window.resizable(0, 0)
    window.configure(background = "lightgrey")

    #number bude promenna, ktera bude zobrazovat zadavane znaky
    number = StringVar()

    #prvni kolonka pro vkladani cisel a zobrazeni vysledku
    entry = Entry(window, width = 20, font = ('none 24'), bg = "white", textvar = number, insertontime = 0)
    entry.pack()
    entry.focus_set()

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
    but_dot = Button(window, text = ".", fg = "black", width = 2, height = 2, command = lambda:load_input('.')) .place(x = 45, y = 229)
    but_fact = Button(window, text = "!", fg = "black", width = 2, height = 2) .place(x = 90, y = 229)
    but_div = Button(window, text = "/", fg = "black", width = 2, height = 2, command = lambda:load_input('/')) .place(x = 135, y = 82)
    but_mul = Button(window, text = "*", fg = "black", width = 2, height = 2, command = lambda:load_input('*')) .place(x = 135, y = 131)
    but_minus = Button(window, text = "-", fg = "black", width = 2, height = 2, command = lambda:load_input('-')) .place(x = 135, y = 180)
    but_plus = Button(window, text = "+", fg = "black", width = 2, height = 2, command = lambda:load_input('+')) .place(x = 135, y = 229)
    but_clear = Button(window, text = "C", fg = "black", width = 2, height = 2, command = clear) .place(x = 180, y = 82)
    but_backsp = Button(window, text = "<-", fg = "black", width = 2, height = 2, command = backspace) .place(x = 225, y = 82)
    but_lbrack = Button(window, text = "(", fg = "black", width = 2, height = 2, command = lambda:load_input('(')) .place(x = 180, y = 131)
    but_rbrack = Button(window, text = ")", fg = "black", width = 2, height = 2, command = lambda:load_input(')')) .place(x = 225, y = 131)
    but_pow = Button(window, text = "", fg = "black", width = 2, height = 2) .place(x = 180, y = 180)
    but_sqrt = Button(window, text = "", fg = "black", width = 2, height = 2) .place(x = 225, y = 180)
    but_res = Button(window, text = "=", fg = "white", bg = "green", width = 6, height = 2, command = result_foo) .place(x = 183, y = 229)

    #lze pouzit enter pro zobrazeni vysledku, ale jen pokud byl priklad zadan mysi
    window.bind('<Return>', result_enter)

    #mainloop, ve kterem se bude vykreslovat kalkulacka
    window.mainloop()
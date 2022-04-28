from tkinter import *       #naimportuje vsechno z knihovny tkinter

#TODO:
#nacitani vstupu z klavesnice

#prazdny retezec, budou se do nej dosazovat cislice a s nimi pak pocitat
character = ""

#promenna, ktera je 1, pokud bylo vybrano pocitani odmocniny 
if_sqrt = 0
#do sqrt_var se nahraje retezec character v pripade vybrani pocitani odmocniny
sqrt_var = ""
#pokud bylo tlacitko "help" stisknuto, if_help se zmeni na 1 a zobrazi se napoveda
#pokud se stiskne "help" podruhe, if_help se zmeni na 0 a napoveda se skryje
if_help = 0

#funkce na nacitani cisel a operatoru , ukladaji se do promenne character
def load_input(input_num):
    global character
    global if_sqrt
    global sqrt_var
    if if_sqrt == 1:
        sqrt_var = sqrt_var + str(input_num)
        length = len(character) - 1
        character = character[:length] + str(input_num) + character[length:]
        number.set(character)
    else:   
        character = character + str(input_num)
        number.set(character)
        position = entry.index(INSERT)
        entry.icursor(position + 1)

#funkce, ktera se zavola pri stisknuti tlacitka "="
#zobrazi vysledek prikladu, a nasledne zresetuje pole pro vkladani cisel
#vetev "try" se vykona, pokud v priklade neni zadna chyba (napriklad dvakrat minus, deleni nulou atd.)
#pokud je tam chyba, provede se vetev "except" a vypise se chybova hlaska
def res(character):
    try:
        return str(eval(character))
    except:
        return "ERROR"
    
def sqrt_total(sqrt_var):
    sqrt_var = sqrt_var + ")"
    return str(eval(sqrt_var))

def catch_exeption(total):
    global character
    global if_sqrt
    if total == "ERROR":
        number.set("chyba v zadání")
        character = ""
        if_sqrt = 0
    else: 
        number.set(total)
        character = ""
        if_sqrt = 0

def result_foo():

    global sqrt_var
    global character
    global if_sqrt
    if if_sqrt == 1:
        total = sqrt_total(sqrt_var)
        catch_exeption(total)
    else:
        total = res(character)
        catch_exeption(total)

#stejna funkce jako result_foo, akorat se vola, kdyz je stisknuta klavesa enter
def result_enter(entry):
    global sqrt_var
    global character
    global if_sqrt
    if if_sqrt == 1:
        total = sqrt_total(sqrt_var)
        catch_exeption(total)
    else:
        total = res(character)
        catch_exeption(total)

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

#funkce na faktorial - pri stisknuti tlacitka "!" se okamzite spocita faktorial a vypise na obrazovku
def factorial(total):
    if total < 0:
        return "ERROR"
    elif total == 0:
        return 1
    else :
        fact = 1
        for i in range(1, total + 1):
            fact = fact * i
    return fact

def factorial_set():
    global character
    if character.isdigit(): 
        total = factorial(int(character))
        if total == "ERROR":
            number.set("chyba v zadání")
            character = ""
        elif total == 1:
            number.set(1)
            character = ""
        else :
            number.set(total)
            character = ""
    else:
        number.set("chyba v zadání")
        character = ""

#funkce pro vypsani odmocniny
def square_root():
    global character
    global sqrt_var
    global if_sqrt
    if_sqrt = 1
    number.set(character+str("\u221A()"))
    sqrt_var = character + str("**(1/")
    character = character + str("\u221A()")

def show_help():
    global if_help
    if if_help == 0:
        window.resizable(width=False, height=False)
        window.geometry("883x446")
        if_help = 1
    else:
        window.resizable(width=False, height=False)
        window.geometry("360x340")
        if_help = 0

help_msg ='''
                Nápověda:

-příklady vytvářejte primárně pomocí tlačítek
 zobrazenými v kalkulačce
-alternativně lze místo tlačítka "=" použít
 klávesu ENTER
-v případě nesprávného zadání kalkulačka 
 vypíše zprávu "chyba v zadání"
-faktoriál: zadejte číslo, kterého chcete 
 vypočítat faktoriál, a stiskněte "!" - ihned
 se zobrazí výsledek
-mocnina: nejdříve zadejte základ mocniny
(mocněnec), dále tlačítko "^", a nakonec exponent
-odmocnina: nejdříve zadejte odmocněnce (číslo 
 pod odmocninou), tlačítko \u221A a nakonec zadejte
 odmocnitele
 '''



##################             MAINLOOP             ######################
#pocatecni inicializace kalkulacky spolu s vykreslenim gui, spusti se
#hned pri spusteni programu
if __name__ == "__main__":

    #window bude oznacovat okno, ve kterem se bude vsechno zobrazovat
    window = Tk()

    #nastaveni parametru, se kterymi se bude kalkulacka (okno) vykreslovat
    window.title("Calculator")
    window.geometry("360x340")
    window.resizable(0, 0)
    window.configure(background = "lightgrey")

    #number bude promenna, ktera bude zobrazovat zadavane znaky
    number = StringVar()

    #prvni kolonka pro vkladani cisel a zobrazeni vysledku
    entry = Entry(window, width = 13, font = ('none 24'), bg = "white", textvar = number, insertontime = 0)
    entry.place(x = 10, y = 0)
    entry.focus_set()

    help_display = Label(window, text = help_msg,
                   font=('none',12),
                   bg='grey',fg='black', justify = LEFT)
 
    help_display.place(x = 360, y = 5)

    #jednotliva tlacitka
    but_9 = Button(window, text = "9", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(9)) .place(x = 30 + 90, y = 82)
    but_8 = Button(window, text = "8", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(8)) .place(x = 30 + 45, y = 82)
    but_7 = Button(window, text = "7", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(7)) .place(x = 30 + 0, y = 82)
    but_6 = Button(window, text = "6", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(6)) .place(x = 30 + 90, y = 131)
    but_5 = Button(window, text = "5", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(5)) .place(x = 30 + 45, y = 131)
    but_4 = Button(window, text = "4", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(4)) .place(x = 30 + 0, y = 131)
    but_3 = Button(window, text = "3", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(3)) .place(x = 30 + 90, y = 180)
    but_2 = Button(window, text = "2", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(2)) .place(x = 30 + 45, y = 180)
    but_1 = Button(window, text = "1", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(1)) .place(x = 30 + 0, y = 180)
    but_0 = Button(window, text = "0", fg = "white", bg = "grey", width = 2, height = 2, command = lambda:load_input(0)) .place(x = 30 + 0, y = 231)
    but_dot = Button(window, text = ".", fg = "black", width = 2, height = 2, command = lambda:load_input('.')) .place(x = 30 + 49, y = 231)
    but_fact = Button(window, text = "!", fg = "black", width = 2, height = 2, command = factorial_set) .place(x = 30 + 94, y = 231)
    but_div = Button(window, text = "/", fg = "black", width = 2, height = 2, command = lambda:load_input('/')) .place(x = 30 + 138, y = 82)
    but_mul = Button(window, text = "*", fg = "black", width = 2, height = 2, command = lambda:load_input('*')) .place(x = 30 + 138, y = 131)
    but_minus = Button(window, text = "-", fg = "black", width = 2, height = 2, command = lambda:load_input('-')) .place(x = 30 + 138, y = 180)
    but_plus = Button(window, text = "+", fg = "black", width = 2, height = 2, command = lambda:load_input('+')) .place(x = 30 + 138, y = 231)
    but_clear = Button(window, text = "C", fg = "black", width = 2, height = 2, command = clear) .place(x = 30 + 180, y = 82)
    but_backsp = Button(window, text = "<-", fg = "black", width = 2, height = 2, command = backspace) .place(x = 30 + 225, y = 82)
    but_lbrack = Button(window, text = "(", fg = "black", width = 2, height = 2, command = lambda:load_input('(')) .place(x = 30 + 180, y = 131)
    but_rbrack = Button(window, text = ")", fg = "black", width = 2, height = 2, command = lambda:load_input(')')) .place(x = 30 + 225, y = 131)
    but_sqr = Button(window, text = "^", fg = "black", width = 2, height = 2, command = lambda:load_input('**')) .place(x = 30 + 180, y = 180)
    but_sqrt = Button(window, text = "\u221A", fg = "black", width = 2, height = 2, command = square_root) .place(x = 30 + 225, y = 180)
    but_help = Button(window, text = "help", fg = "black", width = 2, height = 2, command = show_help) .place(x = 30 + 180, y = 231)
    but_res = Button(window, text = "=", fg = "white", bg = "green", width = 2, height = 2, command = result_foo) .place(x = 30 + 225, y = 231)

    #lze pouzit enter pro zobrazeni vysledku, ale jen pokud byl priklad zadan mysi
    #v tkinteru se enter znaci jako "Return"
    window.bind('<Return>', result_enter)

    #mainloop, ve kterem se bude vykreslovat kalkulacka
    window.mainloop()
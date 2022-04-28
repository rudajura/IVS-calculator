################################################
#IVS Projekt 2 - Kalkulačka
#autor: Rudolf Jurišica
#Email: xjuris02@stud.fit.vutbr.cz
#Datum poslední změny: 22.4.2022
################################################

##
# @file calculator.py
# @author Rudolf Jurisica
# @brief Kalkulacka, pocita zakladni i pokrocilejsi operace


from tkinter import *       #naimportuje vsechno z knihovny tkinter
import math

##prazdny retezec, budou se do nej dosazovat cislice a s nimi pak pocitat
character = ""

##promenna, ktera je 1, pokud bylo vybrano pocitani odmocniny 
if_sqrt = 0
##do sqrt_var se nahraje retezec character v pripade vybrani pocitani odmocniny
sqrt_var = ""
##pokud bylo tlacitko "help" stisknuto, if_help se zmeni na 1 a zobrazi se napoveda
#pokud se stiskne "help" podruhe, if_help se zmeni na 0 a napoveda se skryje
if_help = 0

##funkce na nacitani cisel a operatoru , ukladaji se do promenne character
# @param input_num promenna obsahujici charakter (cislo) ze vstupu od uzivatele
# @return funkce nic nevraci, pouze prepisuje globalni promenne
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

##funkce, ktera se zavola pri stisknuti tlacitka "="
#zobrazi vysledek prikladu, a nasledne zresetuje pole pro vkladani cisel
#vetev "try" se vykona, pokud v priklade neni zadna chyba (napriklad dvakrat minus, deleni nulou atd.)
#pokud je tam chyba, provede se vetev "except" a vypise se chybova hlaska
# @param num promenna num funguje jako boolean - pokud se zadava vstup z klavenice, je num 0, jinak je 1
# @return vraci vysledek po odmocneni, pokud je v zapise chyba, vraci "ERROR"    
def sqrt_total(num):
    global character
    global sqrt_var
    try:
        if num == 0:
            sqrt_ret = eval(number.get() + str(")"))
            return str(sqrt_ret)
        else:
            sqrt_var = sqrt_var + ")"
            return str(eval(sqrt_var))
    except:
        return "ERROR"

##funkce catch_exeption se vola vzdy po vyhodnoceni vysledku 
# @param total pokud je v total ulozeno "ERROR", vypise se chybova hlaska; jinak se vypise vysledek
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

##funkce res se vola pro vyhodnoceni vysledku (pokud neni zavolana odmocnina)
# @param character promenna, do ktere je ulozen cely retezec obsahujici priklad
# @return vraci vyhodnoceny priklad (neboli vysledek), pokud v priklade byla chyba, vraci "ERROR"
def res(character):
    try:
        if character == "":     #pokud se zadava z klavesnice, jde se touto vetvi
            character = eval(number.get())
            if(character == -0.0):
                character = character + 0.0
            return str(character)
        else:
            character = eval(character)
            if(character == -0.0):
                character = character + 0.0
            return str(character)
    except:
        return "ERROR"

##funkce result_foo se vola, aby se vypocital vysledek - nejdrive se roztridi, zda je zadana odmocnina, nebo ne
#potom se zavolaji prislusne funkce - bud res, nebo sqrt_total
#nasledne nastavi okno v kalkulacce a pripravi se na zadavani dalsiho prikladu
def result_foo():
    global sqrt_var
    global character
    global if_sqrt
    if if_sqrt == 1:
        if character == "":
            total = sqrt_total(0)
            catch_exeption(total)
            if_sqrt = 0
            character = total
        else:
            total = sqrt_total(1)
            catch_exeption(total)
            if_sqrt = 0
            character = total
    else:
            total = res(character)
            catch_exeption(total)
            character = total

##stejna funkce jako result_foo, akorat se vola, kdyz je stisknuta klavesa enter
# @param entry bere stisk klavesnice (v nasem pripade pouze enter)
def result_enter(entry):
    global sqrt_var
    global character
    global if_sqrt
    if if_sqrt == 1:
        if character == "":
            total = sqrt_total(0)
            catch_exeption(total)
            if_sqrt = 0
            character = total
        else:
            total = sqrt_total(1)
            catch_exeption(total)
            if_sqrt = 0
            character = total
    else:
        if character == "":
            total = res(character)
            catch_exeption(total)
            character = total
        else:
            total = res(character)
            catch_exeption(character)
            character = total

##odstrani posledni znak z prikladu (cisla)
def backspace():
    global character
    character = character[:-1]
    number.set(character)
    position = entry.index(INSERT)
    entry.icursor(position + 1)

##odstrani cely priklad
def clear():
    global character
    character = ""
    number.set(character)

##funkce na faktorial - pri stisknuti tlacitka "!" se okamzite spocita faktorial a vypise na obrazovku
# @param total cislo, ktereho faktorial se ma pocitat
# @return vraci error, pokud je total zaporne cislo, nebo 1, pokud ne total 0, jinak vypocitany faktorial
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

##funkce na vypocet faktorialu, pro jeho vypocet se zavola funkce factorial(total)
def factorial_set():
    global character
    tmp_var = number.get()
    if tmp_var.isdigit(): 
        total = factorial(int(tmp_var))
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

##funkce pro vypsani odmocniny
def square_root():
    global character
    global sqrt_var
    global if_sqrt
    #pokud je promenna character prazdna, znamena to, ze se zadava vstup z klavesnice
    if character == "":
        if_sqrt = 1
        number.set(number.get() + str("**(1/"))
        position = entry.index(INSERT)
        entry.icursor(position + 5)
    else:
        if_sqrt = 1
        number.set(character+str("\u221A()"))   #na obrazovku se nastavi symbol odmocniny
        sqrt_var = character + str("**(1/")     #ale do promenne, ktera obsahuje priklad, se ulozi **(1/
        character = character + str("\u221A()")

##funkce na zobrazeni okna s napovedou
#funkce akorat zmeni velikost okna, jinak nic nemeni
def show_help():
    global if_help
    if if_help == 0:
        window.resizable(width=False, height=False)
        window.geometry("894x588")
        if_help = 1
    else:
        window.resizable(width=False, height=False)
        window.geometry("360x340")
        if_help = 0

##zprava, ktera se zobrazi pri stisknuti tlacitka napoveda
help_msg ='''              Nápověda: 

-příklady pište pouze klávesnicí nebo pouze 
 vyobrazenými tlačítky v rozhraní kalkulačky
 (kromě funkcí faktorial, odmocnina a rovná se
 (neboli výsledek) nikdy klávesnici a tlačítka
 nekombinujte)
-pokud zadáváte příklad pomocí klávesnice
 a zobrazí se vám chybová hláška "chyba v zadání",
 zmáčkněte tlačítko "C" a můžete zadat nový příklad
-alternativně lze místo tlačítka "=" použít
 klávesu ENTER
-v případě nesprávného zadání kalkulačka 
 vypíše zprávu "chyba v zadání"
-faktoriál: zadejte číslo, kterého chcete 
 vypočítat faktoriál, a stiskněte "!" - ihned
 se zobrazí výsledek
-mocnina: nejdříve zadejte základ mocniny
(mocněnec), dále tlačítko "^", a nakonec exponent
(v případě zadávání z klávesnice mocninu pište 
 jako "**")
-odmocnina: nejdříve zadejte odmocněnce (číslo 
 pod odmocninou), tlačítko \u221A a nakonec zadejte
 odmocnitele '''



##################             MAINLOOP             ######################
##pocatecni inicializace kalkulacky spolu s vykreslenim gui, spusti se
#hned pri spusteni programu
if __name__ == "__main__":

    ##window bude oznacovat okno, ve kterem se bude vsechno zobrazovat
    window = Tk()

    ##nastaveni parametru, se kterymi se bude kalkulacka (okno) vykreslovat
    window.title("Calculator")
    window.geometry("360x340")
    window.resizable(0, 0)
    window.configure(background = "lightgrey")

    ##number bude promenna, ktera bude zobrazovat zadavane znaky
    number = StringVar()

    ##prvni kolonka pro vkladani cisel a zobrazeni vysledku
    entry = Entry(window, width = 13, font = ('none 24'), bg = "white", textvar = number, insertontime = 0, justify = "left")
    entry.place(x = 10, y = 0)
    entry.focus_set()

    ##help_display bude Label (vymezeny prostor), ve kterem bude napsana napoveda
    help_display = Label(window, text = help_msg, font=('none',12), bg='grey',fg='black', justify = LEFT)
    help_display.place(x = 360, y = 5)

    ##jednotliva tlacitka
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

    ##lze pouzit enter pro zobrazeni vysledku
    #v tkinteru se enter znaci jako "Return"
    window.bind('<Return>', result_enter)

    ##mainloop, ve kterem se bude vykreslovat kalkulacka
    window.mainloop()

### End of file calculator.py ###

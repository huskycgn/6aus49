import threading
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import LotterieClass
from zeitberechnen import zeitberechnen

root = Tk()
root.title("Lotto Simulator")
verloren = True
startzeit = datetime.now()
endzeit = datetime.now()
running = True
anzahl_durchlaeufe = 0
ergebnis = False
lotto_ticket = []
lotto_ticket_tk = StringVar()
clicked_buttons = []
zahlenreihe = {}

ergebnisframe = Frame(root, relief=RAISED, borderwidth=4)
ergebnisframe.grid(column=4, columnspan=3, rowspan=8, row=0, padx=5, pady=5)

tastenframe = Frame(root, relief=RAISED, borderwidth=4)
tastenframe.grid(column=0, columnspan=3, row=0, padx=5, pady=5)

e = Entry(ergebnisframe, textvariable=lotto_ticket_tk, width=35, borderwidth=2, state=DISABLED)
e.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

v = Label(ergebnisframe, width=40, borderwidth=2, text='0 Versuche')
v.grid(row=5, column=1, columnspan=2, rowspan=2, padx=10, pady=10)

o = Label(ergebnisframe, width=40, borderwidth=2, text='Noch keine Ergebnisse da!')
o.grid(row=7, column=1, rowspan=2, columnspan=2, padx=10, pady=10)


def start_lotto_thread():
    t = threading.Thread(target=button_enter, daemon=True)
    t.start()


def button_click(number, btn_name):
    global lotto_ticket, e, clicked_buttons
    if len(lotto_ticket) < 6:
        lotto_ticket.append(number)
        button_disable(btn_name)
        clicked_buttons.append(btn_name)
        e.config(textvariable=lotto_ticket_tk)
        lotto_ticket_tk.set(str(lotto_ticket))
        for number in lotto_ticket:
            if lotto_ticket.count(number) >= 2:
                messagebox.showerror(title="Fehler!", message="Dubletten sind nicht erlaubt!\n"
                                                              f"Die {number} ist doppelt.")
                lotto_ticket.pop()
                e.config(textvariable=lotto_ticket_tk)
                lotto_ticket_tk.set(str(lotto_ticket))
            else:
                continue
        lotto_ticket = sorted(lotto_ticket)
        e.delete(0, END)
        e.insert(0, str(lotto_ticket))
    else:
        e.delete(0, END)
        e.insert(0, str(lotto_ticket))


def button_clear():
    global lotto_ticket
    lotto_ticket = []
    e.config(textvariable=lotto_ticket_tk)
    lotto_ticket_tk.set(str(lotto_ticket))
    e.delete(0, END)
    v.config(text='0 Versuche')
    for i in clicked_buttons:
        i.config(state=NORMAL)


def cancel_lotto():
    global running
    running = False
    clr_button.config(state=NORMAL)


def button_disable(button):
    button.config(state=DISABLED)


def button_enable(button):
    button.config(state=NORMAL)


def button_enter():
    global clr_button, ergebnis, verloren, anzahl_durchlaeufe, endzeit, startzeit, lotto_ticket, running, zahlenreihe
    running = True
    verloren = True
    o.config(text='Noch keine Ergebnisse da!')
    button_disable(enter_button)
    startzeit = datetime.now()
    if len(lotto_ticket) < 6:
        messagebox.showerror(title="Fehler!", message="Zu wenige Zahlen ausgewählt!")
    elif len(lotto_ticket) > 6:
        messagebox.showerror(title="Fehler!", message="Zu viele Zahlen ausgewählt!")
    else:
        # my_ticket = [2, 28, 35, 15, 8, 19]
        l = LotterieClass.Lotterie(lotto_ticket)
        anzahl_durchlaeufe = 0
        endzeit = datetime.now()
        while verloren is True and running is True:
            ergebnis = l.deter_result()
            zahlenreihe = l.deter_result()[1]
            ergebnis = l.deter_result()[0]
            # print(f"\n{anzahl_durchlaeufe:,d}", 'Versuche', end='\r')
            v.config(text=f"{anzahl_durchlaeufe:,d} Versuche")
            if ergebnis is False:
                anzahl_durchlaeufe += 1
                print(zahlenreihe)
            elif ergebnis is True:
                verloren = False

    if verloren is False:
        # print("\nGewonnen\n")
        endzeit = datetime.now()
        preisreihe = 180  # Kosten in Euro mal zehn.
        kosten = (anzahl_durchlaeufe * preisreihe) / 100
        kosten = float(kosten)
        kosten = "{0:,.2f}".format(kosten)
        berechnungszeit = zeitberechnen(startzeit, endzeit)
        o.config(text=f"Ergebnis:\n6 Richtige nach {anzahl_durchlaeufe:,d} versuchen."
                      f"\nDas hätte {kosten} Euro gekostet.\n"
                      f"Bis zum Sieg wären {anzahl_durchlaeufe // 104:,d} Jahre vergangen\n"
                      f"bei zwei Ziehungen pro Woche.\n"
                      f"Dauer der Berechnung:\n{berechnungszeit[1]} Stunde(n).\n"
                      f"{berechnungszeit[2]} Minuten und \n"
                      f"{berechnungszeit[3]} Sekunden.")
        button_enable(enter_button)
        for bt in clicked_buttons:
            button_enable(bt)
        print(zahlenreihe)
    else:
        o.config(text=f"Abgebrochen nach {anzahl_durchlaeufe:,d} versuchen.")
        for bt in clicked_buttons:
            button_enable(bt)
            button_enable(enter_button)
        print(zahlenreihe)


'''Clear-Taste - Nummerntasten sind unten'''
clr_button = Button(ergebnisframe, text='CLEAR', padx=15, pady=20, command=lambda: button_clear())
clr_button.grid(row=3, column=2)

enter_button = Button(ergebnisframe, text='ENTER', padx=15, pady=20, command=lambda: start_lotto_thread())
enter_button.grid(row=3, column=1)
cancel_button = Button(ergebnisframe, text='CANCEL', padx=15, pady=20, command=cancel_lotto)
cancel_button.grid(row=9, column=4)

btn1 = Button(tastenframe, text=1, padx=15, pady=20, height=1, width=1, command=lambda: button_click(1, btn1))
btn2 = Button(tastenframe, text=2, padx=15, pady=20, height=1, width=1, command=lambda: button_click(2, btn2))
btn3 = Button(tastenframe, text=3, padx=15, pady=20, height=1, width=1, command=lambda: button_click(3, btn3))
btn4 = Button(tastenframe, text=4, padx=15, pady=20, height=1, width=1, command=lambda: button_click(4, btn4))
btn5 = Button(tastenframe, text=5, padx=15, pady=20, height=1, width=1, command=lambda: button_click(5, btn5))
btn6 = Button(tastenframe, text=6, padx=15, pady=20, height=1, width=1, command=lambda: button_click(6, btn6))
btn7 = Button(tastenframe, text=7, padx=15, pady=20, height=1, width=1, command=lambda: button_click(7, btn7))
btn8 = Button(tastenframe, text=8, padx=15, pady=20, height=1, width=1, command=lambda: button_click(8, btn8))
btn9 = Button(tastenframe, text=9, padx=15, pady=20, height=1, width=1, command=lambda: button_click(9, btn9))
btn10 = Button(tastenframe, text=10, padx=15, pady=20, height=1, width=1, command=lambda: button_click(10, btn10))
btn11 = Button(tastenframe, text=11, padx=15, pady=20, height=1, width=1, command=lambda: button_click(11, btn11))
btn12 = Button(tastenframe, text=12, padx=15, pady=20, height=1, width=1, command=lambda: button_click(12, btn12))
btn13 = Button(tastenframe, text=13, padx=15, pady=20, height=1, width=1, command=lambda: button_click(13, btn13))
btn14 = Button(tastenframe, text=14, padx=15, pady=20, height=1, width=1, command=lambda: button_click(14, btn14))
btn15 = Button(tastenframe, text=15, padx=15, pady=20, height=1, width=1, command=lambda: button_click(15, btn15))
btn16 = Button(tastenframe, text=16, padx=15, pady=20, height=1, width=1, command=lambda: button_click(16, btn16))
btn17 = Button(tastenframe, text=17, padx=15, pady=20, height=1, width=1, command=lambda: button_click(17, btn17))
btn18 = Button(tastenframe, text=18, padx=15, pady=20, height=1, width=1, command=lambda: button_click(18, btn18))
btn19 = Button(tastenframe, text=19, padx=15, pady=20, height=1, width=1, command=lambda: button_click(19, btn19))
btn20 = Button(tastenframe, text=20, padx=15, pady=20, height=1, width=1, command=lambda: button_click(20, btn20))
btn21 = Button(tastenframe, text=21, padx=15, pady=20, height=1, width=1, command=lambda: button_click(21, btn21))
btn22 = Button(tastenframe, text=22, padx=15, pady=20, height=1, width=1, command=lambda: button_click(22, btn22))
btn23 = Button(tastenframe, text=23, padx=15, pady=20, height=1, width=1, command=lambda: button_click(23, btn23))
btn24 = Button(tastenframe, text=24, padx=15, pady=20, height=1, width=1, command=lambda: button_click(24, btn24))
btn25 = Button(tastenframe, text=25, padx=15, pady=20, height=1, width=1, command=lambda: button_click(25, btn25))
btn26 = Button(tastenframe, text=26, padx=15, pady=20, height=1, width=1, command=lambda: button_click(26, btn26))
btn27 = Button(tastenframe, text=27, padx=15, pady=20, height=1, width=1, command=lambda: button_click(27, btn27))
btn28 = Button(tastenframe, text=28, padx=15, pady=20, height=1, width=1, command=lambda: button_click(28, btn28))
btn29 = Button(tastenframe, text=29, padx=15, pady=20, height=1, width=1, command=lambda: button_click(29, btn29))
btn30 = Button(tastenframe, text=30, padx=15, pady=20, height=1, width=1, command=lambda: button_click(30, btn30))
btn31 = Button(tastenframe, text=31, padx=15, pady=20, height=1, width=1, command=lambda: button_click(31, btn31))
btn32 = Button(tastenframe, text=32, padx=15, pady=20, height=1, width=1, command=lambda: button_click(32, btn32))
btn33 = Button(tastenframe, text=33, padx=15, pady=20, height=1, width=1, command=lambda: button_click(33, btn33))
btn34 = Button(tastenframe, text=34, padx=15, pady=20, height=1, width=1, command=lambda: button_click(34, btn34))
btn35 = Button(tastenframe, text=35, padx=15, pady=20, height=1, width=1, command=lambda: button_click(35, btn35))
btn36 = Button(tastenframe, text=36, padx=15, pady=20, height=1, width=1, command=lambda: button_click(36, btn36))
btn37 = Button(tastenframe, text=37, padx=15, pady=20, height=1, width=1, command=lambda: button_click(37, btn37))
btn38 = Button(tastenframe, text=38, padx=15, pady=20, height=1, width=1, command=lambda: button_click(38, btn38))
btn39 = Button(tastenframe, text=39, padx=15, pady=20, height=1, width=1, command=lambda: button_click(39, btn39))
btn40 = Button(tastenframe, text=40, padx=15, pady=20, height=1, width=1, command=lambda: button_click(40, btn40))
btn41 = Button(tastenframe, text=41, padx=15, pady=20, height=1, width=1, command=lambda: button_click(41, btn41))
btn42 = Button(tastenframe, text=42, padx=15, pady=20, height=1, width=1, command=lambda: button_click(42, btn42))
btn43 = Button(tastenframe, text=43, padx=15, pady=20, height=1, width=1, command=lambda: button_click(43, btn43))
btn44 = Button(tastenframe, text=44, padx=15, pady=20, height=1, width=1, command=lambda: button_click(44, btn44))
btn45 = Button(tastenframe, text=45, padx=15, pady=20, height=1, width=1, command=lambda: button_click(45, btn45))
btn46 = Button(tastenframe, text=46, padx=15, pady=20, height=1, width=1, command=lambda: button_click(46, btn46))
btn47 = Button(tastenframe, text=47, padx=15, pady=20, height=1, width=1, command=lambda: button_click(47, btn47))
btn48 = Button(tastenframe, text=48, padx=15, pady=20, height=1, width=1, command=lambda: button_click(48, btn48))
btn49 = Button(tastenframe, text=49, padx=15, pady=20, height=1, width=1, command=lambda: button_click(49, btn49))

btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=0, column=5)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)
btn9.grid(row=1, column=4)
btn10.grid(row=1, column=5)
btn11.grid(row=2, column=1)
btn12.grid(row=2, column=2)
btn13.grid(row=2, column=3)
btn14.grid(row=2, column=4)
btn15.grid(row=2, column=5)
btn16.grid(row=3, column=1)
btn17.grid(row=3, column=2)
btn18.grid(row=3, column=3)
btn19.grid(row=3, column=4)
btn20.grid(row=3, column=5)
btn21.grid(row=4, column=1)
btn22.grid(row=4, column=2)
btn23.grid(row=4, column=3)
btn24.grid(row=4, column=4)
btn25.grid(row=4, column=5)
btn26.grid(row=5, column=1)
btn27.grid(row=5, column=2)
btn28.grid(row=5, column=3)
btn29.grid(row=5, column=4)
btn30.grid(row=5, column=5)
btn31.grid(row=6, column=1)
btn32.grid(row=6, column=2)
btn33.grid(row=6, column=3)
btn34.grid(row=6, column=4)
btn35.grid(row=6, column=5)
btn36.grid(row=7, column=1)
btn37.grid(row=7, column=2)
btn38.grid(row=7, column=3)
btn39.grid(row=7, column=4)
btn40.grid(row=7, column=5)
btn41.grid(row=8, column=1)
btn42.grid(row=8, column=2)
btn43.grid(row=8, column=3)
btn44.grid(row=8, column=4)
btn45.grid(row=8, column=5)
btn46.grid(row=9, column=1)
btn47.grid(row=9, column=2)
btn48.grid(row=9, column=3)
btn49.grid(row=9, column=4)

while True:
    root.mainloop()

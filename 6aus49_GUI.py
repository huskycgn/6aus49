import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import LotterieClass
from zeitberechnen import zeitberechnen

root = Tk()
root.title("Lotto Simulator")

lotto_ticket = []


def button_click(number):
    global lotto_ticket
    if len(lotto_ticket) < 6:
        lotto_ticket.append(number)
        for number in lotto_ticket:
            if lotto_ticket.count(number) >= 2:
                messagebox.showerror(title="Fehler!", message="Dubletten sind nicht erlaubt!\n"
                                                              f"Die {number} ist doppelt.")
                lotto_ticket.pop()
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
    e.delete(0, END)


def update_versuche(versuche):
    v.config(text=versuche)


def button_enter():
    print(lotto_ticket)
    startzeit_unix = time.time()
    startzeit = datetime.now()
    if len(lotto_ticket) < 6:
        messagebox.showerror(title="Fehler!", message="Zu wenige Zahlen ausgewählt!")
    elif len(lotto_ticket) > 6:
        messagebox.showerror(title="Fehler!", message="Zu viele Zahlen ausgewählt!")
    else:
        l = LotterieClass.Lotterie(lotto_ticket)
        number_of_runs = 0
        verloren = True
        endzeit = datetime.now()
        endzeit_unix = time.time()
        preisreihe = 120  # Kosten in Euro mal zehn.
        kosten = (number_of_runs * preisreihe) / 100
        kosten = float(kosten)
        kosten = "{0:,.2f}".format(kosten)
        berechnungszeit = zeitberechnen(startzeit, endzeit)
        berechnungszeit_roh = endzeit_unix - startzeit_unix
        berechnungszeit_roh = float(berechnungszeit_roh)

        while verloren is True:
            result = l.deter_result()
            print(f"\n{number_of_runs:,d}", 'Versuche', end='\r')
            update_versuche(number_of_runs)
            if result is False:
                update_versuche(number_of_runs)
                number_of_runs += 1
            else:
                if result is True:
                    verloren = False
                    # print("\nGewonnen\n")
                    endzeit = datetime.now()
                    endzeit_unix = time.time()
                    o.config(text=f"\n6 Richtige nach {number_of_runs:,d} versuchen."
                                  f"\nDas hätte {kosten} Euro gekostet.\n"
                                  f"Bis zum Sieg wären {number_of_runs // 104:,d} Jahre vergangen\n"
                                  f"bei zwei Ziehungen pro Woche.")

        # messagebox.showinfo(title="Ergebnis", message=


o = Label(root, width=40, borderwidth=2, text="Noch kein Ergebnis da.")
o.grid(row=2, column=7, columnspan=2, rowspan=2, padx=0, pady=0)

Button(root, text=1, padx=15, pady=20, command=lambda: button_click(1)).grid(row=0, column=1)
Button(root, text=2, padx=15, pady=20, command=lambda: button_click(2)).grid(row=0, column=2)
Button(root, text=3, padx=15, pady=20, command=lambda: button_click(3)).grid(row=0, column=3)
Button(root, text=4, padx=15, pady=20, command=lambda: button_click(4)).grid(row=0, column=4)
Button(root, text=5, padx=15, pady=20, command=lambda: button_click(5)).grid(row=0, column=5)
Button(root, text=6, padx=15, pady=20, command=lambda: button_click(6)).grid(row=1, column=1)
Button(root, text=7, padx=15, pady=20, command=lambda: button_click(7)).grid(row=1, column=2)
Button(root, text=8, padx=15, pady=20, command=lambda: button_click(8)).grid(row=1, column=3)
Button(root, text=9, padx=15, pady=20, command=lambda: button_click(9)).grid(row=1, column=4)
Button(root, text=10, padx=15, pady=20, command=lambda: button_click(10)).grid(row=1, column=5)
Button(root, text=11, padx=15, pady=20, command=lambda: button_click(11)).grid(row=2, column=1)
Button(root, text=12, padx=15, pady=20, command=lambda: button_click(12)).grid(row=2, column=2)
Button(root, text=13, padx=15, pady=20, command=lambda: button_click(13)).grid(row=2, column=3)
Button(root, text=14, padx=15, pady=20, command=lambda: button_click(14)).grid(row=2, column=4)
Button(root, text=15, padx=15, pady=20, command=lambda: button_click(15)).grid(row=2, column=5)
Button(root, text=16, padx=15, pady=20, command=lambda: button_click(16)).grid(row=3, column=1)
Button(root, text=17, padx=15, pady=20, command=lambda: button_click(17)).grid(row=3, column=2)
Button(root, text=18, padx=15, pady=20, command=lambda: button_click(18)).grid(row=3, column=3)
Button(root, text=19, padx=15, pady=20, command=lambda: button_click(19)).grid(row=3, column=4)
Button(root, text=20, padx=15, pady=20, command=lambda: button_click(20)).grid(row=3, column=5)
Button(root, text=21, padx=15, pady=20, command=lambda: button_click(21)).grid(row=4, column=1)
Button(root, text=22, padx=15, pady=20, command=lambda: button_click(22)).grid(row=4, column=2)
Button(root, text=23, padx=15, pady=20, command=lambda: button_click(23)).grid(row=4, column=3)
Button(root, text=24, padx=15, pady=20, command=lambda: button_click(24)).grid(row=4, column=4)
Button(root, text=25, padx=15, pady=20, command=lambda: button_click(25)).grid(row=4, column=5)
Button(root, text=26, padx=15, pady=20, command=lambda: button_click(26)).grid(row=5, column=1)
Button(root, text=27, padx=15, pady=20, command=lambda: button_click(27)).grid(row=5, column=2)
Button(root, text=28, padx=15, pady=20, command=lambda: button_click(28)).grid(row=5, column=3)
Button(root, text=29, padx=15, pady=20, command=lambda: button_click(29)).grid(row=5, column=4)
Button(root, text=30, padx=15, pady=20, command=lambda: button_click(30)).grid(row=5, column=5)
Button(root, text=31, padx=15, pady=20, command=lambda: button_click(31)).grid(row=6, column=1)
Button(root, text=32, padx=15, pady=20, command=lambda: button_click(32)).grid(row=6, column=2)
Button(root, text=33, padx=15, pady=20, command=lambda: button_click(33)).grid(row=6, column=3)
Button(root, text=34, padx=15, pady=20, command=lambda: button_click(34)).grid(row=6, column=4)
Button(root, text=35, padx=15, pady=20, command=lambda: button_click(35)).grid(row=6, column=5)
Button(root, text=36, padx=15, pady=20, command=lambda: button_click(36)).grid(row=7, column=1)
Button(root, text=37, padx=15, pady=20, command=lambda: button_click(37)).grid(row=7, column=2)
Button(root, text=38, padx=15, pady=20, command=lambda: button_click(38)).grid(row=7, column=3)
Button(root, text=39, padx=15, pady=20, command=lambda: button_click(39)).grid(row=7, column=4)
Button(root, text=40, padx=15, pady=20, command=lambda: button_click(40)).grid(row=7, column=5)
Button(root, text=41, padx=15, pady=20, command=lambda: button_click(41)).grid(row=8, column=1)
Button(root, text=42, padx=15, pady=20, command=lambda: button_click(42)).grid(row=8, column=2)
Button(root, text=43, padx=15, pady=20, command=lambda: button_click(43)).grid(row=8, column=3)
Button(root, text=44, padx=15, pady=20, command=lambda: button_click(44)).grid(row=8, column=4)
Button(root, text=45, padx=15, pady=20, command=lambda: button_click(45)).grid(row=8, column=5)
Button(root, text=46, padx=15, pady=20, command=lambda: button_click(46)).grid(row=9, column=1)
Button(root, text=47, padx=15, pady=20, command=lambda: button_click(47)).grid(row=9, column=2)
Button(root, text=48, padx=15, pady=20, command=lambda: button_click(48)).grid(row=9, column=3)
Button(root, text=49, padx=15, pady=20, command=lambda: button_click(49)).grid(row=9, column=4)

Button(root, text='ENTER', padx=15, pady=20, command=lambda: button_enter()).grid(row=9, column=7)
Button(root, text='CLEAR', padx=15, pady=20, command=lambda: button_clear()).grid(row=9, column=8)

e = Entry(root, width=20, borderwidth=1)
e.grid(row=0, column=7, columnspan=2, padx=0, pady=0)

global v

v = Label(root, width=40, borderwidth=2, text='0 Versuche')
v.grid(row=1, column=7, columnspan=2, padx=0, pady=0)

root.mainloop()

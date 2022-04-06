import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import LotterieClass
from zeitberechnen import zeitberechnen
import threading

root = Tk()
root.title("Lotto Simulator")
verloren = True
startzeit = datetime.now()
endzeit = datetime.now()
lotto_ticket = []
running = True
anzahl_durchlaeufe = 0
ergebnis = False

ergebnisframe = Frame(root, relief=RAISED, borderwidth=4)
ergebnisframe.grid(column=4, columnspan=3, rowspan=8, row=0, padx=5, pady=5)

tastenframe = Frame(root, relief=RAISED, borderwidth=4)
tastenframe.grid(column=0, columnspan=3, row=0, padx=5, pady=5)

e = Entry(ergebnisframe, width=35, borderwidth=2)
e.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

v = Label(ergebnisframe, width=40, borderwidth=2, text='0 Versuche')
v.grid(row=5, column=1, columnspan=2, rowspan=2, padx=10, pady=10)

o = Label(ergebnisframe, width=40, borderwidth=2, text='Noch keine Ergebnisse da!')
o.grid(row=7, column=1, rowspan=2, columnspan=2, padx=10, pady=10)

'''Clear-Taste - Nummerntasten sind unten'''
clr_button = Button(ergebnisframe, text='CLEAR', padx=15, pady=20, command=lambda: button_clear())
clr_button.grid(row=3, column=2)


def start_lotto_thread():
    t = threading.Thread(target=button_enter, daemon=True)
    t.start()


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


def cancel_lotto():
    global running
    running = False


def button_enter():
    global clr_button, ergebnis, verloren, anzahl_durchlaeufe, endzeit, startzeit
    clr_button.config(state=DISABLED)
    print(lotto_ticket)
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
            # print(f"\n{anzahl_durchlaeufe:,d}", 'Versuche', end='\r')
            v.config(text=f"{anzahl_durchlaeufe:,d} Versuche")
            if ergebnis is False:
                anzahl_durchlaeufe += 1
            elif ergebnis is True:
                verloren = False

    if verloren is False:
        # print("\nGewonnen\n")
        endzeit = datetime.now()
        preisreihe = 120  # Kosten in Euro mal zehn.
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
    else:
        o.config(text=f"Abgebrochen nach {anzahl_durchlaeufe:,d} versuchen.")
    clr_button.config(state=ACTIVE)


Button(tastenframe, text=1, padx=15, pady=20, height=1, width=1, command=lambda: button_click(1)).grid(row=0, column=1)
Button(tastenframe, text=2, padx=15, pady=20, height=1, width=1, command=lambda: button_click(2)).grid(row=0, column=2)
Button(tastenframe, text=3, padx=15, pady=20, height=1, width=1, command=lambda: button_click(3)).grid(row=0, column=3)
Button(tastenframe, text=4, padx=15, pady=20, height=1, width=1, command=lambda: button_click(4)).grid(row=0, column=4)
Button(tastenframe, text=5, padx=15, pady=20, height=1, width=1, command=lambda: button_click(5)).grid(row=0, column=5)
Button(tastenframe, text=6, padx=15, pady=20, height=1, width=1, command=lambda: button_click(6)).grid(row=1, column=1)
Button(tastenframe, text=7, padx=15, pady=20, height=1, width=1, command=lambda: button_click(7)).grid(row=1, column=2)
Button(tastenframe, text=8, padx=15, pady=20, height=1, width=1, command=lambda: button_click(8)).grid(row=1, column=3)
Button(tastenframe, text=9, padx=15, pady=20, height=1, width=1, command=lambda: button_click(9)).grid(row=1, column=4)
Button(tastenframe, text=10, padx=15, pady=20, height=1, width=1, command=lambda: button_click(10)).grid(row=1,
                                                                                                         column=5)
Button(tastenframe, text=11, padx=15, pady=20, height=1, width=1, command=lambda: button_click(11)).grid(row=2,
                                                                                                         column=1)
Button(tastenframe, text=12, padx=15, pady=20, height=1, width=1, command=lambda: button_click(12)).grid(row=2,
                                                                                                         column=2)
Button(tastenframe, text=13, padx=15, pady=20, height=1, width=1, command=lambda: button_click(13)).grid(row=2,
                                                                                                         column=3)
Button(tastenframe, text=14, padx=15, pady=20, height=1, width=1, command=lambda: button_click(14)).grid(row=2,
                                                                                                         column=4)
Button(tastenframe, text=15, padx=15, pady=20, height=1, width=1, command=lambda: button_click(15)).grid(row=2,
                                                                                                         column=5)
Button(tastenframe, text=16, padx=15, pady=20, height=1, width=1, command=lambda: button_click(16)).grid(row=3,
                                                                                                         column=1)
Button(tastenframe, text=17, padx=15, pady=20, height=1, width=1, command=lambda: button_click(17)).grid(row=3,
                                                                                                         column=2)
Button(tastenframe, text=18, padx=15, pady=20, height=1, width=1, command=lambda: button_click(18)).grid(row=3,
                                                                                                         column=3)
Button(tastenframe, text=19, padx=15, pady=20, height=1, width=1, command=lambda: button_click(19)).grid(row=3,
                                                                                                         column=4)
Button(tastenframe, text=20, padx=15, pady=20, height=1, width=1, command=lambda: button_click(20)).grid(row=3,
                                                                                                         column=5)
Button(tastenframe, text=21, padx=15, pady=20, height=1, width=1, command=lambda: button_click(21)).grid(row=4,
                                                                                                         column=1)
Button(tastenframe, text=22, padx=15, pady=20, height=1, width=1, command=lambda: button_click(22)).grid(row=4,
                                                                                                         column=2)
Button(tastenframe, text=23, padx=15, pady=20, height=1, width=1, command=lambda: button_click(23)).grid(row=4,
                                                                                                         column=3)
Button(tastenframe, text=24, padx=15, pady=20, height=1, width=1, command=lambda: button_click(24)).grid(row=4,
                                                                                                         column=4)
Button(tastenframe, text=25, padx=15, pady=20, height=1, width=1, command=lambda: button_click(25)).grid(row=4,
                                                                                                         column=5)
Button(tastenframe, text=26, padx=15, pady=20, height=1, width=1, command=lambda: button_click(26)).grid(row=5,
                                                                                                         column=1)
Button(tastenframe, text=27, padx=15, pady=20, height=1, width=1, command=lambda: button_click(27)).grid(row=5,
                                                                                                         column=2)
Button(tastenframe, text=28, padx=15, pady=20, height=1, width=1, command=lambda: button_click(28)).grid(row=5,
                                                                                                         column=3)
Button(tastenframe, text=29, padx=15, pady=20, height=1, width=1, command=lambda: button_click(29)).grid(row=5,
                                                                                                         column=4)
Button(tastenframe, text=30, padx=15, pady=20, height=1, width=1, command=lambda: button_click(30)).grid(row=5,
                                                                                                         column=5)
Button(tastenframe, text=31, padx=15, pady=20, height=1, width=1, command=lambda: button_click(31)).grid(row=6,
                                                                                                         column=1)
Button(tastenframe, text=32, padx=15, pady=20, height=1, width=1, command=lambda: button_click(32)).grid(row=6,
                                                                                                         column=2)
Button(tastenframe, text=33, padx=15, pady=20, height=1, width=1, command=lambda: button_click(33)).grid(row=6,
                                                                                                         column=3)
Button(tastenframe, text=34, padx=15, pady=20, height=1, width=1, command=lambda: button_click(34)).grid(row=6,
                                                                                                         column=4)
Button(tastenframe, text=35, padx=15, pady=20, height=1, width=1, command=lambda: button_click(35)).grid(row=6,
                                                                                                         column=5)
Button(tastenframe, text=36, padx=15, pady=20, height=1, width=1, command=lambda: button_click(36)).grid(row=7,
                                                                                                         column=1)
Button(tastenframe, text=37, padx=15, pady=20, height=1, width=1, command=lambda: button_click(37)).grid(row=7,
                                                                                                         column=2)
Button(tastenframe, text=38, padx=15, pady=20, height=1, width=1, command=lambda: button_click(38)).grid(row=7,
                                                                                                         column=3)
Button(tastenframe, text=39, padx=15, pady=20, height=1, width=1, command=lambda: button_click(39)).grid(row=7,
                                                                                                         column=4)
Button(tastenframe, text=40, padx=15, pady=20, height=1, width=1, command=lambda: button_click(40)).grid(row=7,
                                                                                                         column=5)
Button(tastenframe, text=41, padx=15, pady=20, height=1, width=1, command=lambda: button_click(41)).grid(row=8,
                                                                                                         column=1)
Button(tastenframe, text=42, padx=15, pady=20, height=1, width=1, command=lambda: button_click(42)).grid(row=8,
                                                                                                         column=2)
Button(tastenframe, text=43, padx=15, pady=20, height=1, width=1, command=lambda: button_click(43)).grid(row=8,
                                                                                                         column=3)
Button(tastenframe, text=44, padx=15, pady=20, height=1, width=1, command=lambda: button_click(44)).grid(row=8,
                                                                                                         column=4)
Button(tastenframe, text=45, padx=15, pady=20, height=1, width=1, command=lambda: button_click(45)).grid(row=8,
                                                                                                         column=5)
Button(tastenframe, text=46, padx=15, pady=20, height=1, width=1, command=lambda: button_click(46)).grid(row=9,
                                                                                                         column=1)
Button(tastenframe, text=47, padx=15, pady=20, height=1, width=1, command=lambda: button_click(47)).grid(row=9,
                                                                                                         column=2)
Button(tastenframe, text=48, padx=15, pady=20, height=1, width=1, command=lambda: button_click(48)).grid(row=9,
                                                                                                         column=3)
Button(tastenframe, text=49, padx=15, pady=20, height=1, width=1, command=lambda: button_click(49)).grid(row=9,
                                                                                                         column=4)

Button(ergebnisframe, text='ENTER', padx=15, pady=20, command=lambda: start_lotto_thread()).grid(row=3, column=1)
Button(ergebnisframe, text='CANCEL', padx=15, pady=20, command=cancel_lotto).grid(row=9, column=4)

root.mainloop()

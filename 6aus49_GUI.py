from datetime import datetime
from zeitberechnen import zeitberechnen
import time
import LotterieClass
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lotto Simulator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=6, columnspan=3, padx=10, pady=10)
lotto_ticket = []


def button_click(number):
    global lotto_ticket
    if len(lotto_ticket) < 6:
        lotto_ticket.append(number)
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


def button_enter():
    print(lotto_ticket)
    startzeit_unix = time.time()
    startzeit = datetime.now()
    if len(lotto_ticket) < 6:
        print("Zu wenige Zahlen!")
    elif len(lotto_ticket) > 6:
        print("Zu viele Zahlen!")
    else:
        # my_ticket = [2, 28, 35, 15, 8, 19]
        l = LotterieClass.Lotterie(lotto_ticket)
        anzahl_durchlaeufe = 0
        verloren = True
        endzeit = datetime.now()
        endzeit_unix = time.time()

        while verloren is True:
            ergebnis = l.deter_result()
            print(f"\n{anzahl_durchlaeufe:,d}", 'Versuche', end='\r')
            if ergebnis is False:
                anzahl_durchlaeufe += 1
            else:
                if ergebnis is True:
                    verloren = False
                    print("\nGewonnen\n")
                    endzeit = datetime.now()
                    endzeit_unix = time.time()

        preisreihe = 120  # Kosten in Euro mal zehn.
        kosten = (anzahl_durchlaeufe * preisreihe) / 100
        kosten = float(kosten)
        kosten = "{0:,.2f}".format(kosten)
        berechnungszeit = zeitberechnen(startzeit, endzeit)
        berechnungszeit_roh = endzeit_unix - startzeit_unix
        berechnungszeit_roh = float(berechnungszeit_roh)

        messagebox.showinfo(title="Ergebnis", message=f"\n6 Richtige nach {anzahl_durchlaeufe:,d} versuchen."
                                                      f"\nDas hätte {kosten} Euro gekostet.\nBis zum Sieg wären {anzahl_durchlaeufe // 104:,d} Jahre vergangen\n"
                                                      f"bei zwei Ziehungen pro Woche.")


Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1)).grid(row=0, column=1)
Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2)).grid(row=0, column=2)
Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3)).grid(row=0, column=3)
Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4)).grid(row=0, column=4)
Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5)).grid(row=0, column=5)
Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6)).grid(row=1, column=1)
Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7)).grid(row=1, column=2)
Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8)).grid(row=1, column=3)
Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9)).grid(row=1, column=4)
Button(root, text=10, padx=40, pady=20, command=lambda: button_click(10)).grid(row=1, column=5)
Button(root, text=11, padx=40, pady=20, command=lambda: button_click(11)).grid(row=2, column=1)
Button(root, text=12, padx=40, pady=20, command=lambda: button_click(12)).grid(row=2, column=2)
Button(root, text=13, padx=40, pady=20, command=lambda: button_click(13)).grid(row=2, column=3)
Button(root, text=14, padx=40, pady=20, command=lambda: button_click(14)).grid(row=2, column=4)
Button(root, text=15, padx=40, pady=20, command=lambda: button_click(15)).grid(row=2, column=5)
Button(root, text=16, padx=40, pady=20, command=lambda: button_click(16)).grid(row=3, column=1)
Button(root, text=17, padx=40, pady=20, command=lambda: button_click(17)).grid(row=3, column=2)
Button(root, text=18, padx=40, pady=20, command=lambda: button_click(18)).grid(row=3, column=3)
Button(root, text=19, padx=40, pady=20, command=lambda: button_click(19)).grid(row=3, column=4)
Button(root, text=20, padx=40, pady=20, command=lambda: button_click(20)).grid(row=3, column=5)
Button(root, text=21, padx=40, pady=20, command=lambda: button_click(21)).grid(row=4, column=1)
Button(root, text=22, padx=40, pady=20, command=lambda: button_click(22)).grid(row=4, column=2)
Button(root, text=23, padx=40, pady=20, command=lambda: button_click(23)).grid(row=4, column=3)
Button(root, text=24, padx=40, pady=20, command=lambda: button_click(24)).grid(row=4, column=4)
Button(root, text=25, padx=40, pady=20, command=lambda: button_click(25)).grid(row=4, column=5)
Button(root, text=26, padx=40, pady=20, command=lambda: button_click(26)).grid(row=5, column=1)
Button(root, text=27, padx=40, pady=20, command=lambda: button_click(27)).grid(row=5, column=2)
Button(root, text=28, padx=40, pady=20, command=lambda: button_click(28)).grid(row=5, column=3)
Button(root, text=29, padx=40, pady=20, command=lambda: button_click(29)).grid(row=5, column=4)
Button(root, text=30, padx=40, pady=20, command=lambda: button_click(30)).grid(row=5, column=5)
Button(root, text=31, padx=40, pady=20, command=lambda: button_click(31)).grid(row=6, column=1)
Button(root, text=32, padx=40, pady=20, command=lambda: button_click(32)).grid(row=6, column=2)
Button(root, text=33, padx=40, pady=20, command=lambda: button_click(33)).grid(row=6, column=3)
Button(root, text=34, padx=40, pady=20, command=lambda: button_click(34)).grid(row=6, column=4)
Button(root, text=35, padx=40, pady=20, command=lambda: button_click(35)).grid(row=6, column=5)
Button(root, text=36, padx=40, pady=20, command=lambda: button_click(36)).grid(row=7, column=1)
Button(root, text=37, padx=40, pady=20, command=lambda: button_click(37)).grid(row=7, column=2)
Button(root, text=38, padx=40, pady=20, command=lambda: button_click(38)).grid(row=7, column=3)
Button(root, text=39, padx=40, pady=20, command=lambda: button_click(39)).grid(row=7, column=4)
Button(root, text=40, padx=40, pady=20, command=lambda: button_click(40)).grid(row=7, column=5)
Button(root, text=41, padx=40, pady=20, command=lambda: button_click(41)).grid(row=8, column=1)
Button(root, text=42, padx=40, pady=20, command=lambda: button_click(42)).grid(row=8, column=2)
Button(root, text=43, padx=40, pady=20, command=lambda: button_click(43)).grid(row=8, column=3)
Button(root, text=44, padx=40, pady=20, command=lambda: button_click(44)).grid(row=8, column=4)
Button(root, text=45, padx=40, pady=20, command=lambda: button_click(45)).grid(row=8, column=5)
Button(root, text=46, padx=40, pady=20, command=lambda: button_click(46)).grid(row=9, column=1)
Button(root, text=47, padx=40, pady=20, command=lambda: button_click(47)).grid(row=9, column=2)
Button(root, text=48, padx=40, pady=20, command=lambda: button_click(48)).grid(row=9, column=3)
Button(root, text=49, padx=40, pady=20, command=lambda: button_click(49)).grid(row=9, column=4)

Button(root, text='ENTER', padx=40, pady=20, command=lambda: button_enter()).grid(row=9, column=6)
Button(root, text='CLEAR', padx=40, pady=20, command=lambda: button_clear()).grid(row=9, column=7)

root.mainloop()

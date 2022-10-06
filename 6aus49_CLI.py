import time
from datetime import datetime

from cursor import cursor
from art import logo

import LotterieClass
from zeitberechnen import zeitberechnen

cursor.hide()

startzeit_unix = time.time()
startzeit = datetime.now()
my_ticket = []

print(logo)

while len(my_ticket) < 6:
    zahl = input("Bitte Zahl zwischen 1 und 49 eingeben: ")
    if LotterieClass.Lotterie.eingabe_pruefen(int(zahl)) is True:
        dublette = int(zahl) in my_ticket
        if dublette is False:
            my_ticket.append(int(zahl))
        else:
            print("Dubletten sind nicht zugelassen! ")
            continue
    else:
        print("Zahl muss zwischen 1 und 49 liegen! ")
        continue

print(sorted(my_ticket))

# my_ticket = [2, 28, 35, 15, 8, 19]
l = LotterieClass.Lotterie(my_ticket)

anzahl_durchlaeufe = 0
verloren = True
endzeit = datetime.now()
endzeit_unix = time.time()

while verloren is True:
    ergebnis = l.deter_result()
    print(f"{anzahl_durchlaeufe:,d}", 'Versuche', end='\r', flush=True)
    if ergebnis is False:
        anzahl_durchlaeufe += 1
    else:
        if ergebnis is True:
            verloren = False
            print("\nGewonnen\n")
            endzeit = datetime.now()
            endzeit_unix = time.time()
preisreihe = 180  # Kosten in Euro mal zehn.
kosten = (anzahl_durchlaeufe * preisreihe) / 100
kosten = float(kosten)
kosten = "{0:,.2f}".format(kosten)
berechnungszeit = zeitberechnen(startzeit, endzeit)
berechnungszeit_roh = endzeit_unix - startzeit_unix
berechnungszeit_roh = float(berechnungszeit_roh)

print(f"\n6 Richtige nach {anzahl_durchlaeufe:,d} versuchen.")
print(f"Das hätte {kosten} Euro gekostet.\nBis zum Sieg wären {anzahl_durchlaeufe // 104:,d} Jahre vergangen\n"
      f"bei zwei Ziehungen pro Woche.")
print(f"Dauer der Berechnung:\n{berechnungszeit[1]} Stunde(n).\n"
      f"{berechnungszeit[2]} Minuten und \n"
      f"{berechnungszeit[3]} Sekunden.")

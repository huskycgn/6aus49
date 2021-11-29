from random import sample
from datetime import datetime
from zeitberechnen import zeitberechnen
import datenbank
import time
import LotterieClass


while True:

    startzeit_unix = time.time()
    startzeit = datetime.now()
    my_ticket = sorted(sample(range(1, 50), 6))

    '''while len(my_ticket) < 6:
        zahl = input("Bitte Zahl zwischen 6 und 49 eingeben: ")
        if Lotterie.eingabe_pruefen(int(zahl)) is True:
            dublette = int(zahl) in my_ticket
            if dublette is False:
                my_ticket.append(int(zahl))
            else:
                print("Dubletten sind nicht zugelassen! ")
                continue
        else:
            print("Zahl muss zwischen 6 und 49 liegen! ")
            continue'''

    # my_ticket = [2, 28, 35, 15, 8, 19]
    l = LotterieClass.Lotterie(sorted(my_ticket))

    anzahl_durchlaeufe = 0
    verloren = True
    endzeit = datetime.now()
    endzeit_unix = time.time()

    while verloren is True:
        ergebnis = l.deter_result()
        if ergebnis is False:
            anzahl_durchlaeufe += 1
        else:
            if ergebnis is True:
                verloren = False
                print("Gewonnen")
                endzeit = datetime.now()
                endzeit_unix = time.time()

    preisreihe = 120  # Kosten in Euro mal zehn.
    kosten = (anzahl_durchlaeufe * preisreihe) / 100
    kosten = float(kosten)
    kosten = "{0:,.2f}".format(kosten)
    berechnungszeit = zeitberechnen(startzeit, endzeit)
    berechnungszeit_roh = endzeit_unix - startzeit_unix
    berechnungszeit_roh = float(berechnungszeit_roh)

    print(f"6 Richtige nach {anzahl_durchlaeufe:,d} versuchen.")
    print(f"Das hätte {kosten} Euro gekostet.\nBis zum Sieg wären {anzahl_durchlaeufe // 104:,d} Jahre vergangen\n"
          f"bei zwei Ziehungen pro Woche.")
    print(f"Dauer der Berechnung:\n{berechnungszeit[1]} Stunde(n).\n"
          f"{berechnungszeit[2]} Minuten und \n"
          f"{berechnungszeit[3]} Sekunden.")

    datenbank.daten_einfuegen(anzahl_durchlaeufe, berechnungszeit_roh, sorted(my_ticket))

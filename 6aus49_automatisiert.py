import socket
import time
from datetime import datetime
from random import sample

import LotterieClass
import datenbank
from zeitberechnen import zeitberechnen

hostip = socket.gethostbyname(socket.gethostname())

while True:

    startzeit_unix = time.time()
    startzeit = datetime.now()
    my_ticket = sorted(sample(range(1, 50), 6))

    # my_ticket = [2, 28, 35, 15, 8, 19]
    l = LotterieClass.Lotterie(sorted(my_ticket))

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

    print(f"6 Richtige nach {anzahl_durchlaeufe:,d} versuchen.")
    print(f"Das hätte {kosten} Euro gekostet.\nBis zum Sieg wären {anzahl_durchlaeufe // 104:,d} Jahre vergangen\n"
          f"bei zwei Ziehungen pro Woche.")
    print(f"Dauer der Berechnung:\n{berechnungszeit[1]} Stunde(n).\n"
          f"{berechnungszeit[2]} Minuten und \n"
          f"{berechnungszeit[3]} Sekunden.")

    datenbank.daten_einfuegen(anzahl_durchlaeufe, berechnungszeit_roh, sorted(my_ticket), hostip)

from random import sample
from datetime import datetime
from zeitberechnen import zeitberechnen


class Lotterie:
    '''Lotterieklasse - kann alles, was eine Lotterie koennen sollte.
    Parameter ist eine Liste mit sechs Integerwerten.'''

    def __init__(self, tip):
        self.lotteriezahlen = list(range(1, 50))  # Anzahl der Gesamtzahlen minus 1
        self.lottery = tip  # Der ausgefüllte "Lottoschein"

    def ziehung_der_zahlen(self):
        ziehung = sample(self.lotteriezahlen, 6)  # Anzahl der zu ziehenden Zahlen
        return sorted(ziehung)  # Gibt die zufällig gezogenen Zahlen aus.

    def output_zahlen(self):
        return self.lotteriezahlen

    def deter_result(self):
        if sorted(self.lottery) == sorted(self.ziehung_der_zahlen()):
            return True
        else:
            return False

    @staticmethod  # statische Methode, um die Eingaben zu prüfen.
    def eingabe_pruefen(eingabe):
        if str(eingabe).isnumeric():
            if 49 >= int(eingabe) >= 0:
                return True
            else:
                return False
        else:
            print("Buchstaben sind nicht erlaubt!")
            return False


startzeit = datetime.now()
my_ticket = []

while len(my_ticket) < 6:
    zahl = input("Bitte Zahl zwischen 6 und 49 eingeben: ")
    if Lotterie.eingabe_pruefen(zahl) is True:
        dublette = zahl in my_ticket
        if dublette is False:
            my_ticket.append(int(zahl))
        else:
            print("Dubletten sind nicht zugelassen! ")
            continue
    else:
        print("Zahl muss zwischen 6 und 49 liegen! ")
        continue

print(sorted(my_ticket))

# my_ticket = [2, 28, 35, 15, 8, 19]
l = Lotterie(my_ticket)

anzahl_durchlaeufe = 0
verloren = True
endzeit = datetime.now()

while verloren is True:
    ergebnis = l.deter_result()
    if ergebnis is False:
        anzahl_durchlaeufe += 1
    else:
        if ergebnis is True:
            verloren = False
            print("Gewonnen")
            endzeit = datetime.now()

preisreihe = 120  # Kosten in Euro mal zehn.
kosten = (anzahl_durchlaeufe * preisreihe) / 100
kosten = float(kosten)
kosten = "{0:,.2f}".format(kosten)
berechnungszeit = zeitberechnen(startzeit, endzeit)

print(f"6 Richtige nach {anzahl_durchlaeufe:,d} versuchen.")
print(f"Das hätte {kosten} Euro gekostet.")
print(f"Dauer der Berechnung:\n{berechnungszeit[1]} Stunde(n).\n"
      f"{berechnungszeit[2]} Minuten und \n"
      f"{berechnungszeit[3]} Sekunden.")

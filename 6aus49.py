from random import sample


class Lotterie:
    '''Lotterieklasse - kann alles, was eine Lotterie koennen sollte.
    Parameter ist eine Liste mit sechs Integerwerten.'''

    def __init__(self, tip):
        self.lotteriezahlen = list(range(1, 50))
        self.lottery = tip

    def ziehung_der_zahlen(self):
        ziehung = sample(self.lotteriezahlen, 6)
        return sorted(ziehung)

    def output_zahlen(self):
        return self.lotteriezahlen

    def out_myticket(self):
        return self.lottery

    def deter_result(self):
        if sorted(self.lottery) == sorted(self.ziehung_der_zahlen()):
            return True
        else:
            return False

    @staticmethod
    def eingabe_pruefen(eingabe):
        if str(eingabe).isnumeric():
            if 49 >= int(eingabe) >= 0:
                return True
            else:
                return False
        else:
            print("Buchstaben sind nicht erlaubt!")
            return False


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
print(l.ziehung_der_zahlen())

anzahl_durchlaeufe = 0
verloren = True


while verloren is True:
    ergebnis = l.deter_result()
    if ergebnis is False:
        anzahl_durchlaeufe += 1
    else:
        if ergebnis is True:
            verloren = False
            print("Gewonnen")

print(anzahl_durchlaeufe)

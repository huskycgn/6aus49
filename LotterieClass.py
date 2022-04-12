from random import sample


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
        ziehung = sorted(self.ziehung_der_zahlen())
        # ziehung = sorted([4, 7, 31, 34, 47, 49])
        schein = sorted(self.lottery)
        if schein == ziehung:
            return True
        else:
            return False

    def statistik(self, wertreihe):
        for i in self.ziehung_der_zahlen():
            wertreihe[i] += 1
            return wertreihe

    @staticmethod  # statische Methode, um die Eingaben zu prüfen.
    def eingabe_pruefen(eingabe):
        if str(eingabe).isnumeric():
            if 49 >= int(eingabe) > 0:
                return True
            else:
                return False
        else:
            print("Buchstaben sind nicht erlaubt!")
            return False

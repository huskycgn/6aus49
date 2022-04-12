from random import sample

wertreihe = {}
for i in range(1, 50):
    wertreihe[i] = 0


class Lotterie:
    '''Lotterieklasse - kann alles, was eine Lotterie koennen sollte.
    Parameter ist eine Liste mit sechs Integerwerten.'''

    def __init__(self, tip):
        self.lotteriezahlen = list(range(1, 50))  # Anzahl der Gesamtzahlen minus 1
        self.lottery = tip  # Der ausgefüllte "Lottoschein"

    def ziehung_der_zahlen(self):
        global wertreihe
        ziehung = sample(self.lotteriezahlen, 6)  # Anzahl der zu ziehenden Zahlen
        for z in ziehung:
            wertreihe[z] += 1
        resultset = [sorted(ziehung), wertreihe]
        # return sorted(ziehung), wertreihe  # Gibt die zufällig gezogenen Zahlen aus.
        return resultset

    def output_zahlen(self):
        return self.lotteriezahlen

    def deter_result(self):
        ziehung = sorted(self.ziehung_der_zahlen()[0])
        wertreihe = (self.ziehung_der_zahlen()[1])
        # ziehung = sorted([4, 7, 31, 34, 47, 49])
        schein = sorted(self.lottery)
        if schein == ziehung[0]:
            return True, wertreihe
        else:
            return False, wertreihe

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

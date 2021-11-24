def zeitberechnen(start, ende):
    """Nimmt datetime Objekte an
    und gibt Zeitdifferenzen als Liste aus
    0: Gesamtdauer in Sekunden (int)
    1: Dauer in Stunden (int)
    2: Dauer in Minuten (int)
    3: Dauer in Sekunden (int)"""
    dauer = ende - start
    dauer = int(dauer.seconds)
    dauer = int(dauer)
    stunden = dauer // 3600  # Sekunden in einer Stunde.
    minuten = (dauer // 60) - (stunden * 60)  # Berechnung der Minuten - Abzueglich der bereits berechneten Stunden.
    sekunden = dauer - ((stunden * 3600) + (minuten * 60))
    return [dauer, stunden, minuten, sekunden]
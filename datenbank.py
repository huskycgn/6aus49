import mysql.connector as database


def daten_einfuegen(anzahl_versuche, rechenzeit, ticket, host):
    connection = database.connect(user='lotto_user',
                                  host='192.168.178.22',
                                  database='lotto',
                                  password='NB!Hu9_#@e^2Uc2d')

    mycursor = connection.cursor()
    sql_befehl = "INSERT INTO spiele " \
                 "(nummer, anzahl_versuche, rechenzeit, ticket, host) VALUES " \
                 f"(NULL, {anzahl_versuche}, {rechenzeit}, '{ticket}', '{host}')"
    mycursor.execute(sql_befehl)
    connection.commit()
    connection.close()


def daten_auslesen(spalte):
    connection = database.connect(user='lotto_user',
                                  host='192.168.178.22',
                                  database='lotto',
                                  password='NB!Hu9_#@e^2Uc2d')
    mycursor = connection.cursor()
    sql_befehl = f"SELECT {spalte} FROM spiele;"
    mycursor.execute(sql_befehl)
    datensatz = mycursor.fetchall()
    connection.close()
    return datensatz

'''
daten = daten_auslesen('anzahl_versuche')
datenliste = []

for element in daten:
    datenliste.append(str(element).replace(',', ''))

print(datenliste)
'''
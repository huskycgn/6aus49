import mysql.connector as database


def daten_einfuegen(anzahl_versuche, rechenzeit, ticket):
    connection = database.connect(user='lotto_user',
                                  host='192.168.178.22',
                                  database='lotto',
                                  password='NB!Hu9_#@e^2Uc2d')

    mycursor = connection.cursor()
    sql_befehl = "INSERT INTO spiele " \
                 "(nummer, anzahl_versuche, rechenzeit, ticket) VALUES " \
                 f"(NULL, {anzahl_versuche}, {rechenzeit}, {ticket})"
    mycursor.execute(sql_befehl)
    connection.commit()
    connection.close()


daten_einfuegen(345, 34223, "'[1, 45, 18, 38, 6, 1]'")
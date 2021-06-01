# install mysql-connector-python
import mysql.connector
import sys
import time

mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Spotify"
)
cursor = mysql_db.cursor()

print("                             *****          ********      **      ** ")
print("                            **   **        **             **      ** ")
print("                           **     **      **              ********** ")
print("                          ***********     **     *****    **      ** ")
print("                         **         **     **      **     **      ** ")
print("                        **           **     ********      **      ** ")
print(" ")
print("by Mateusz Janik, Konrad Krzempek & Sławomir Kotula")
time.sleep(5)


def menu():
    print("                                         ladowanie.....")
    time.sleep(3)

    choice = input("""



    1:Wyświetlanie
    2:Dodawanie jednego rekordu
    3:Usuwanie wcześniej dodanego rekordu
    4:Aktualizowanie
    5:Wyjście





    """)

    if choice == "1":
        choice_w = input(""" 
        a - Wykonawcy
        b - Liderzy
        c - Lista utworow
        """)
        if choice_w == "a" or choice_w == "A":
            cursor.execute("select * from Wykonawcy")
            print(cursor.fetchall())
            print("Czy chcesz wrócić do menu? (tak/nie)")
            tak_nie = input()
            if tak_nie == "tak" or tak_nie == "Tak" or tak_nie == "TAK":
                menu()
            elif tak_nie == "nie" or tak_nie == "Nie" or tak_nie == "NIE":
                print("Dobrze, automatyczny powrót do menu nastąpi za 10 sekund")
                time.sleep(10)
                menu()
            else:
                print("Zła odpowiedź")
        elif choice_w == "b" or choice_w == "B":
            cursor.execute("select * from Liderzy")
            print(cursor.fetchall())
            print("Czy chcesz wrócić do menu? (tak/nie)")
            tak_nie = input()
            if tak_nie == "tak" or tak_nie == "Tak" or tak_nie == "TAK":
                menu()
            elif tak_nie == "nie" or tak_nie == "Nie" or tak_nie == "NIE":
                print("Dobrze, automatyczny powrót do menu nastąpi za 10 sekund")
                time.sleep(10)
                menu()
            else:
                print("Zła odpowiedź")
        elif choice_w == "c" or choice_w == "C":
            cursor.execute("select * from `Lista utworów`")
            print(cursor.fetchall())
            print("Czy chcesz wrócić do menu? (tak/nie)")
            tak_nie = input()
            if tak_nie == "tak" or tak_nie == "Tak" or tak_nie == "TAK":
                menu()
            elif tak_nie == "nie" or tak_nie == "Nie" or tak_nie == "NIE":
                print("Dobrze, automatyczny powrót do menu nastąpi za 10 sekund")
                time.sleep(10)
                menu()
            else:
                print("Zła odpowiedź")
                menu()
        else:
            print("Error:coś poszło nie tak")
            menu()
    elif choice == "2":
        print("dodawanie...")
        time.sleep(2)
        cursor.execute("INSERT INTO `Wykonawcy` VALUES ('Dr.Alban','Alban Uzoma Nwapa',1979,0)")
        print("Sukces")
        mysql_db.commit()
        menu()
    elif choice == "3":
        print("usuwanie...")
        time.sleep(2)
        cursor.execute("DELETE from Wykonawcy where `Nazwa zespołu`='Dr.Alban'")
        print("Sukces")
        mysql_db.commit()
        menu()
    elif choice == "4":
        print("zaaktualizowanie danych w tablicy wykonawcy (zamiana 0 na null)")
        cursor.execute(
            "UPDATE Wykonawcy set `Rok zakończenia działalności`=NULL where `Rok zakończenia działalności`=0")
        mysql_db.commit()
        menu()
    elif choice == "5":
        print("Dziękujemy, do widzenia :)")
    else:
        print("Error")
        menu()
menu()

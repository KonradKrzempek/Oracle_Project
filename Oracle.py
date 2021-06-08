# install mysql-connector-python
import cx_Oracle
import os
import sys
import time


#con = cx_Oracle.connect("mati/mati@localhost:1521/XEPDB1")
con = cx_Oracle.connect("proj/proj@localhost:1521/XEPDB1")
cursor = con.cursor()

print("                                *****          ********      **      ** ")
print("                               **   **        **             **      ** ")
print("                              **     **      **              ********** ")
print("                             ***********     **     *****    **      ** ")
print("                            **         **     **      **     **      ** ")
print("                           **           **     ********      **      ** ")
print(" ")
print(" Wirtualny dziekanat ")
print(" ")
print("by Mateusz Janik & Slawek Kotula & Konrad Krzempek")

def oknoDialogowePowrotDoMenu():
    print("Czy chcesz wrócić do menu? (tak/nie)")
    tak_nie = input()
    if tak_nie == "tak" or tak_nie == "Tak" or tak_nie == "TAK":
        menu()
    else:
        print("Wychodzenie z programu...")
        time.sleep(1)


def menu():
    print("                                         ladowanie.....")

    choice = input("""



    1:Wyświetlanie
    2:Dodawanie jednego rekordu
    3:Usuwanie wcześniej dodanego rekordu
    4:Aktualizowanie
    5:CTE
    6:Wyjście





    """)

    if choice == "1":
        choice_w = input(""" 
            a - Pracownicy
            b - Przedmioty
            c - Studenci
            d - Grupy
            e - Zajecia
            
            
            """)
        if choice_w == "a" or choice_w == "A":
            cursor.execute("select * from pracownik")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        elif choice_w == "b" or choice_w == "B":
            cursor.execute("select * from przedmiot")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        elif choice_w == "c" or choice_w == "C":
            cursor.execute("select * from student")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        elif choice_w == "d" or choice_w == "D":
            cursor.execute("select * from grupa")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        elif choice_w == "e" or choice_w == "E":
            cursor.execute("select * from grupa")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        else:
            print("Error:coś poszło nie tak")
            menu()
    elif choice == "2":
        print("dodawanie...")
        #time.sleep(2)
        cursor.execute("insert into przedmiot values (9, 'WCIM')")
        con.commit()
        print("Sukces")
        menu()
    elif choice == "3":
        print("usuwanie...")
        #time.sleep(2)
        cursor.execute("DELETE from przedmiot where idprzedmiotu = 9 ")
        con.commit()
        print("Sukces")
        menu()
    elif choice == "4":
        print("zaaktualizowanie danych w tablicy przedmiot ")
        cursor.execute(
            "UPDATE przedmiot set nazwaprzedmiotu = NULL where idprzedmiotu = 9 ")
        con.commit()
        menu()
    elif choice == "5":
        print("CTE")
        choice_cte = input(""" 
                   1 - CTE Przedmiot
                   2 - CTE Ludzie 
                   3 - CTE Plan zajec dla grupy 1

                   """)
        if choice_cte == "1":
            cursor.execute(
            """
WITH przedmiot_CTE
AS
(   
    SELECT idprzedmiotu, nazwaprzedmiotu as przedmiot
    FROM przedmiot
)
SELECT * from przedmiot_CTE""")
            print(cursor.fetchall())
            oknoDialogowePowrotDoMenu()
        elif choice_cte == "2":
            print("Lista osob bedacych na uczelni")
            cursor.execute(
                """
    WITH ludzie_CTE
    AS
    (   
        SELECT imie, nazwisko
        FROM pracownik
        
        UNION ALL
        
        SELECT imie, nazwisko
        FROM student
    )
    SELECT * from ludzie_CTE""")
            print(cursor.fetchall())
            # con.commit()
            oknoDialogowePowrotDoMenu()
        elif choice_cte == "3":
            print("Plan zajec dla grupy 1")
            cursor.execute(
                """
   WITH plan_CTE
    AS
    (   
        SELECT student.imie, student.nazwisko
        FROM student INNER JOIN zajecia ON student.idStudenta = zajecia.student_IDSTUDENTA
        WHERE grupa_idgrupy = 1
    )
    SELECT * from plan_CTE""")
            print(cursor.fetchall())
            # con.commit()
            oknoDialogowePowrotDoMenu()
    elif choice == "6":
        print("Dziękujemy, do widzenia :)")
    else:
        print("Error")
        menu()


menu()

import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql
import re


# Filmek tábla műveletei:

def filmek_insert():
    try:
        if input_1.get() != "":
            MessageBox.showinfo("Info", "Film azonosito megadasa nem szukseges!")
        elif input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "" or input_6.get() == "":
            MessageBox.showinfo("Info", "A film azonosito mezo kivetelevel minden mezo kotelezo!")
        elif int(input_5.get()) < 1 or int(input_5.get()) > 10 or input_3.get().isnumeric() is False \
                or re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()) == []:
            MessageBox.showinfo("Info", "Nem megfelelo input(ok)!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into filmek values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}","{input_6.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            input_6.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            filmek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmek_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
            input_6.insert(0, lol[5])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Film azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from filmek where film_id="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            input_6.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
                input_6.insert(0, row[5])
            con.close()
            filmek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmek_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "" or input_6.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif int(input_5.get()) < 1 or int(input_5.get()) > 10 or input_3.get().isnumeric() is False \
                or re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()) == []:
            MessageBox.showinfo("Info", "Nem megfelelo input(ok)!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update filmek set cim="{input_2.get()}", jatekido="{input_3.get()}", '
                           f'bemutato="{input_4.get()}", ertekeles="{input_5.get()}", '
                           f'forgalmazo_id="{input_6.get()}" '
                           f'where film_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            input_6.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            filmek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmek_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Film azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from filmek where film_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            input_6.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            filmek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Filmek műfajai tábla műveletei:

def filmmu_insert():
    try:
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj mufaj mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into filmek_mufajai values("{input_1.get()}","{input_2.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            filmek_mufajai_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmmu_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update filmek_mufajai set mufaj="{input_3.get()}" where film_id = "{input_1.get()}" '
                           f'and mufaj = "{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            filmek_mufajai_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmmu_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        input_2.insert(0, lol[1])
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj mufaj mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from filmek_mufajai where film_id="{input_1.get()}" and mufaj="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            filmek_mufajai_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Forgalmazók tábla műveletei:

def forg_insert():
    try:
        if input_1.get() != "":
            MessageBox.showinfo("Info", "Forgalmazo azonosito megadasa nem szukseges!")
        elif input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "A forgalmazo azonosito mezo kivetelevel minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into forgalmazok values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            forgalmazok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def forg_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Forgalmazo azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from forgalmazok where forgalmazo_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            forgalmazok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def forg_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update forgalmazok set nev="{input_2.get()}", alapitdatum="{input_3.get()}", '
                           f'alapito="{input_4.get()}", kozpontorszag="{input_5.get()}" '
                           f'where forgalmazo_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            forgalmazok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def forg_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Forgalmazo azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from forgalmazok where forgalmazo_id="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
            con.close()
            forgalmazok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Gyártók tábla műveletei:

def gyar_insert():
    try:
        if input_1.get() != "":
            MessageBox.showinfo("Info", "Gyarto azonosito megadasa nem szukseges!")
        elif input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "A gyarto azonosito mezo kivetelevel minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into gyartok values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            gyartok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyar_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Gyarto azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from gyartok where gyarto_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            gyartok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyar_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update gyartok set nev="{input_2.get()}", alapitdatum="{input_3.get()}", '
                           f'alapito="{input_4.get()}", kozpontorszag="{input_5.get()}" '
                           f'where gyarto_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            gyartok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyar_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Gyarto azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from gyartok where gyarto_id="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
            con.close()
            gyartok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Gyártások tábla műveletei:

def gyartas_insert():
    try:
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into gyartasok values("{input_1.get()}","{input_2.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            gyartasok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyartas_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        input_2.insert(0, lol[1])
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from gyartasok where gyarto_id="{input_1.get()}" and film_id="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            gyartasok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyartas_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update gyartasok set film_id="{input_3.get()}" where gyarto_id = "{input_1.get()}" '
                           f'and film_id = "{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            gyartasok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Rendezők tábla műveletei:

def rend_insert():
    try:
        if input_1.get() != "":
            MessageBox.showinfo("Info", "Rendezo azonosito megadasa nem szukseges!")
        elif input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "A rendezo azonosito mezo kivetelevel minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into rendezok values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            rendezok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rend_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Rendezo azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from rendezok where rendezo_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            rendezok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rend_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update rendezok set veznev="{input_2.get()}", kernev="{input_3.get()}", '
                           f'szuldatum="{input_4.get()}", nemzetiseg="{input_5.get()}" '
                           f'where rendezo_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            rendezok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rend_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Rendezo azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from rendezok where rendezo_id="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
            con.close()
            rendezok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Rendezések tábla műveletei:

def rendez_insert():
    try:
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into rendezesek values("{input_1.get()}","{input_2.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            rendezesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rendez_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        input_2.insert(0, lol[1])
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from rendezesek where rendezo_id="{input_1.get()}" and film_id="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            rendezesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rendez_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update rendezesek set film_id="{input_3.get()}" where rendezo_id = "{input_1.get()}" '
                           f'and film_id = "{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            rendezesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Színészek tábla műveletei:

def szin_insert():
    try:
        if input_1.get() != "":
            MessageBox.showinfo("Info", "Szinesz azonosito megadasa nem szukseges!")
        elif input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "A szinesz azonosito mezo kivetelevel minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into szineszek values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            szineszek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szin_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Szinesz azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from szineszek where szinesz_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            szineszek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szin_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_4.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update szineszek set veznev="{input_2.get()}", kernev="{input_3.get()}", '
                           f'szuldatum="{input_4.get()}", nemzetiseg="{input_5.get()}" '
                           f'where szinesz_id="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            szineszek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szin_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Szinesz azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from szineszek where szinesz_id="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
            con.close()
            szineszek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Szereplések tábla műveletei:

def szerep_insert():
    try:
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into szereplesek values("{input_1.get()}","{input_2.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            szereplesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szerep_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        input_2.insert(0, lol[1])
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito mezo kivetelevel minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from szereplesek where szinesz_id="{input_1.get()}" and film_id="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            szereplesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szerep_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update szereplesek set film_id="{input_3.get()}" where szinesz_id = "{input_1.get()}" '
                           f'and film_id = "{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            szereplesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Felhasználók tábla műveletei:

def user_insert():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into felhasznalok values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}","{input_5.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            felhasznalok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def user_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        if input_1.get() == "":
            MessageBox.showinfo("Info", "Felhasznalonev mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from felhasznalok where felhasznalonev="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            felhasznalok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def user_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif not re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input_3.get()):
            MessageBox.showinfo("Info", "Nem megfelelo datum formatum!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update felhasznalok set jelszo="{input_2.get()}", szuldatum="{input_3.get()}", '
                           f'veznev="{input_4.get()}", kernev="{input_5.get()}" '
                           f'where felhasznalonev="{input_1.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            felhasznalok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def user_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
            input_5.insert(0, lol[4])
        elif input_1.get() == "":
            MessageBox.showinfo("Info", "Felhasznalonev kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from felhasznalok where felhasznalonev="{input_1.get()}"')
            rows = cursor.fetchmany(1)
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            for row in rows:
                input_2.insert(0, row[1])
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
                input_5.insert(0, row[4])
            con.close()
            felhasznalok_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Értékelések tábla műveletei:

def ertek_insert():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "":
            MessageBox.showinfo("Info", "Az uj film azonosito kivetelevel minden mezo kotelezo!")
        elif int(input_4.get()) < 1 or int(input_4.get()) > 10:
            MessageBox.showinfo("Info", "A pont 1 es 10 kozotti szam lehet csak!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'insert into ertekelesek values("{input_1.get()}","{input_2.get()}","{input_3.get()}",'
                           f'"{input_4.get()}")')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Beszuras megtortent!")
            con.close()
            ertekelesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def ertek_delete():
    try:
        vmi = ""
        for i in lista.curselection():
            vmi = lista.get(i)
        lol = vmi.split("    ")
        input_1.insert(0, lol[0])
        input_2.insert(0, lol[1])
        if input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Felhasznalonev es film azonosito mezo kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'delete from ertekelesek where felhasznalonev="{input_1.get()}"'
                           f' and film_id="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Torles megtortent!")
            con.close()
            ertekelesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def ertek_update():
    try:
        if input_1.get() == "" or input_2.get() == "" or input_3.get() == "" or input_4.get() == "" \
                or input_5.get() == "":
            MessageBox.showinfo("Info", "Minden mezo kotelezo!")
        elif int(input_4.get()) < 1 or int(input_4.get()) > 10:
            MessageBox.showinfo("Info", "A pont 1 es 10 kozotti szam lehet csak!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'update ertekelesek set film_id="{input_5.get()}", uzenet="{input_3.get()}", '
                           f'pont="{input_4.get()}" '
                           f'where felhasznalonev="{input_1.get()}" and film_id="{input_2.get()}"')
            cursor.execute('commit')
            input_1.delete(0, 'end')
            input_2.delete(0, 'end')
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            input_5.delete(0, 'end')
            MessageBox.showinfo("Info", "Frissites megtortent!")
            con.close()
            ertekelesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def ertek_get():
    try:
        if lista.curselection() != ():
            vmi = ""
            for i in lista.curselection():
                vmi = lista.get(i)
            lol = vmi.split("    ")
            input_1.insert(0, lol[0])
            input_2.insert(0, lol[1])
            input_3.insert(0, lol[2])
            input_4.insert(0, lol[3])
        elif input_1.get() == "" or input_2.get() == "":
            MessageBox.showinfo("Info", "Felhasznalonev es film azonosito kotelezo!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(f'select * from ertekelesek where felhasznalonev="{input_1.get()}" '
                           f'and film_id="{input_2.get()}"')
            rows = cursor.fetchmany(1)
            input_3.delete(0, 'end')
            input_4.delete(0, 'end')
            for row in rows:
                input_3.insert(0, row[2])
                input_4.insert(0, row[3])
            input_5.insert(0, input_2.get())
            con.close()
            ertekelesek_change()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


# Listbox, label, entry es gomb modosito fuggvenyek:

def filmek_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from filmek')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=filmek_insert)
        delete_button.config(command=filmek_delete)
        update_button.config(command=filmek_update)
        get_button.config(command=filmek_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Film azonosito")
        var2.set("Cim")
        var3.set("Jatekido")
        var4.set("Bemutato")
        var5.set("Ertekeles")
        var6.set("Forgalmazo azonosito")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def filmek_mufajai_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from filmek_mufajai')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}'.format(row[0], row[1])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=filmmu_insert)
        delete_button.config(command=filmmu_delete)
        update_button.config(command=filmmu_update)
        btn_config()
        get_button.config(state="disabled")

        var1.set("Film azonosito")
        var2.set("Mufaj")
        var3.set("Uj mufaj")
        var4.set("")
        var5.set("")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def forgalmazok_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from forgalmazok')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=forg_insert)
        delete_button.config(command=forg_delete)
        update_button.config(command=forg_update)
        get_button.config(command=forg_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Forgalmazo azonosito")
        var2.set("Nev")
        var3.set("Alapitas datuma")
        var4.set("Alapito")
        var5.set("Kozpont orszag")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyartok_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from gyartok')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=gyar_insert)
        delete_button.config(command=gyar_delete)
        update_button.config(command=gyar_update)
        get_button.config(command=gyar_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Gyarto azonosito")
        var2.set("Nev")
        var3.set("Alapitas datuma")
        var4.set("Alapito")
        var5.set("Kozpont orszag")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def gyartasok_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from gyartasok')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}'.format(row[0], row[1])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=gyartas_insert)
        delete_button.config(command=gyartas_delete)
        update_button.config(command=gyartas_update)
        btn_config()
        get_button.config(state="disabled")

        var1.set("Gyarto azonosito")
        var2.set("Film azonosito")
        var3.set("Uj film azonosito")
        var4.set("")
        var5.set("")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rendezok_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from rendezok')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=rend_insert)
        delete_button.config(command=rend_delete)
        update_button.config(command=rend_update)
        get_button.config(command=rend_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Rendezo azonosito")
        var2.set("Vezeteknev")
        var3.set("Keresztnev")
        var4.set("Szuletesi datum")
        var5.set("Nemzetiseg")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def rendezesek_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from rendezesek')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}'.format(row[0], row[1])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=rendez_insert)
        delete_button.config(command=rendez_delete)
        update_button.config(command=rendez_update)
        btn_config()
        get_button.config(state="disabled")

        var1.set("Rendezo azonosito")
        var2.set("Film azonosito")
        var3.set("Uj film azonosito")
        var4.set("")
        var5.set("")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szineszek_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szineszek')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=szin_insert)
        delete_button.config(command=szin_delete)
        update_button.config(command=szin_update)
        get_button.config(command=szin_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Szinesz azonosito")
        var2.set("Vezeteknev")
        var3.set("Keresztnev")
        var4.set("Szuletesi datum")
        var5.set("Nemzetiseg")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def szereplesek_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szereplesek')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}'.format(row[0], row[1])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=szerep_insert)
        delete_button.config(command=szerep_delete)
        update_button.config(command=szerep_update)
        btn_config()
        get_button.config(state="disabled")

        var1.set("Szinesz azonosito")
        var2.set("Film azonosito")
        var3.set("Uj film azonosito")
        var4.set("")
        var5.set("")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def felhasznalok_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from felhasznalok')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}    {}'.format(row[0], row[1], row[2], row[3], row[4])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=user_insert)
        delete_button.config(command=user_delete)
        update_button.config(command=user_update)
        get_button.config(command=user_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Felhasznalonev")
        var2.set("Jelszo")
        var3.set("Szuletesi datum")
        var4.set("Vezeteknev")
        var5.set("Keresztnev")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def ertekelesek_change():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from ertekelesek')
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}    {}'.format(row[0], row[1], row[2], row[3])
            lista.insert(lista.size() + 1, insertData)
        con.close()

        insert_button.config(command=ertek_insert)
        delete_button.config(command=ertek_delete)
        update_button.config(command=ertek_update)
        get_button.config(command=ertek_get)
        btn_config()
        get_button.config(state="normal")

        var1.set("Felhasznalonev")
        var2.set("Film azonosito")
        var3.set("Uzenet")
        var4.set("Pont")
        var5.set("Uj film azonosito")
        var6.set("")

        entry_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def leker1():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute("SELECT szineszek.kernev, szineszek.veznev, "
                       "YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, szineszek.szuldatum))) AS eletkor, "
                       "COUNT(szereplesek.szinesz_id) AS szereplesek_db FROM szineszek, szereplesek "
                       "WHERE szereplesek.szinesz_id = szineszek.szinesz_id GROUP BY szineszek.szinesz_id")
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{} {}    {}    {}'.format(row[0], row[1], row[2], row[3])
            lista.insert(lista.size() + 1, insertData)
        con.close()
        leker_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def leker2():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute("SELECT filmek.cim, filmek.jatekido, rendezok.kernev, rendezok.veznev "
                       "FROM filmek, rendezok, rendezesek WHERE "
                       "filmek.jatekido = (SELECT MAX(filmek.jatekido) FROM filmek) "
                       "AND filmek.film_id = rendezesek.film_id AND rendezesek.rendezo_id = rendezok.rendezo_id")
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {} {}'.format(row[0], row[1], row[2], row[3])
            lista.insert(lista.size() + 1, insertData)
        con.close()
        leker_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def leker3():
    try:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute("SELECT forgalmazok.nev, COUNT(filmek.forgalmazo_id) AS kiadott_filmek, "
                       "SUM(filmek.jatekido) AS filmek_hossza_sum FROM filmek, forgalmazok "
                       "WHERE filmek.forgalmazo_id = forgalmazok.forgalmazo_id GROUP BY forgalmazok.forgalmazo_id")
        rows = cursor.fetchall()
        lista.delete(0, lista.size())
        for row in rows:
            insertData = '{}    {}    {}'.format(row[0], row[1], row[2])
            lista.insert(lista.size() + 1, insertData)
        con.close()
        leker_config()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def leker_config():
    try:
        insert_button.config(state="disabled")
        delete_button.config(state="disabled")
        update_button.config(state="disabled")
        get_button.config(state="disabled")

        input_1.config(state="disabled")
        input_2.config(state="disabled")
        input_3.config(state="disabled")
        input_4.config(state="disabled")
        input_5.config(state="disabled")
        input_6.config(state="disabled")

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def btn_config():
    try:
        insert_button.config(state="normal")
        delete_button.config(state="normal")
        update_button.config(state="normal")
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


def entry_config():
    try:
        if var6.get() == "" and var5.get() == "" and var4.get() == "":
            input_1.config(state="normal")
            input_2.config(state="normal")
            input_3.config(state="normal")
            input_4.config(state="disabled")
            input_5.config(state="disabled")
            input_6.config(state="disabled")
        elif var6.get() == "":
            input_1.config(state="normal")
            input_2.config(state="normal")
            input_3.config(state="normal")
            input_4.config(state="normal")
            input_5.config(state="normal")
            input_6.config(state="disabled")
        else:
            input_1.config(state="normal")
            input_2.config(state="normal")
            input_3.config(state="normal")
            input_4.config(state="normal")
            input_5.config(state="normal")
            input_6.config(state="normal")
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")


if __name__ == '__main__':
    try:
        dbhost = 'localhost'
        dbuser = 'root'
        dbpass = ''
        dbname = 'imdb'

        # Ablak
        root = tk.Tk()
        root.geometry("1200x800")
        root.configure(bg="#DF3C5F")
        root.title("Kotelezo program, imdb")

        # Label-ök
        var1 = tk.StringVar()
        var2 = tk.StringVar()
        var3 = tk.StringVar()
        var4 = tk.StringVar()
        var5 = tk.StringVar()
        var6 = tk.StringVar()

        label1 = tk.Label(root, textvariable=var1, font=('bold', 10), bg="#6F9BD1")
        label1.place(x=20, y=30)

        label2 = tk.Label(root, textvariable=var2, font=('bold', 10), bg="#6F9BD1")
        label2.place(x=20, y=60)

        label3 = tk.Label(root, textvariable=var3, font=('bold', 10), bg="#6F9BD1")
        label3.place(x=20, y=90)

        label4 = tk.Label(root, textvariable=var4, font=('bold', 10), bg="#6F9BD1")
        label4.place(x=20, y=120)

        label5 = tk.Label(root, textvariable=var5, font=('bold', 10), bg="#6F9BD1")
        label5.place(x=20, y=150)

        label6 = tk.Label(root, textvariable=var6, font=('bold', 10), bg="#6F9BD1")
        label6.place(x=20, y=180)

        # input mezők:
        input_1 = tk.Entry()
        input_1.place(x=170, y=30)
        input_1.configure(bg="#6F9BD1")

        input_2 = tk.Entry()
        input_2.place(x=170, y=60)
        input_2.configure(bg="#6F9BD1")

        input_3 = tk.Entry()
        input_3.place(x=170, y=90)
        input_3.configure(bg="#6F9BD1")

        input_4 = tk.Entry()
        input_4.place(x=170, y=120)
        input_4.configure(bg="#6F9BD1")

        input_5 = tk.Entry()
        input_5.place(x=170, y=150)
        input_5.configure(bg="#6F9BD1")

        input_6 = tk.Entry()
        input_6.place(x=170, y=180)
        input_6.configure(bg="#6F9BD1")

        # gombok:
        insert_button = tk.Button(root, text="Beszur", font=('italic', 10), bg='#224193', fg="white",
                                  activeforeground="#D2601A", activebackground="#1D3C45")
        delete_button = tk.Button(root, text="Torol", font=('italic', 10), bg='#224193', fg="white",
                                  activeforeground="#D2601A", activebackground="#1D3C45")
        get_button = tk.Button(root, text="Leker", font=('italic', 10), bg='#224193', fg="white",
                               activeforeground="#D2601A", activebackground="#1D3C45")
        update_button = tk.Button(root, text="Frissit", font=('italic', 10), bg='#224193', fg="white",
                                  activeforeground="#D2601A", activebackground="#1D3C45")

        filmek_tabla = tk.Button(root, text="Filmek", font=('italic', 10), bg='#224193', fg="white",
                                 activeforeground="#D2601A", activebackground="#1D3C45", command=filmek_change)
        film_mufaj_tabla = tk.Button(root, text="Filmek mufajai", font=('italic', 10), bg='#224193', fg="white",
                                     activeforeground="#D2601A", activebackground="#1D3C45", command=filmek_mufajai_change)
        forgalmazok_tabla = tk.Button(root, text="Forgalmazok", font=('italic', 10), bg='#224193', fg="white",
                                      activeforeground="#D2601A", activebackground="#1D3C45", command=forgalmazok_change)
        gyartok_tabla = tk.Button(root, text="Gyartok", font=('italic', 10), bg='#224193', fg="white",
                                  activeforeground="#D2601A", activebackground="#1D3C45", command=gyartok_change)
        gyartasok_tabla = tk.Button(root, text="Gyartasok", font=('italic', 10), bg='#224193', fg="white",
                                    activeforeground="#D2601A", activebackground="#1D3C45", command=gyartasok_change)
        rendezok_tabla = tk.Button(root, text="Rendezok", font=('italic', 10), bg='#224193', fg="white",
                                   activeforeground="#D2601A", activebackground="#1D3C45", command=rendezok_change)
        rendezesek_tabla = tk.Button(root, text="Rendezesek", font=('italic', 10), bg='#224193', fg="white",
                                     activeforeground="#D2601A", activebackground="#1D3C45", command=rendezesek_change)
        szineszek_tabla = tk.Button(root, text="Szineszek", font=('italic', 10), bg='#224193', fg="white",
                                    activeforeground="#D2601A", activebackground="#1D3C45", command=szineszek_change)
        szereplesek_tabla = tk.Button(root, text="Szereplesek", font=('italic', 10), bg='#224193', fg="white",
                                      activeforeground="#D2601A", activebackground="#1D3C45", command=szereplesek_change)
        felhasznalok_tabla = tk.Button(root, text="Felhasznalok", font=('italic', 10), bg='#224193', fg="white",
                                       activeforeground="#D2601A", activebackground="#1D3C45", command=felhasznalok_change)
        ertekelesek_tabla = tk.Button(root, text="Ertekelesek", font=('italic', 10), bg='#224193', fg="white",
                                      activeforeground="#D2601A", activebackground="#1D3C45", command=ertekelesek_change)

        elso_leker = tk.Button(root, text="Elso lekerdezes", font=('italic', 10), bg='#224193', fg="white",
                               activeforeground="#D2601A", activebackground="#1D3C45", command=leker1)
        masodik_leker = tk.Button(root, text="Masodik lekerdezes", font=('italic', 10), bg='#224193', fg="white",
                                  activeforeground="#D2601A", activebackground="#1D3C45", command=leker2)
        harmadik_leker = tk.Button(root, text="Harmadik lekerdezes", font=('italic', 10), bg='#224193', fg="white",
                                   activeforeground="#D2601A", activebackground="#1D3C45", command=leker3)

        insert_button.place(x=20, y=220)
        delete_button.place(x=90, y=220)
        get_button.place(x=160, y=220)
        update_button.place(x=230, y=220)

        filmek_tabla.place(x=20, y=320)
        film_mufaj_tabla.place(x=20, y=370)
        forgalmazok_tabla.place(x=100, y=320)
        gyartok_tabla.place(x=220, y=320)
        gyartasok_tabla.place(x=140, y=370)
        rendezok_tabla.place(x=20, y=420)
        rendezesek_tabla.place(x=20, y=470)
        szineszek_tabla.place(x=120, y=420)
        szereplesek_tabla.place(x=140, y=470)
        felhasznalok_tabla.place(x=20, y=520)
        ertekelesek_tabla.place(x=140, y=520)

        elso_leker.place(x=20, y=620)
        masodik_leker.place(x=150, y=620)
        harmadik_leker.place(x=20, y=670)

        # listboxok, scrollbarok:
        lista = tk.Listbox(root)
        lista.configure(bg="#6F9BD1")
        scrollbar = tk.Scrollbar(lista)
        scrollbar1 = tk.Scrollbar(lista, orient="horizontal")
        scrollbar.pack(side="right", fill="both")
        scrollbar1.pack(side="bottom", fill="x")
        lista.config(yscrollcommand=scrollbar.set)
        lista.config(xscrollcommand=scrollbar1.set)
        scrollbar.config(command=lista.yview)
        scrollbar1.config(command=lista.xview)
        lista.place(x=390, y=30, width=700, height=600)
        filmek_change()

        # Start
        root.mainloop()
    except Exception:
        MessageBox.showinfo("Info", "Hiba tortent!")

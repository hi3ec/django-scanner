#! /usr/bin/env python
import sqlite3
import datetime

def checkMAC(records,mac_address):
    print("Total rows are:  ", len(records))
    for row in records:
        print("MAC_Address: ", row[0]) 
        print("IP_Address: ", row[1])
        print("Date: ", row[2])
        print("\n")
        if row[0] == mac_address:
            print('find device')
            return True
    return False

def WriteToSqlite(mac_address,ip_address):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite')
        cursor = sqliteConnection.cursor()
        data = (mac_address, ip_address, datetime.datetime.now())
        cursor.execute('create table if not exists DEVICEs(mac text, ip text, date date)')
        sqlite_select_query = """SELECT * from DEVICEs"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        check_mac = checkMAC(records,mac_address)

        if check_mac is False:
            cursor.execute("INSERT INTO devices VALUES(?, ?, ?)", data)
            sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from DEVICEs"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        
        print(records)
        print("Total rows are:  ", len(records))
   
       
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return(records)

#! /usr/bin/env python
import sqlite3
import datetime

def checkMAC(records,mac_address):
    print("Total rows are:  ", len(records))

    for row in records:
        print("MAC_Address: ", row[1]) 
        print("IP_Address: ", row[2])
        print("Date: ", row[4])
        print("\n")
        if row[1] == mac_address:
            print('find device')
            return True
    return False

def WriteToSqlite(mac_address,ip_address,os):
    try:
        sqliteConnection = sqlite3.connect('../../db.sqlite3')
        cursor = sqliteConnection.cursor()
        #cursor.execute('create table if not exists blog_devices(mac text, ip text, date date)')
        sqlite_select_query = """SELECT * from blog_devices"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        check_mac = checkMAC(records,mac_address)

        if check_mac is False:
            add_device = ("INSERT INTO blog_devices "
                "(mac_address, ip_address, os, first_time, last_time) "
                "VALUES (?, ?, ?, ?, ?)")
            data_device = (mac_address, ip_address, os, datetime.datetime.now(), datetime.datetime.now())
            cursor.execute(add_device, data_device)
            sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('../../db.sqlite3')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from blog_devices"""
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

#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="data.csv"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with  open(DB_FILE, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    ctr = 0
    for row in reader:
        if ctr == 0:
            header = row
            print(row)



command = "CREATE TABLE roster {0}"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database



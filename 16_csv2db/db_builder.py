#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('data/courses.csv') as coursesFile:
    courses = csv.DictReader(coursesFile)
    for rec in courses:
        string = "INSERT INTO courses VALUES('"
        for val in rec:
             string += rec[val] +"','"
        c.execute(string[0:-2] + ');')

with open('data/peeps.csv') as peepsFile:
    peeps = csv.DictReader(peepsFile)
    for rec in peeps:
        string = "INSERT INTO peeps VALUES(" + "'"
        for val in rec:
             string += rec[val] + "','"
        c.execute(string[0:-2] + ');')

#==========================================================

db.commit() #save changes
db.close()  #close database



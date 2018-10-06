#What - Jeffrey Wu and Sajed Nahian
#SoftDev1 pd6
#K17 Average
#2018-10-06

import sqlite3   #enable control of an sqlite database

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute("SELECT id FROM 'peepstable'")
studentIDs = c.fetchall()
c.execute('CREATE TABLE peeps_avg({0},{1},{2})'.format('name TEXT'
                                                           , 'id INTEGER'
                                                           , 'average NUMERIC'))
for idNo in studentIDs:
    print("SELECT grades FROM 'coursestable' WHERE id = " + str(idNo[0]))
    c.execute("SELECT grades FROM 'coursestable' WHERE id = " + str(idNo[0]))
    grades = c.fetchall()
    gradeSum = 0
    for grade in grades:
        gradeSum += grade[0]
    c.execute("SELECT name FROM 'peepstable' WHERE id = " + str(idNo[0]))
    name = c.fetchone()
    print(name[0])
    c.execute("INSERT INTO peeps_avg VALUES('{0}',{1},{2})".format(name[0],
                                                                   str(idNo[0]),
                                                                   str(gradeSum/3)))
peeps = c.execute('SELECT * from peeps_avg')
for rec in peeps:
    print(rec)

def closeDB ():
	db.commit() #save changes
	db.close()  #close database


closeDB()

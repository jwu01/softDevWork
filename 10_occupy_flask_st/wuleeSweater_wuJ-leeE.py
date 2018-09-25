'''
wuleeSweater-Jeffrey Wu, Emily Lee
SoftDev1 pd6
K#10 -- Jinja Tuning 
2018-09-23
'''

from flask import Flask, render_template
import random

#initializes dictionary
occ={}

#finds position of comma
def first(word):
    place=0
    final=0
    for char in word:
        if char==",":
            final=place #finds the position of the last comma
        place+=1
    return final

file=open("occupations.csv","r") #reads the csv

def isnum(number):
    try:
        float(number)
        return True
    except:
        return False

#enumerates dictionary
for line in file:
    place=first(line) #finds the comma/ where to split the line
    if(isnum(line[place+1:len(line)-1])): #filters if the line has a percentage (therefore is an occupation)
        occ[line[0:place]]=float(line[place+1:len(line)-1]) #splits the line into the "key" before the comma and the "value" afterwards
        
full=float(occ['Total']) #the total percentage
occ.pop('Total') #takes out the bottom line of the total from the dictionary

def randOcc():
    ran = random.uniform(1,full) #gives a random number within a range
    count=0
    for key in occ:
        count+=occ[key] #adds percentages to get rid of overlap between percentages 
        if(count>=ran): #if the percentage is within the occupation's percentage range
            return key


        
app=Flask(__name__)

@app.route("/")
def reroute(): #gives link to the occupations page
    return "<a href='/occupations'> Hw #10 </a>"

@app.route("/occupations")
def hello_world():
    return render_template("template.html",
                           title="Occupations",
                           randomocc=randOcc(), #gives random occupation
                           first="occupation",second="percentage", #the table headings
                           diction=occ) #the dictionary
    
if __name__ == "__main__":
    app.debug = True
    app.run()

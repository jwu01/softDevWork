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
    count=0
    for char in word:
        if char=='"':
            count+=1
        if count!=1:
            if char==",":
                final=place
            else:
                place+=1
        else:
            place+=1
    return final

file=open("occupations.csv","r")

def isnum(number):
    try:
        float(number)
        return True
    except:
        return False

#enumerates dictionary
for line in file:
    place=first(line)
    if(isnum(line[place+1:len(line)-1])):
        occ[line[0:place]]=float(line[place+1:len(line)-1])
        
full=float(occ['Total'])
occ.pop('Total')

def randOcc():
    ran = random.uniform(1,full)
    count=0
    for key in occ:
        count+=occ[key]
        if(count>=ran):
            return key


        
app=Flask(__name__)

@app.route("/")
def reroute(): #gives link to the occupations page
    return "<a href='/occupations'> Hw #10 </a>"

@app.route("/occupations")
def hello_world():
    return render_template("template.html",
                           title="Occupations",
                           randomocc=randOcc(),
                           first="occupation",second="percentage",
                           diction=occ)
    
if __name__ == "__main__":
    app.debug = True
    app.run()

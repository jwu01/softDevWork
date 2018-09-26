'''
wuleeSweater-Jeffrey Wu, Emily Lee
SoftDev1 pd6
K#10 -- Jinja Tuning 
2018-09-23
'''

from flask import Flask, render_template
from util import helper

        
app=Flask(__name__)

@app.route("/")
def reroute(): #gives link to the occupations page
    return "<a href='/occupations'> Hw #10 </a>"

@app.route("/occupations")
def hello_world():
    return render_template("template.html",
                           title="Occupations",
                           randomocc=helper.randOcc(), #gives random occupation
                           first="occupation",second="percentage", #the table headings
                           diction=helper.getDict()) #the dictionary
    
if __name__ == "__main__":
    app.debug = True
    app.run()

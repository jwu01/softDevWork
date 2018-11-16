#Jeffrey Wu
#SoftDev1 pd7
#K26 -- Getting More Rest
#2018-11-16

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/",methods = ["POST", "GET"])
def home():
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer xWNbMaDlQTR7LLsD5djglE3jbrjosHip')
    data = json.dumps({
    "email": "bart@fullcontact.com",
    "webhookUrl": "http://www.fullcontact.com/hook"
    })
    response = urllib.request.urlopen(req,data)
    return render_template("index.html",
                            image = response['url'],
                            explanation = response['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()

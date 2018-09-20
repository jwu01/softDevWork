
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    text = """whats good guys! </br>
              click <a href ="/fun"> here </a>
              to have some fun"""
    return text
    

@app.route("/fun")
def fun():
    msg = """here's some fun </br>
            <a href="/"> go back home</a> </br>
            have some more <a href= "/morefun"> fun </a>"""
    return msg

@app.route("/morefun")
def moreFun():
    msg = """FUNNFUNNFUNNFUNNFUNNFUNNFUNN </br>
            <a href="/"> go back home</a> </br>
            have some less <a href= "/fun"> fun </a>"""
    return msg
   


if __name__ == "__main__":
    app.run(debug=True)
    


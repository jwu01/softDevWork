##Jeffrey Wu
##SoftDev1 pd6
##K<n> -- <Title/Topic/Summary>
##<yyyy>-<mm>-<dd> 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return 'hello3'

if __name__ == "__main__":
    app.debug = True
    app.run()

##IsaacWuton -- Jeffrey Wu and Isaac Jon
##SoftDev1 pd6
##K14 - Do I Know You?
##2018-10-02

from flask import Flask,render_template,request,session,url_for,redirect
from os import urandom

app = Flask(__name__)
username = 'zero123'
password = '1234'
app.secret_key = urandom(32)

@app.route("/")
def home():
    if 'username' in session:
        return render_template('welcome.html', u = username, message = "Welcome ", x = "Logout")
    else:
        return render_template('home.html')

@app.route("/auth")
def authPage():        
    if request.args['username'] != username:
        return render_template('welcome.html', message = "Username incorrect ", x = "retry")
    elif request.args['username'] == username: 
        if request.args['password'] == password:
            session['username'] = username
            return render_template('welcome.html', u = username, message = "Welcome ", x = "Logout")
        else:
            return render_template('welcome.html', message = "Password incorrect", x = "retry")

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("home"))
if __name__ == '__main__':
        app.debug = True
        app.run()

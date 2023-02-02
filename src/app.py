from flask import Flask,render_template,redirect,request,session

app=Flask(__name__)
app.secret_key='a15sacet'

@app.route('/')
def homepage():
    return render_template('Home.html')

@app.route('/Registration')
def registrationpage():
    return render_template('Registration.html')

@app.route('/Login')
def loginpage():
    return render_template('Login.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
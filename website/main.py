from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Underweight')
def underweight():
    return render_template("Underweight.html")

@app.route('/Overweight')
def overweight():
    return render_template("Overweight.html")

@app.route('/Severewasting')
def Severewasting():
    return render_template("Severewasting.html")

@app.route('/Stunting')
def Stunting():
    return render_template("Stunting.html")

@app.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html")


if __name__=='__main__':
    app.run(debug=True)
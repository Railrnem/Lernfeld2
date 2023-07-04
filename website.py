from flask import Flask, render_template, request

import database

app = Flask(__name__)

# Home Page
@app.route("/")
def hello_world():
    return render_template('index.html')


# Open the page to select most important component 
@app.route("/device", methods = ['POST', 'GET'])
def device():
    if request.method == 'GET':
        return f"The URL /device is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form['hardware']
        return render_template('device.html', device=form_data)
        

# Get the best device informations and display the list
@app.route("/list", methods = ['POST', 'GET'])
def list():
    if request.method == 'GET':
        return f"The URL /list is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        db = database.Database()
        if "laptoppart" in request.form:
            print("test")
            laptop_data = request.form['laptoppart']
            categorys = ["Display","Ram (in GB)","Storage (in MB)","Batteryhours"]
            result = db.getLaptopHighScore(laptop_data.lower())
            return render_template('list.html', result = result, categorys = categorys)
        elif "computerpart" in request.form:
            computer_data = request.form['computerpart']
            categorys = ["CPU","GPU","RAM (in GB)","Storage (in MB)"]
            result = db.getComputerHighScore(computer_data.lower())
            return render_template('list.html', result = result, categorys = categorys)
        else:
            print("Failed to print list")


# Runs the test enviroment
app.run(host='localhost', port=5000)
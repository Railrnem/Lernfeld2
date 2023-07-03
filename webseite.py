from flask import Flask, render_template, request

import database

app = Flask(__name__)

# Home Page
@app.route("/")
def hello_world():
    return render_template('index.html')


# Evaluate the selected option from the Home Page and open appropied next page
@app.route("/device", methods = ['POST', 'GET'])
def device():
    if request.method == 'GET':
        return f"The URL /device is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form['hardware']
        if form_data.lower() == 'laptop':
            return render_template('laptop.html')
        if form_data.lower() == 'computer':
            return render_template('computer.html')
        else:
            return render_template('index.html')
        

# Get and lists best laptops
@app.route("/listlaptop", methods = ['POST', 'GET'])
def listlaptop():
    if request.method == 'GET':
        return f"The URL /device is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form['part']
        # Sanity check, that only valid categorys have been selected
        if form_data.lower() == 'display' or form_data.lower() == 'ram' or form_data.lower() == 'storage' or form_data.lower() == 'batteryhours':
            result = database.getLaptopHighScore(form_data.lower())
            return render_template('listlaptop.html', result = result)
        else:
            return render_template('laptop.html')
        

# Get and lists best computer
@app.route("/listcomputer", methods = ['POST', 'GET'])
def listcomputer():
    if request.method == 'GET':
        return f"The URL /device is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form['part']
        # Sanity check, that only valid categorys have been selected
        if form_data.lower() == 'cpu' or form_data.lower() == 'gpu' or form_data.lower() == 'ram' or form_data.lower() == 'storage':
            result = database.getComputerHighScore(form_data.lower())
            return render_template('listcomputer.html', result = result)
        else:
            return render_template('computer.html')

# Runs the test enviroment
app.run(host='localhost', port=5000)
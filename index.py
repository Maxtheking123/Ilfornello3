from flask import Flask, render_template
import os 

dir_path = os.getcwd() + "/files/"
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template(dir_path + 'templates/index.html')

@app.route('/bar')
def Bar():
    return render_template(dir_path + 'templates/bar.html')

@app.route('/thecave')
def TheCave():
    return render_template(dir_path + 'templates/thecave.html')

@app.route('/swirland')
def Swirland():
    return render_template(dir_path + 'templates/swirland.html')

@app.route('/pool')
def Pool():
    return render_template(dir_path + 'templates/pool.html')

@app.route('/projector')
def Projector():
    return render_template(dir_path + 'templates/projector.html')

@app.route('/kitchen')
def Kitchen():
    return render_template(dir_path + 'templates/kitchen.html')

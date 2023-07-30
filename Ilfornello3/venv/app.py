from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('templates/index.html')

@app.route('/bar')
def Bar():
    return render_template('templates/bar.html')

@app.route('/thecave')
def TheCave():
    return render_template('templates/thecave.html')

@app.route('/swirland')
def Swirland():
    return render_template('templates/swirland.html')

@app.route('/pool')
def Pool():
    return render_template('templates/pool.html')

@app.route('/projector')
def Projector():
    return render_template('templates/projector.html')

@app.route('/kitchen')
def Kitchen():
    return render_template('templates/kitchen.html')

if __name__ == '__main__':
    app.run()

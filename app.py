from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/asl')
def asl():
    return render_template('ASL.html')

@app.route('/isl')
def isl():
    return render_template('ISL.html')

@app.route('/start_asl')
def start_asl():
    # Execute applicationA.py
    subprocess.Popen(["python", "applicationA.py"])
    return "American Sign Language Application Started!"

@app.route('/start_isl')
def start_isl():
    # Execute applicationI.py
    subprocess.Popen(["python", "applicationI.py"])
    return "Indian Sign Language Application Started!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

username='leh'
password='leh123'

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    if not (request.form['username'] == username and request.form['password'] == password):
        return render_template('login-error.html'), 401

    return render_template('login-success.html'), 200

app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_app():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


app.run(debug="True")
from flask import Flask, render_template
#Only for FLASK
import os
n=100
app = Flask(__name__)
#Main page
@app.route('/')
def main_page():
	return render_template('random.html')

#Testing to check if it works
@app.route('/test')
def test():
    return "Frontend Testing Works!"

from . import  main
from flask import render_template

@main.route('/')
def home():
    
    return render_template('home.html')

@main.route('/writer')
def writer():
    return render_template('writer.html')
# myapp/app/routes.py
from flask import Flask, render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # name variable takes an input of the users name
            name = request.form['name']
            # age variable takes an input of the users age
            age = int(request.form['age'])
            # current_year variable takes an input of the current year
            current_year = int(request.form['current_year'])
            # result variable calculates what year you will be 100 by minusing your age from the current year and adding 100
            result = int(current_year) - int(age) + 100
            return render_template('result.html', name=name, result=result)
        except ValueError:
            return "Invalid input. Please enter valid numbers for age and current year."
    return render_template('index.html')
from flask import render_template, request, flash
from application import app
from application.main_scraper import TopFormGoalkeeper, TopFormDefender, TopFormMidfielder, TopFormForward, Differential 

#Routes
@app.route('/')
@app.route('/index')
def index():	
	return render_template('index.html')

@app.route('/priceget/', methods = ['POST'])
def priceget():
	num = request.form['Price']
	try:
		input = float(num)
		num = float(request.form['Price'])
	except ValueError:
		flash('Please enter a specific price.')
		return render_template('index.html')
	
	return render_template('index.html', dif = Differential(num), gk = TopFormGoalkeeper(num), df = TopFormDefender(num), md = TopFormMidfielder(num), fw = TopFormForward(num))
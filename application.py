from flask import Flask, render_template
from scraper import TopFormPlayer
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', player = TopFormPlayer())
	
if __name__ == '__main__':
	app.run()
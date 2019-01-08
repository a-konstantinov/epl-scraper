from flask import Flask

#Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fac236a4a39c269b7dda0d580c9f07af'


from application import routes
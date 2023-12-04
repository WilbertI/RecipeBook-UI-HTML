from flask import Flask
from recipe import bp as recipe

app = Flask(__name__)

app.register_blueprint(recipe, url_prefix = 'recipe')

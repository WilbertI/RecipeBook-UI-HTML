from flask import Flask
from recipe import bp as recipe
from menu import bp as menu

# DataManager Integrations Setup

# Flask Website Setup
app = Flask(__name__)
app.register_blueprint(recipe, url_prefix = '/recipe')
app.register_blueprint(menu, url_prefix = '/menu')

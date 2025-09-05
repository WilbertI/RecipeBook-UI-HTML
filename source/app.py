from flask import Flask
from functions.form import bp as form
from views.recipe import bp as recipe
from views.menu import bp as menu

# DataManager Integrations Setup

# Flask Website Setup
app = Flask(__name__)
app.register_blueprint(form, url_prefix = '/forms')
app.register_blueprint(recipe, url_prefix = '/recipe')
app.register_blueprint(menu, url_prefix = '/menu')

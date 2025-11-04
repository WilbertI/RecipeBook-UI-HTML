import yaml
from flask import Flask
from globalconfig import ConfigurationManager
from globalthemes import ThemeManager
from globalthemes import ThemeLoader

from functions.form import bp as form
from views.recipe import bp as recipe
from views.menu import bp as menu

# Application Configuration Setup
config = ConfigurationManager()
config.load('config.cfg', yaml.safe_load)

# Theme Management
themes = ThemeManager()
for theme in config.get('themes.targets'):
    themes.registerTheme(theme)
themes.setDefault(config.get('themes.default'))

loader = ThemeLoader(themes)

# DataManager Integrations Setup

# Flask Website Setup
app = Flask(__name__)
app.jinja_loader = loader

app.register_blueprint(form, url_prefix = '/forms')
app.register_blueprint(recipe, url_prefix = '/recipe')
app.register_blueprint(menu, url_prefix = '/menu')

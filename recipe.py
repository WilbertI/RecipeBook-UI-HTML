from flask import Blueprint
from flask import render_template
from flask import request

import yaml
from recipe_handler import objectify
from database_manager import insert, find

bp = Blueprint('recipe', __name__, url_prefix = '')

@bp.route('/edit', methods = ['GET'])
@bp.route('/<id>/edit')
def recipe_edit(id = None):
    recipe = None;
    page = render_template('recipe_edit.j2', recipe = recipe)
    return page

@bp.route('/edit', methods = ['POST'])
def recipe_store(id = None):
    content = request.form

    # Will be handled by form management system
    with open('datamaps/recipe.yaml', 'r') as file:
        recipe_map = yaml.safe_load(file)

    storable = objectify(content, recipe_map)
    record = insert('recipes', storable)

    return redirect(url_for(recipe_view(record)))

@bp.route('/<id>', methods=['GET'])
def recipe_view(id):
    recipe = find('recipes', id)
    page = render_template('recipe_view.j2', recipe = recipe)
    return page

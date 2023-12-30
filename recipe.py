from flask import Blueprint, render_template, request, redirect, url_for
from database_manager import insert, find, gather

import yaml
from recipe_handler import objectify

bp = Blueprint('recipe', __name__, url_prefix = '')

@bp.route('/edit', methods = ['GET'])
@bp.route('/<id>/edit')
def edit(id = None):
    recipe = None;
    page = render_template('recipe_edit.html.j2', recipe = recipe)
    return page

@bp.route('/edit', methods = ['POST'])
def store(id = None):
    content = request.form

    # Will be handled by form management system
    with open('datamaps/recipe.yaml', 'r') as file:
        recipe_map = yaml.safe_load(file)

    storable = objectify(content, recipe_map)
    result = insert('recipes', storable)

    return redirect(url_for('.view_single', id = result))

@bp.route('/<id>', methods=['GET'])
def view_single(id):
    recipe = find('recipes', id)
    page = render_template('recipe_view.html.j2', recipe = recipe)
    return page

@bp.route('/', methods=['GET'])
def view_list():
    recipes = gather('recipes')
    page = render_template('recipe_list.html.j2', recipes = recipes)
    return page

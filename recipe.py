from flask import Blueprint
from flask import render_template
from flask import request

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
    return content

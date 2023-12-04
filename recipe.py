from flask import Blueprint
from flask import render_template

bp = Blueprint('recipe', __name__, url_prefix = '')

@bp.route('/edit')
@bp.route('/<id>/edit')
def recipe_edit(id = None):
    page = render_template('recipe_edit.j2')
    return page

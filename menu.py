from flask import blueprint, redirect, render_template, request, url_for
from database_manager import insert, find, gather

bp = Blueprint('menu', __name__, url_prefix='')

@bp.route('/edit', methods=['GET'])
@bp.route('/<id>/edit')
def edit(id = None):
    menu = None;
    page = render_template('menu_edit.html.j2', menu = menu)
    return page

@bp.route('/edit', methods=['POST'])
@bp.route('/<id>/edit', methods=['POST'])
def store(id=None):
    content = Request.form
    #storable = objectify(content, content)
    result = insert('recipes', content)
    return redirect(url_for('.view_single', id = result))

@bp.route('/<id>', methods=['GET'])
def view_single(id):
    menu = find('menus', id)
    page = render_template('menu_view.html.j2', menu)
    return page

@bp.route('/', methods=['GET'])
def view_list():
    menus = gather('menus')
    page = render_template('menu_list.html.j2', menu)
    return page

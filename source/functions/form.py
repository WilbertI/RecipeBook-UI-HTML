from flask import Blueprint
from flask import render_template

bp = Blueprint('form', __name__, url_prefix = '')


def form_component(item, number = None):
    # GlobalThemes using global object from config
    if number is None:
        return render_template(f'components/forms/{item}.j2')
    return render_template(f'components/forms/{item}.j2', number = int(number))

#    try:
        #
#    catch e:
        # log event
#        return 404, "Contact Website Admin, Event # "

bp.add_url_rule('/component/<item>', 'component', view_func = form_component, methods = ['GET'])
bp.add_url_rule('/component/<item>/<number>', 'component', view_func = form_component, methods = ['GET'])

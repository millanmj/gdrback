from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__,template_folder='templates')
# , __name__, template_folder='app/templates'

@home_bp.route('/', methods=['GET'])
def ping():
    return render_template('index.html')

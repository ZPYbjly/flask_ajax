
from flask import Blueprint,render_template,redirect,abort,url_for,make_response,session

from wtforms import TextAreaField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
import time,json


fire_bp =Blueprint('fire',__name__)

SECRET_KEY = "secret"

# keys for localhost. Change as appropriate.

RECAPTCHA_PUBLIC_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"
RECAPTCHA_PRIVATE_KEY = "6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu"



class FirePoint:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
    def __str__(self) :
        return self.name

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[DataRequired()])
    recaptcha = RecaptchaField()

@fire_bp.route('/hello/')
@fire_bp.route('/hello/<name>')
def hello(name='z'):
    fire = FirePoint('Modis','z')
    return render_template('hello.html', name=name,fire = fire)

@fire_bp.route('/')
def testa1():
    return redirect(url_for('fire.testa'))
@fire_bp.route('/testa')
def testa():
    abort(404)
    # return "火点首页"
@fire_bp.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp



@fire_bp.route('/test3')
def test3():
    

    data =[{'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'},{'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'}]

   
    data2 = {'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'}
    datajson = json.dumps(data2)
    # print(data['a'])
    return render_template('test3.html', data=data,data2 = datajson)
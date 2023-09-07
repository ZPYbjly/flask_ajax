
from flask import Flask,render_template, jsonify
from flask import request,abort,make_response
import json
import datetime
from flask import flash
from flask import redirect
import json
from flask import session
from flask import url_for
from wtforms import TextAreaField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
import time

DEBUG = True
SECRET_KEY = "secret"

# keys for localhost. Change as appropriate.

RECAPTCHA_PUBLIC_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"
RECAPTCHA_PRIVATE_KEY = "6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu"

app = Flask(__name__)
app.debug=True
app.config.from_object(__name__)

class FirePoint:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
    def __str__(self) :
        return self.name


class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[DataRequired()])
    recaptcha = RecaptchaField()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='z'):
    fire = FirePoint('Modis','z')
    return render_template('hello.html', name=name,fire = fire)



@app.route('/')
def testa1():
    return redirect(url_for('testa'))

@app.route('/testa')
def testa():
    abort(404)
    this_is_never_executed()


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp



@app.route("/test")
def index(form=None):
    if form is None:
        form = CommentForm()
    comments = session.get("comments", [])
    return render_template("test.html", comments=comments, form=form)


@app.route("/add/", methods=("POST",))
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comments = session.pop("comments", [])
        comments.append(form.comment.data)
        session["comments"] = comments
        flash("You have added a new comment")
        return redirect(url_for("index"))
    return index(form)

    


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ


@app.route('/test3')
def test3():
    

    data =[{'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'},{'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'}]

   
    data2 = {'a': '1', 'b': '2', 'c': '3','d':'3','e':'4'}
    datajson = json.dumps(data2)
    # print(data['a'])
    return render_template('test3.html', data=data,data2 = datajson)


@app.route('/start',methods=['POST','GET'])

def start():
    return render_template('login.html')

@app.route('/testajax',methods=['POST','GET'])
def testajax():
    test_dict = { 'week': ['西安','大同','北京','天津','上海','南京','呼和浩特市'], 'numbers': [12,2,14,7,8,6,4]}
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info['number_p'] = '232'
    info['number_c'] = '233'
    return jsonify(info,test_dict)

@app.route('/test2',methods=['POST','GET'])
def test2():
    test_dict = { 'week': ['西安','大同','北京','天津','上海','南京','呼和浩特市'], 'numbers': [12,2,14,7,8,6,4]} 
    
    data = request.get_data()
    print(data)
    json_data = json.loads(data)
    print(json_data)
    
    # province: $('#province').val(),/////////////////
    #         city:  $('#city').val(),
    #         district:$
    province = json_data.get("province")
    city = json_data.get("city")
    district = json_data.get("district")
    print("province is "+province)
    print("city is "+city)
    print("district is "+district)
    
    # 给前端传输json数据
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info['province'] = province
    info['city'] = city
    info['number_p'] = '232'
    info['number_c'] = '233'
    return jsonify(info,test_dict)




@app.route('/download',methods=['POST','GET'])
def download():
    data = request.get_data()
    print(data) 
    json_data = json.loads(data)
    print(json_data)
    
    # province: $('#province').val(),
    #         city:  $('#city').val(),
    #         district:$
        
    province = json_data.get("province")
    city = json_data.get("city")
    district = json_data.get("district")
    firetype = json_data.get("firetype")
    firesource = json_data.get("firesource")

    print("firetype is "+firetype)
    print("firesource is "+firesource)
   
    print("province is "+province)
    print("city is "+city)
    print("district is "+district)
    
    # 给前端传输json数据
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    return jsonify(info)

@app.route('/firmdownload', methods=['POST','GET'])
def login1():
    return render_template('firmdownload.html')



@app.route('/login', methods=['POST','GET'])
def login():
    # 获取前端json数据
    data = request.get_data()
    print(data)
    json_data = json.loads(data)
    print(json_data)
    
    Id = json_data.get("userId")
    password = json_data.get("password")
    print("userId is "+Id)
    print("password is "+password)
    
    # 给前端传输json数据
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(3)
    
    return jsonify(info)
    

if __name__ == '__main__':
    app.run(port=5000)	# 此处可自定义使用端口
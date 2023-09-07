from flask import Flask,Blueprint,render_template
from flask import request,jsonify
import json
import datetime
import time



login_bp = Blueprint('login_bp',__name__)

@login_bp.route('/start',methods=['POST','GET'])
def start():
    return render_template('login.html')

@login_bp.route('/login', methods=['POST','GET'])
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
from flask import Blueprint,render_template
from flask import request,jsonify
import json,datetime


fireid_bp = Blueprint("fireid_bp",__name__)

@fireid_bp.route('/fireid')
def fireid_index():
    
    comment = ['张','网','刘']
    return render_template('test.html',comments=comment)

@fireid_bp.route('/applyresult',methods=['POST','GET'])
def applyresult():
    data = request.get_data()
    print(data) 
    json_data = json.loads(data)
    print(json_data)
    
    # province: $('#province').val(),
    #         city:  $('#city').val(),
    #         district:$
        
    # province = json_data.get("province")
    # city = json_data.get("city")
    # district = json_data.get("district")
    # firetype = json_data.get("firetype")
    # firesource = json_data.get("firesource")

    # print("firetype is "+firetype)
    # print("firesource is "+firesource)
   
    # print("province is "+province)
    # print("city is "+city)
    # print("district is "+district)
    
    # 给前端传输json数据
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    return jsonify(info)




@fireid_bp.route('/download',methods=['POST','GET'])
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

@fireid_bp.route('/firmdownload', methods=['POST','GET'])
def firmdownload():
    return render_template('firmdownload.html')



@fireid_bp.route('/apply', methods=['POST','GET'])
def apply():
    return render_template('apply_map.html')

@fireid_bp.route('/testajax',methods=['POST','GET'])
def testajax():
    test_dict = { 'week': ['西安','大同','北京','天津','上海','南京','呼和浩特市'], 'numbers': [12,2,14,7,8,6,4]}
    info = dict()
    info['status'] = 'success'
    info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info['number_p'] = '232'
    info['number_c'] = '233'
    return jsonify(info,test_dict)

@fireid_bp.route('/test2',methods=['POST','GET'])
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
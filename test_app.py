from flask import Flask, url_for,request,render_template
import settings
app = Flask(__name__)

app.config.from_object(settings)

@app.route('/')
def demo1():
    print(url_for("book"))  # 注意这个引用的是视图函数的名字 字符串格式
    print(type(url_for("book")))

    return url_for("book")


@app.route('/book_list/')
def book():
    return 'flask_book'


@app.route('/demo2/')


def demo2():
    
    student_url = url_for('student', id=5, name='mark',code='2323') # id 就是动态 path 的 key 必须赋值，															# name 将作为查询字符串传入
    print(student_url)

    return student_url

@app.route('/student/<int:id>/')
def student(id):
    return 'student {}'.format(id)

@app.route('/test1')
def test1():
    comment = ['张','网','刘']
    return render_template('test.html',comments=comment)

if __name__ == "__main__":
    app.run()

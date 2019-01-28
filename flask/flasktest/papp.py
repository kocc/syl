#练习题：为Flask应用增加路由及视图函数
#当访问 http://localhost:5000/courses/linux 时，页面上显示字符串 Courses:linux

from flask import Flask
from flask import url_for


app = Flask(__name__)

@app.route('/course/<name>')
def course(name):
	return 'Course:{}'.format(name)

@app.route('/test')
def test():
	print(url_for('index'))
	print(url_for('index', username='shiyanlou'))
	print(url_for('show_post', post_id=1, _external=True))
	print(url_for('show_post', post_id=2, q='python 03'))
	print(url_for('show_post', post_id=2, q='python 可以'))
	print(url_for('show_post', post_id=2, _anchor='a'))
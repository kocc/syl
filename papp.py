#练习题：为Flask应用增加路由及视图函数
#当访问 http://localhost:5000/courses/linux 时，页面上显示字符串 Courses:linux

from flask import Flask

app = Flask(__name__)

@app.route('/course/<name>')				#127.0.0.1:5000/usr/zlm
def course(name):							#首页会显示Hello zlm
	return 'Course:{}'.format(name)
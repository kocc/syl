#{% ... %} 包含的代码是可以被执行的语句，比如循环语句，继承语法
#{{ ... }} 包含的是 Python 对象，用于解析出这些对象的值，经常用于打印内容
#{# ... #} 用于添加注释，这些注释不会被处理，但是也不会输出到 HTML 源码中；

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True		#每当模板发生改变时会自动重新渲染模板

@app.route('/')
def index():
	teacher = {
		'name':'admin',
		'email':luojin@simplecloud.cn
	}

	course = {
		'name':'Python Basic',
		'teacher':'teacher',
		'user_count':'5348',
		'price':'199.0',
		'lab':'None'
		'is_private':'False'
		'is_member_course':'True'
		'tags':['python', 'big data', 'linux']
	}
	return render_template('index.html',course = course)
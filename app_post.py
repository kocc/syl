#POST请求用于向指定的资源提交待处理的数据，会对服务器上的数据产生影响，传参不放在URL中，而是通过单数据的形式发给服务器
#一般而言，POST 请求是通过表单传递数据的，可以通过 request.form 获取表单数据，通过 request.method 获取当前请求的方法（GET 或 POST）。

from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
	print('method:', request.method)						#查看本次请求的方式
	print('name:', request.form['name'])					#获取name值
	print('name:', request.form.get('passworrd'))			#获取password值
	print('hobbies:', request.form.get.getlist('hobbies'))	#获取hobbies值，因为有多项故用getlist方法
	print('age:', request.form.get('age', default=18))		#如果没有传递age值，可以在程序中设置默认值
	return 'register successed'

if __name__ == '__main__':
	app()

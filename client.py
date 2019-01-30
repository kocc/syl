#该文件模拟要发送数据的客户端。使用py的requests库模拟浏览器发送post请求
#需要提前安装pip3 install requests
import requests

#设置成需要发送的数据
user_info = {'name':'shixiaolou', 'password':'abc123', 'hobbies':['code', 'swim']}

#向URL发送POST请求
r = requests.post("http://127.0.0.1:5000/register", data=user_info)

#打印返回文本
print(r.text)
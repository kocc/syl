#由类的特征被称为属性，行为被称为方法
#类由类名+属性（默认包含的数据）+方法（函数，对数据进行操作）构成。
'''
class Dog:		#创建类。py会自动创建内置的方法或者属性。内置方法前后均有两个下划线__，如__init__
	def __init__(self):		#最常用的内置方法，可对实例进行初始化设置
		self.name = '小白'

dog = Dog()		#创建类的实例对象
dog.name = '旺财'	#给实例对象绑定name属性
print('dog.name')	#访问类的实例对象dog的name属性
'''
#要求输出
#Jackie's id is 101
#Louplus's id is 102

class UserData:
	def __init__(self, ID, Name):
		self.ID = ID
		self.Name = Name

class NewUser(UserData):
	def get_name(self):
		return self.name
	def set_name(self, value):
		self.name = value
	def __repr__(self):
		return '{}\'s ID is {}'.format(self.Name, self.ID)


if __name__ == '__main__':
	user1 = NewUser(101, 'Jack')
	user1.set_name('Jackie')
	user2 = NewUser(102, 'Louplus')
	print(user1)
	print(user2)
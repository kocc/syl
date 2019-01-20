<<<<<<< HEAD
#要求输出
#ERROR
#Jackie
#Louplus

class UserData():
	def __init__(self, id, name):
		self.id = id
		self._name = name

class NewUser(UserData):
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, Name):
		if len(Name) > 3:
			self._name = Name
		else:
			print('ERROR')


if __name__ == '__main__':
	user1 = NewUser(101, 'Jack')
	user1.name = 'Lou'
	user1.name = 'Jackie'
	user2 = NewUser(102, 'Louplus')
	print(user1.name)
=======
#要求输出
#ERROR
#Jackie
#Louplus

class UserData():
	def __init__(self, id, name):
		self.id = id
		self._name = name

class NewUser(UserData):
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, Name):
		if len(Name) > 3:
			self._name = Name
		else:
			print('ERROR')


if __name__ == '__main__':
	user1 = NewUser(101, 'Jack')
	user1.name = 'Lou'
	user1.name = 'Jackie'
	user2 = NewUser(102, 'Louplus')
	print(user1.name)
>>>>>>> 0096e2efa181f047f0e45d587d2bd1af3ff9e6c3
	print(user2.name)
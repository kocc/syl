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
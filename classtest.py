#要求输出
#ID:101 Name:Jack
#ID:102 Name:Louplus

class UserData:
	def __init__(self, ID, Name):
		self.ID = ID
		self.Name = Name

	def __repr__(self):
		return 'ID:{} Name:{}'.format(self.ID, self.Name)


if __name__ == '__main__':
	user1 = UserData(101, 'Jack')
	user2 = UserData(102, 'Louplus')
	print(user1)
	print(user2)

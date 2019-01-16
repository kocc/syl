class UserData:
	def __init__(self, ID, Name):
		self.ID = ID
		self.Name = Name

class NewUser(UserData):
	group = 'shiyanlou-louplus'
	@classmethod
	def get_group(cls):
		return cls.group
	@staticmethod
	def format_userdata(ID, Name):
		return '{}\'s id is {}'.format(Name, ID)

if __name__ == '__main__':
	print(NewUser.get_group())
	print(NewUser.format_userdata(109, 'Lucy'))
	


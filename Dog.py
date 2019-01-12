class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return 'Dog:{}, age:{}'.format(self.name, self.age)
	
dog = Dog('旺财', 2)

print(Dog)
print(dog)
print(dog.name)
print(dog.age)

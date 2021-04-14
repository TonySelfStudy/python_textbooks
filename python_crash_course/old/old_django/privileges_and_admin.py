from user import User
class Admin(User):
	def __init__(
		self, first_name, last_name, 
		city='sacramento', state='ca', joined='2020'):
		super().__init__(
			first_name, last_name, 
			city, state, joined)
		self.privileges=Privileges(['can add post', 'can delete post', 'can ban user'])

	def show_privileges(self):
		print(f'{self.first_name} has the following admin privileges:\n'
			f'{self.privileges.show_privileges()}')

class Privileges:
	def __init__(self, *privileges):
		self.privileges=[]
		for privilege in privileges:
			self.privileges.append(privilege)
	def show_privileges(self):
		return self.privileges

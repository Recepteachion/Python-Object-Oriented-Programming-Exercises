class Employer:
	def __init__(self,name,surname,money):
		self.name = name
		self.surname = surname
		self.money = money 
		self.mail = self.surname+"."+self.name+"@hotmail"

	def fullname(self):
		return "{} {}".format(self.name,self.surname)

employee1 = Employer("Sansa","Stark",5000)

print(employee1.name)
print(employee1.fullname())
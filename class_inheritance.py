class Employee:
	raise_amt = 1.04

	def __init__(self,first,last,pay):
		self.first = first
		self.last  = last 
		self.pay   = pay 
		self.email = first+'_'+last+'@hotmail.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * raise_amt)

class Develepor(Employee):

	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self,first,last,pay,employees = None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.fullname())


dev_1 = Develepor("John","McKain",5000,prog_lang='Python')
dev_2 = Develepor("Elisa","Martel",6000,prog_lang="Java")

mng_1 = Manager("Jasy","Frozen",10000,employees=[])

print(mng_1.fullname())
mng_1.add_emp(dev_1)
mng_1.add_emp(dev_2)
print(mng_1.print_emps())
mng_1.remove_emp(dev_2)
print(mng_1.print_emps())


print(isinstance(mng_1,Employee))
print(issubclass(Manager,Employee))

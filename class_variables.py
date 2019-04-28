class Employee:
	raise_amount = 1.05
	num_emps = 0

	def __init__(self,first,last,pay):
		self.first = first
		self.last  = last
		self.pay   = pay
		self.email = first+'_'+self.last+'@hotmail.com'

		Employee.num_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

print("Number of Employees :",Employee.num_emps)
emp_1 = Employee('Jhon','Snow',5000)
emp_2 = Employee('Theon','Greyjoy',5000)
emp_3 = Employee('Jessica','Alba',5000)
print("Number of Employees :",Employee.num_emps)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)






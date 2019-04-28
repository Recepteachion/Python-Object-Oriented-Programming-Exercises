class Employee:

	num_emps = 0
	raise_amt = 1.04

	def __init__(self,first,last,pay):
		self.first = first 
		self.last = last 
		self.pay = pay
		self.email = first+'_'+last+'@hotmail.com'

		Employee.num_emps += 1
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = self.pay * self.raise_amt

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt = amount
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)
	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True


emp_str_1 = "Bran-Stark-4000"
emp_str_2 = "Danerys-Targarian-7000"


emp_1 = Employee.from_string(emp_str_1)
print(emp_1.email)

import datetime

today = datetime.date(2019,4,29)
print(Employee.is_workday(today))

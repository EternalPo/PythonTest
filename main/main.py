#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# 创建类
## class 语句创建一个新的类定义. 类的名称紧跟在关键字class后, 接着又跟一个冒号.

class Employee:
	def __int__(self, name, empCount):
		self.name = name
		self.empCount = empCount

	def __str__(self):
		return "Employee "%(self.name, self.empCount)

	def displayEmployee(self):
		print (self.name)
		return

emp1 = Employee()

emp1.name = "mamam"

#emp2 = Employee("Manni", 5000)

emp1.displayEmployee()


#print ("Total Employee %d"%Employee.empCount)


